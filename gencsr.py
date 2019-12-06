import sys
import os

def checkPath(dest):
	if not os.path.exists(dest):
		os.makedirs(dest)
	if not dest[-1:] == '/':
		dest += '/'
	return dest

def gencsr(host, dest):
	cmd = "openssl req -new -newkey rsa:2048 -sha256 -nodes -out " + dest+host + ".csr -keyout " + dest+host + ".key -subj '/C=FR/CN=" + host + "'"
	cat = "cat " + dest + host + '.csr'
	os.system(cmd)
	os.system(cat)

if len(sys.argv) == 3:
	dest = checkPath(sys.argv[2])
	gencsr(sys.argv[1], dest)
elif len(sys.argv) == 2:
	dest = checkPath('./' + sys.argv[1])
	gencsr(sys.argv[1], dest)
else:
	print ('usage : gencsr host [destination]')