import glob, io, inspect, itertools, json, os, subprocess, shlex, sys, tempfile
from os.path import basename, dirname, exists, join
from conans.client.output import ConanOutput
from collections import deque
from natsort import natsorted
import networkx as nx
from .Utility import Utility

class PackageBuilder(object):
	'''
	Provides functionality for building a set of Conan packages
	'''
	
	def __init__(self, rootDir, user, channel, profile, rebuild, dryRun):
		self.rootDir = rootDir
		self.user = user
		self.channel = channel
		self.profile = profile
		self.rebuild = rebuild
		self.dryRun = dryRun
		
		# Cache our list of available packages
		self.availablePackages = self.listAvailablePackages()
	
	def execute(self, command):
		'''
		Executes the supplied command (or just prints it if we're in dry run mode)
		'''
		if self.dryRun == True:
			print(' '.join([shlex.quote(arg) for arg in command]), file=sys.stderr)
			return True
		else:
			return subprocess.call(command) == 0
	
	def listAvailablePackages(self):
		'''
		Retrieves the list of available packages (just the names, not the versions)
		'''
		return Utility.listPackagesInDir(self.rootDir)
	
	def identifyNewestVersion(self, name):
		'''
		Determines the newest version of a package and returns the identifier (name/version)
		'''
		
		# Attempt to retrieve the list of available versions for the package
		versions = natsorted([basename(dirname(v)) for v in glob.glob(join(self.rootDir, name, '*', 'conanfile.py'))])
		if len(versions) == 0:
			raise RuntimeError('no available versions for package "{}"'.format(name))
		
		return '{}/{}'.format(name, versions[-1])
	
	def parsePackage(self, package):
		'''
		Parses a package identifier (name/version) and returns the components
		'''
		return package.split('/', maxsplit=1)
	
	def stripQualifiers(self, package):
		'''
		Strips the username and channel from a fully-qualified package identifier
		'''
		return package.split('@', maxsplit=1)[0]
	
	def getConanfile(self, package):
		'''
		Retrieves the absolute path to the conanfile.py for a package, checking that it exists
		'''
		
		# Determine if we have a conanfile.py for the specified package
		name, version = self.parsePackage(package)
		conanfile = join(self.rootDir, name, version, 'conanfile.py')
		if not exists(conanfile):
			raise RuntimeError('no conanfile.py found for package "{}"'.format(package))
		
		return conanfile
	
	def extractDependencies(self, package):
		'''
		Retrieves the list of dependencies for a package
		'''
		
		# Import the conanfile and instantiate the first recipe class it contains
		module = Utility.importFile('conanfile', self.getConanfile(package))
		classes = inspect.getmembers(module, inspect.isclass)
		recipes = list([c[1] for c in classes if 'ConanFile' in Utility.baseNames(c[1])])
		recipe = recipes[0](ConanOutput(io.StringIO()), None, user=self.user, channel=self.channel)
		
		# Extract the list of dependencies
		dependencies = list(recipe.requires)
		if hasattr(recipe, 'requirements'):
			setattr(recipe, 'requires', lambda d: dependencies.append(d))
			recipe.requirements()
		
		# Filter the dependencies to include only those we are building from our directory tree,
		# which will all use the same username and channel as the package that requires them
		dependencies = list([
			self.stripQualifiers(d)
			for d in dependencies
			if d.endswith('@{}/{}'.format(self.user, self.channel)) == True and
			self.parsePackage(d)[0] in self.availablePackages
		])
		return dependencies
	
	def buildDependencyGraph(self, packages):
		'''
		Builds the dependency graph for the specified list of packages
		'''
		
		# Create the DAG that will act as our dependency graph
		graph = nx.DiGraph()
		
		# Iteratively process our list of packages
		toProcess = deque(packages)
		while len(toProcess) > 0:
			
			# Add the current package to the graph
			current = toProcess.popleft()
			graph.add_node(current)
			
			# Retrieve the dependencies for the package and add them to the graph
			deps = self.extractDependencies(current)
			for dep in deps:
				graph.add_node(dep)
				graph.add_edge(dep, current)
				toProcess.append(dep)
		
		return graph
	
	def fullyQualifiedIdentifier(self, package):
		'''
		Generates the fully-qualified identifier for the specified package
		'''
		return '{}@{}/{}'.format(package, self.user, self.channel)
	
	def isPackageInCache(self, package):
		'''
		Determines if the specified package exists in the local Conan cache
		'''
		
		# Create a temporary file path for the JSON output
		jsonFile = tempfile.NamedTemporaryFile(delete=False)
		jsonFile.close()
		
		# Attempt to perform the search and parse the JSON output
		try:
			fullyQualified = self.fullyQualifiedIdentifier(package)
			searchResult = Utility.capture(['conan', 'search', fullyQualified, '--json', jsonFile.name])
			parsedJSON = json.loads(Utility.readFile(jsonFile.name))
		except:
			parsedJSON = {}
		finally:
			os.unlink(jsonFile.name)
		
		# Determine if the package has at least one binary in the cache
		try:
			return len(parsedJSON['results'][0]['items'][0]['packages']) > 0
		except:
			return False
	
	def buildPackage(self, package, options=[]):
		'''
		Builds an individual package
		'''
		packageDir = dirname(self.getConanfile(package))
		optionsArgs = list(itertools.chain.from_iterable([['-o', option] for option in options]))
		if self.execute(['conan', 'create'] + optionsArgs + [packageDir, '{}/{}'.format(self.user, self.channel), '--profile=' + self.profile]) == False:
			raise RuntimeError('failed to build package "{}"'.format(package))
	
	def uploadPackage(self, package, remote):
		'''
		Uploads the specified package to the specified remote
		'''
		fullyQualified = self.fullyQualifiedIdentifier(package)
		if self.execute(['conan', 'upload', fullyQualified, '--all', '--confirm', '-r', remote]) == False:
			raise RuntimeError('failed to upload package "{}" to remote "{}"'.format(fullyQualified, remote))
	
	def computeBuildOrder(self, packages):
		'''
		Builds the dependency graph for the specified list of packages and computes the build order
		'''
		
		# Build the dependency graph for the packages
		graph = self.buildDependencyGraph(packages)
		
		# Perform a topological sort to determine the build order
		buildOrder = list(nx.topological_sort(graph))
		
		# Determine which packages need to be built
		if self.rebuild == True:
			return buildOrder
		else:
			return list([p for p in buildOrder if self.isPackageInCache(p) == False])
	
	def buildPackages(self, buildOrder, options=[]):
		'''
		Builds a list of packages using a pre-computed build order
		'''
		for package in buildOrder:
			print('\nBuilding package "{}"...'.format(package))
			self.buildPackage(package, options)
	
	def uploadPackages(self, packages, remote):
		'''
		Uploads the specified list of packages to the specified remote
		'''
		for package in packages:
			print('\nUploading package "{}"...'.format(package))
			self.uploadPackage(package, remote)
