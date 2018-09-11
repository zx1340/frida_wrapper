import argparse
import sys
import time
import frida
import os
import glob
import cmd
from utils import *
from traceconfig import traceconfig

# pylint: disable=W0312,C0303,C0326,C0111,C0301
__metaclass__ = type


class Command(cmd.Cmd):
	def __init__(self,frida):
		cmd.Cmd.__init__(self)
		self.frida = frida

	def do_hello(self, args):
		"""Says hello. If you provide a name, it will greet you with it."""
		if len(args) == 0:
			name = 'stranger'
		else:
			name = args
		print "Hello, %s" % name

	def do_quit(self, args):
		"""Quits the program."""
		print "Quitting."
		raise SystemExit

	def do_fhook(self,args):
		"""Create frida hook function"""
		self.frida.scripts.exports.fh(args)
	
	def do_chook(self,args):
		"""Create frida hook class"""
		self.frida.scripts.exports.ch(args)

	def do_c(self,args):
		"""Continue programe"""
		self.frida.script.exports.c()
	

	def do_smali(self,args):
		"""show smali code"""
		self.frida.data.smali_code(args)

	def do_bt(self,args):
		"""Get backtrace from id"""
		self.frida.get_backtrace(args)


	def do_resume(self,args):
		"""Resume process"""
		self.frida.do_resume()

	
	def do_java(self,args):
		"""Show smali code"""
		self.frida.data.java_code(args)


	def do_unload(self,args):
		"""unload all script"""
		self.frida.scripts.unload()
		logger.info("Script unload")

	def emptyline(self):
		pass

	def do_q(self,args):
		"""Quit"""
		#close file handler before exit
		self.frida.fhandle.close()
		sys.exit()


class Data():
	def __init__(self,fridawp,prj_base):
		self.frida = fridawp
		self.apk_source = prj_base+'base.apk'
		self.smali_loc = prj_base+'/smali_code/'
		self.java_loc = prj_base+'/java_decompiled/'


	def smali_code(self,args):
		fname = self.smali_loc +'/'.join(args.split('.')[:-1])+'.smali'
		method = args.split('.')[-1]

		if file_exits(fname):
			with open(fname,'r') as f:
				data = f.read().split('\n')
			f.close()

			if len(data):
				add = False
				for i in range(len(data)):
					if data[i].startswith('.method') and ' '+method+'(' in data[i]:
						logger.info("Found method %s at line %s: %s"%(method,i,data[i]))
						self.frida.show = False
						# os.system('idea -l '+str(i)+' '+fname)
						os.system('vim +'+str(i)+ ' '+fname)
						self.frida.show = True
						self.frida.show_tmp()
						return
			else:
				logger.warning("File empty")

		else:
			logger.error("File not found: %s"% (fname))

	def java_code(self,args):
		fname = self.java_loc+'/sources/'+'/'.join(args.split('.')[:-1])+'.java'
		method = args.split('.')[-1]
		if file_exits(fname):
			with open(fname,'r') as f:
				data = f.read().split('\n')

			for i in range(len(data)):
				if 'public' in data[i] or 'private' in data[i]:
					if ' '+method +'(' in data[i]:
						logger.info("Found method %s at line %s: %s"%(method,i,data[i]))
						self.frida.show = False
						os.system('vim +'+str(i)+ ' '+fname)
						self.frida.show = True
						self.frida.show_tmp()
						return

class Message():
	def __init__(self,data):
		self.data = data
		self.type = self.data.split('::')[0]
		self.sig = self.data.split('::')[1]
		self.method = self.data.split('::')[2]
		self.args = (self.data.split('::')[3:])
	

	def __str__(self):
		
		if self.type == 'O':
			return "["+self.type+"] | "+self.sig+" | "+self.method+": \t"+self.args[0]+'\n'

		ret = ""
		for i in range(len(self.args)):
			#Array
			if self.args[i].startswith('[') and self.args[i].endswith(']'):
				ret += "["+ self.type+"] | "+self.sig+" | "+ self.method + ":\t[ARG:"+str(i)+"]\n"+hexdump(self.args[i][1:-1].split(','))+'\n'
			else:
				ret += "["+ self.type+"] | "+self.sig+" | "+ self.method + ":\t[ARG:"+str(i)+"]: "+self.args[i]+'\n'
		return ret


