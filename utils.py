
import logging
import os
import subprocess
import sys
import glob 
import base64
# import datetime
import time
import re

logging.basicConfig(level=logging.INFO)
logging.addLevelName( logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
logging.addLevelName( logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))

logger = logging.getLogger(__name__)

def get_all_file(source_folder):
	ret = []
	for r, d, f in os.walk(source_folder):
		for file in f:
			if ".smali" in file:
				#print(os.path.join(r, file))
				ret.append(os.path.join(r, file))
	return ret

def file_exits(fpath):
	return os.path.isfile(fpath)



def get_app_version(app_name):
	ret = cmd_get_output("adb shell dumpsys package %s | grep versionCode"%app_name)
	if not ret:
		#raise SystemExit('dumpsys not found on device')
		print("Cannot found package")
		return '1337'
	else:
		try:
			return re.findall(r'\d+',ret)[0]
		except:
			raise SystemExit("Cannot find versioncode")


def project_exits(app_name):

	if not os.path.exists('project/%s'%app_name):
		logger.info("Creating folder project/%s"%app_name)
		os.mkdir('project/%s'%app_name)

	app_version = get_app_version(app_name)
	logger.info("Get app version: %s"%app_version)
	if not os.path.exists('project/%s/%s'%(app_name,app_version)):
		create_project(app_name,app_version)
	else:
		logger.info('Found project/%s/%s'%(app_name,app_version))
	return app_version

def create_project(app_name,app_version):
	logger.info('Create project folder: project/%s/%s'%(app_name,app_version))
	os.mkdir('project/%s/%s'%(app_name,app_version))
	copy_apk_file(app_name,app_version)
	make_smali_code(app_name,app_version)
	#decompile(app_name,app_version)

def hexdump(src, length=16):
	FILTER = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])
	lines = []
	for c in range(0, len(src), length):
		chars = src[c:c+length]
		while u'' in chars:
			chars.remove(u'')
		hex = ' '.join(["%02x" % (int(x) if int(x)>=0 else 0xff+int(x) )for x in chars])
		printable = ''.join(["%s" % ((int(x) <= 127 and FILTER[int(x)]) or '.') for x in chars])
		lines.append("%04x  %-*s  %s\n" % (c, length*3, hex, printable))
	return ''.join(lines)



def which(program):
	def is_exe(fpath):
		return file_exits(fpath)# and os.access(fpath, os.X_OK)

	fpath, fname = os.path.split(program)
	if fpath:
		if is_exe(program):
			return program
	else:
		for path in os.environ["PATH"].split(os.pathsep):
			exe_file = os.path.join(path, program)
			if os.path.isfile(exe_file):
				return exe_file
	return None

def cmd_get_output(cmd):
	logger.info("CMD:"+cmd)
	logger.info("PWD" +  os.getcwd())
	process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr= subprocess.PIPE)
	result,error = process.communicate()
	if error:
		logger.warning(error)
	return result[:-1].decode('utf-8')

def copy_apk_file(process_name,app_version):
	logger.info("Copy apk file %s"%process_name)
	logger.info("Copy apk file %s"%app_version)

	flocation = cmd_get_output('adb shell pm path %s'%process_name)

	if len(flocation):
		logger.info("App location %s" % flocation)
		pull_status = cmd_get_output('adb pull %s project/%s/%s/%s.apk'%(flocation.split(':')[1],process_name,app_version,process_name))
		if 'pulled' not in pull_status:
			raise SystemExit("Cannot pull %s \nError %s",process_name,pull_status)
		assert os.path.isfile('project/%s/%s/%s.apk'%(process_name,app_version,process_name))
	else:
		logger.error("Cannot get app location")
def make_smali_code(process_name,app_version):
	cmd_get_output('unzip -q -o project/%s/%s/%s.apk -d project/tmp'%(process_name,app_version,process_name))
	all_dex = glob.glob('project/tmp/*.dex')
	if not len(all_dex):
		raise SystemExit("Cannot found any dex file")
	for dex_file in all_dex:
		cmd_get_output('java -jar baksmali.jar d %s -o project/%s/%s/smali_code/'%(dex_file,process_name,app_version))
	cmd_get_output('rm -rf project/tmp')

def decompile(process_name,app_version):
	cmd_get_output('./jadx/bin/jadx -d project/%s/%s/java_decompiled/ project/%s/%s/%s.apk'%(process_name,app_version,process_name,app_version,process_name))


def basic_check():
	out = cmd_get_output('adb devices')
	if out == 'List of devices attached\n\n':
		raise SystemExit('Device not found')

def current_time():
	return str(time.time())

