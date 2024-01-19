import argparse
import sys
import time
import frida
import os
import glob
import cmd
from utils import *
from traceconfig import traceconfig
from colored import fg, bg, attr
import subprocess


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
		print ("Hello, %s" % name)

	def do_quit(self, args):
		"""Quits the program."""
		raise SystemExit

	def do_fhook(self,args):
		"""Create frida hook function: fhook android.util.Log.d"""
		self.frida.scripts.exports_sync.fh(args)
	
	def do_chook(self,args):
		"""Create frida hook class"""
		self.frida.scripts.exports_sync.ch(args)
	
	def do_shook(self,args):
		"""Create frida hook all class contain string| """
		allfile = self.frida.data.get_file_name_match(args)
		for fname in allfile:
			print ("\"" + fname + "\",")
			self.frida.scripts.exports_sync.ch(fname)


	def do_fc(self,args):
		""" Find class, filter all android class: fc <filter>"""
		self.frida.scripts.exports_sync.fc(args)

	def do_phook(self,args):
		"""Create frida package hook"""
		allclass = self.frida.data.get_class_name(args)
		for fname in allclass:
			print ("\"" + fname + "\",")
			self.frida.scripts.exports_sync.ch(fname)

	def do_c(self,args):
		"""Continue programe"""
		self.frida.scripts.exports_sync.c()
	
	def do_smali(self,args):
		"""show smali code| smali <class.method>"""
		self.frida.data.smali_code(args)

	def do_bt(self,args):
		"""Get backtrace from id"""
		self.frida.get_backtrace(args)



	def do_rm(self,args):
		"""Rplace method arguiment :rm com.abc.xyz """

		method_name = args.split(' ')[0]
		replace_param = args.split(' ')[1:]

		self.frida.scripts.exports_sync.rm(method_name, )

	def do_resume(self,args):
		"""Resume process"""
		self.frida.do_resume()

	
	def do_java(self,args):
		"""Show smali code| smali <class.method>"""
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
		# self.frida.fhandle.close()
		sys.exit()
	
	def do_help(self,args):
		# Get all command, print help of each command
		if args:
			cmd.Cmd.do_help(self,args)
		else:
			print ("Available command:")
			for i in self.get_names():
				if i.startswith('do_'):
					print("\t"+i[3:] + " : ",end=" ")
					self.do_help(i[3:])

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

	def get_file_name_match(self,args):
		all_file = glob.glob(self.smali_loc + "/*.smali")
		if not len(all_file):
			logger.error("Cannot found smali file")
			return 
		ret = []
		logger.info("Found %s file match" % args)
		for fname in all_file:
			with open(fname) as f:
				if args in f.read():
					if fname not in ret:	
						ret.append(fname.replace(self.smali_loc,'').replace('/','.').replace('.smali',''))
						logger.info("Found %s" % fname)
		return ret	

	def get_class_name(self,args):
		package_location  = self.smali_loc + args.replace('.','/')+ "/*.smali"
		all_file = glob.glob(package_location)
		if not len(all_file):
			logger.error("Cannot found smali file match %s" %(package_location))
			return
		ret = []
		logger.info("Found %d"% len(all_file))
		for fname in all_file:
			with open(fname) as f:
				ret.append(fname.replace(self.smali_loc,'').replace('/','.').replace('.smali',''))
		return ret	

class Message():
	def __init__(self,data):
		self.data = data
		self.type = self.data.split('::')[0]
		self.sig = self.data.split('::')[1]
		self.method = self.data.split('::')[2]
		self.args = (self.data.split('::')[3:])

	def __str__(self):
		
		choose_color = int(self.sig)%15 + 1 # Make sure we dont get black color


		in_or_out = "IN " if self.type == 'I' else "OUT"

		if self.type == 'O':
			if self.args[0].startswith('[') and self.args[0].endswith(']'):
				# Return value is arrayn
				return fg(choose_color) + "["+in_or_out+"] | "+self.sig+" | "+self.method+": \n"+ hexdump(self.args[0][1:-1].split(','))+'\n' +  attr(0)
			else:
				return fg(choose_color) +"["+in_or_out+"] | "+self.sig+" | "+self.method+": \t"+ self.args[0]+'\n'+  attr(0)
		
		
		ret = fg(choose_color)

		ret += "["+ in_or_out +"] | "+self.sig+" | "+ self.method + '\n'
		for i in range(len(self.args)):

			if self.args[i].startswith('[') and self.args[i].endswith(']'):
				ret += "\t"* 6 + ":\t[ARG:"+str(i)+"]\n"+hexdump(self.args[i][1:-1].split(','))+'\n'
			else:
				ret += "\t"* 6 + ":\t[ARG:" + str(i)+"]: "+self.args[i]+'\n'
		return ret + attr(0)


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
		self.show = True
		self.tmp = ""
		self.block_sig = ""
		self.msg = []


	def create_script(self):

		with open('core.js','r') as f:
			hook_data = f.read()
		f.close()
		

		# Check if external.js exits
		if file_exits('external.js'):
			with open('external.js','r') as f:
				hook_data += f.read()
			f.close()

		if self.args.attach:
			logger.info("Frida now attach to process %s" % self.prc_name)
			proc_id = int(subprocess.check_output(f"adb shell pidof {self.prc_name}".split()))
			if not proc_id:
				logger.error("Cannot found process id")
				sys.exit()
			logger.info("Device %s" % self.frida_device)
			session = self.frida_device.attach(proc_id)
			self.scripts = session.create_script(hook_data)
			
			self.scripts.on('message', self.on_message)
			self.scripts.load()

			#create script from config file
			for method in self.traceconfig['Method']:
				self.scripts.exports_sync.fh(method)
			
			for _class in self.traceconfig['Class']:
				self.scripts.exports_sync.ch(_class)

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
				self.scripts.exports_sync.fh(method)
			
			for _class in self.traceconfig['Class']:
				self.scripts.exports_sync.ch(_class)

			#TODO: Fix that
			time.sleep(1)
			self.frida_device.resume(self.pid)
		
	
	def get_backtrace(self,args):
		for msg in self.msg:
			if msg.sig == args:
				print (msg.method.replace('java.lang.Exception',''))

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
		# try:
		# 	self.fhandle.write(message['payload'])
		# 	self.fhandle.flush()
		# except:
		# 	logger.warn("Cannot wite:"+str(message))
		try:
			msg = Message(message['payload'])
		except:
			print ("Cannot parse message", message)

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
		logger.exception("Need process name run with: python main.py -p <process_name>")
		sys.exit()

	basic_check()

	#If project not exit so create it
	app_ver = project_exits(args.process_name)

	fridawrapper = FridaWrapper(args,app_ver,traceconfig)

	Command(fridawrapper).cmdloop()

if __name__== "__main__":
	main()