class FridaWrapper():
	def __init__(self,args,app_ver,traceconfig):
		self.args = args
		self.app_ver = app_ver
		self.traceconfig = traceconfig
		self.prc_name = args.process_name
		self.prj_base = 'project/'+self.prc_name+'/'+self.app_ver
		self.data = Data(self,self.prj_base)
		self.frida_device = None
		self.scripts = None
		self.bind_device()
		self.create_script()
		self.fhandle = open(self.prj_base+'/'+current_time(),'w')
		self.show = True
		self.tmp = ""
		self.block_sig = ""
		self.msg = []


	def create_script(self):

		with open('core.js','r') as f:
			hook_data = f.read()
		f.close()

		if self.args.attach:
			logger.info("Frida now attach to process")
			try:
				self.frida_prc_name = self.frida_device.get_process(self.prc_name)
			except:
				raise SystemExit("Process not found %s"%self.prc_name)
			session = self.frida_device.attach(self.frida_prc_name)
			self.scripts = session.create_script(hook_data)

			
			self.scripts.on('message', self.on_message)
			self.scripts.load()

			#create script from config file
			for method in self.traceconfig['Method']:
				self.scripts.exports.fh(method)
			
			for _class in self.traceconfig['Class']:
				self.scripts.exports.ch(_class)

		else:
			self.pid = self.frida_device.spawn([self.prc_name])
			logger.info("Spawn pid" + str(self.pid))
			session = self.frida_device.attach(self.pid)

			# somehow script cannot load after frida attach
			# we resume process then load script
			# self.frida_device.resume(self.pid)
			
			self.scripts = session.create_script(hook_data)
			
			self.scripts.on('message', self.on_message)
			self.scripts.load()
			for method in self.traceconfig['Method']:
				print (method)
				self.scripts.exports.fh(method)
			
			for _class in self.traceconfig['Class']:
				self.scripts.exports.ch(_class)

			#TODO: Fix that
			time.sleep(1)
			self.frida_device.resume(self.pid)
		
	
	def get_backtrace(self,args):
		for msg in self.msg:
			if msg.sig == args:
				print msg.method.replace('java.lang.Exception','')

	def do_resume(self):
		self.frida_device.resume(self.pid)
		

	
	def bind_device(self, timeout=0):
		try:
			self.frida_device = frida.get_usb_device(timeout)
			logger.info("Found device: %s" % self.frida_device)
		except:
			logger.error("No devices found")
			sys.exit()

	def on_message(self,message, data):
		#save log
		try:
			self.fhandle.write(message['payload'])
			self.fhandle.flush()
		except:
			logger.warn("Cannot wite:"+str(message))
		
		msg = Message(message['payload'])
		if msg.type == 'BACKTRACE':
			#if 'facebook' in msg.method or 'google' in msg.method:
			for btblock in self.traceconfig['BacktraceBlock']:
				if btblock in msg.method:
					self.block_sig = msg.sig
		else:
			if msg.sig != self.block_sig:
				if self.show:
					print(msg)
				else:
					self.tmp += str(msg) 
		
		self.msg.append(msg)

	def show_tmp(self):
		print(self.tmp)
		self.tmp = ""


def main():
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-p', action="store", dest="process_name", required =False, help="Application process name ")
	parser.add_argument("-a", "--attach",action="store_true",required =False, help="Attach to process")
	
	args = parser.parse_args()
	if not args.process_name:
		logger.exception("Need process name")
		sys.exit()

	basic_check()

	#If project not exit so create it
	app_ver = project_exits(args.process_name)

	fridawrapper = FridaWrapper(args,app_ver,traceconfig)

	Command(fridawrapper).cmdloop()

if __name__== "__main__":
	main()