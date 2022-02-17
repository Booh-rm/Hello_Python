'''
==============================================================================================================================
|																															 |
|														MANDATE INTERPRETER													 |
|																															 |
|															   Booh!														 |
|																															 |
==============================================================================================================================

'''
#=============================================================================================================================

from ast import If
import os
import cmd
import console
import shlex
import sys
from core.view import head
from core.help import help
from sys import argv, exit, version_info
import colorama
import re

#=============================================================================================================================

config = {}

#=============================================================================================================================

def main():
	head()
	shell = Shell()
	shell.prompt = colorama.Fore.GREEN + os.getcwd() + '\: My Shell > ' + colorama.Fore.WHITE
	shell.cmdloop()

#=============================================================================================================================	

colors = {'blue':(0,0,1),
          'red':(1,0,0)}

def get_color(color):
	return colors.get(color, None)

def print_in_color(color_name, msg):
	print (msg)

#=============================================================================================================================

def corrections(lines):

	result = []
	for line in lines:

		tabs = 0
		while line.startswith("   "):
			tabs+=1
			line = line[4:]
		line = "\t"*tabs + line

		line = re.sub(r"(\S) {2,}", r"\1 ", line)

		line = re.sub(r"([:;.,]+)(\S)", r"\1 \2", line)

		result.append(line)

	return result

#=============================================================================================================================

class Shell(cmd.Cmd):

	#-------------------------------------------------------------------

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.startup_dir = os.getcwd()

	#-------------------------------------------------------------------

	def do_clr(self, line):
		if sys.platform.startswith('win'):
			command = 'cls'
			os.system(command)
		elif sys.platform.startswith('darwin'):
			command = 'clear'
			os.system(command)
		elif sys.platform.startswith('linux'):
			command = 'clear'
			os.system(command)

	#-------------------------------------------------------------------

	def safe_path(self, path):
		if config.get('allow_unsafe'):
			return True 
		paths = [self.startup_dir, os.path.normpath(path)]
		return self.startup_dir == os.path.commonprefix(paths)

	#-------------------------------------------------------------------

	def do_dir(self, line):
		try:
			for f in sorted(os.listdir(os.getcwd())):
				if os.path.isdir(f):
					print_in_color('blue', f)
				else:
					print_in_color('default', f)
		except OSError as e:
			print (e)

	#-------------------------------------------------------------------

	def do_pwd(self, line):
		print (os.getcwd())
	
	#-------------------------------------------------------------------

	def do_quit(self, inp):
		print (colorama.Fore.RED + "\n" +  "-- BYE --" + "\n" + colorama.Fore.WHITE)
		print(sys.exit())
		return True

	#-------------------------------------------------------------------

	def do_environ(self, line):
		print (os.environ)

	#-------------------------------------------------------------------

	def do_help(self, line):
		help()

	#-------------------------------------------------------------------

	def do_echo(self, line):
		args = shlex.split(line)
		data = args
		try:
			print (corrections(data))
		except Exception as e:
			print('error' + e)

	#-------------------------------------------------------------------

	def do_cat(self, line):
		args = shlex.split(line)
		if len(args) == 0:
			return
		try:
			with open(args[0], 'r') as f:
				for l in f:
					sys.stdout.write(l)
		except Exception as e:
			print_in_color('red', e)
	
	#-------------------------------------------------------------------

	def do_cd(self, line):
		args = shlex.split(line)
		if not args:
			args = ['~/Documents']
		dir = os.path.expanduser(args[0])
		if os.path.exists(dir):
			os.chdir(dir)
			self.do_pwd(line)
			shell = Shell()
			shell.prompt = colorama.Fore.GREEN + os.getcwd() + '\: My Shell > ' + colorama.Fore.WHITE
			shell.cmdloop()
		else:
			print ('Directory does not exist: ' + dir)
	
	#-------------------------------------------------------------------
	
	def do_mkdir(self, line):
		args = shlex.split(line)
		if len(args) == 0:
			return
		if not self.safe_path(os.getcwd()):
			print ('Changes to unsafe directories are disabled.')
			return 
		if os.path.exists(args[0]):
			print ('Directory already exists: ' + args[0])
			return
		try:
			os.mkdir(args[0])
		except OSError as e:
			print( e)

	#-------------------------------------------------------------------

	def do_rm(self, line):
		args = shlex.split(line)
		if len(args) == 0:
			return
		if not os.path.exists(args[0]):
			print ('Invalid path: ' + args[0])
			return 
		elif not self.safe_path(os.path.abspath(args[0])):
			print ('Changes to unsafe directories are disabled.')
			return 
		elif os.path.isdir(args[0]):
			try:
				os.rmdir(args[0])
			except OSError as e:
				print (e)
		else:
			try:
				os.remove(args[0])
			except OSError as e:
				print (e)

	#-------------------------------------------------------------------

#=============================================================================================================================

if __name__ == '__main__':
	main()
