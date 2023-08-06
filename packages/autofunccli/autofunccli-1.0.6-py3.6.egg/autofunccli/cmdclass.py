from inspect import isfunction
from .analysis import FunctionArgParser
import argparse
import sys

class cmdfusion():
	"""
	Class allowing to merge multiple function in one command
	"""
	def __init__(self,desc=""):
		self.dct = {}
		self.desc = desc

	def parse(self,arg='',*args):
		"""
		Parse an input using return the result.
		If there is no input, try to parse sys.argv.
		"""
		if(len(args)):
			if(type(arg)==str):
				arg = [arg]
			for i in args:
				arg.append(i)
		if(not(arg)):
			arg = sys.argv[1:] if len(sys.argv)>1 else ['']
		choices = [str(k) for k,v in self.dct.items()]
		epilog = "description:"
		fnDesc = ""
		for k,v in self.dct.items():
			if(len(v.doc.strip())>0):
				fnDesc += "\n\t"+k + "\t\t"+v.doc.strip()
		if(len(fnDesc)==0):epilog=''
		epilog += fnDesc
		self.baseParser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=epilog,description=self.desc)
		self.baseParser.add_argument('cmd',type=str,choices=choices)
		result = self.baseParser.parse_args([arg[0]])
		result = {k:v for k,v in result._get_kwargs()}
		if('cmd' in result):
			if(result['cmd'] in choices):
				return self.dct[result['cmd']].parse(arg[1:])

	def add(self,f):
		"""
		Add the function as a command to the current cmdfusion
		"""
		if(isfunction(f)):
			self.dct[f.__name__] = FunctionArgParser(f)

	def main(self,__name__):
		"""
		Test if it's main or not.
		If yes, parse sys.argv.
		"""
		if(__name__=='__main__'):
			return self.parse()
		else:
			return None
