import sys
import os

country = "FR"
state = "Franche-Comte"
locality = "Montbeliard"
organization = "Web&Design"
organizationalunit = "IT"
email = "hebergement@webetdesign.com"

def checkPath(dest):
	if not os.path.exists(dest):
		os.makedirs(dest)
	if not dest[-1:] == '/':
		dest += '/'
	return dest

def gencsr(host, dest):
	subject = "/C="+country+"/ST="+state+"/L="+locality+"/O="+organization+"/OU="+organizationalunit+"/CN="+host+"/emailAddress="+email
	cmd = "openssl req -new -newkey rsa:2048 -sha256 -nodes -out " + dest+host + ".csr -keyout " + dest+host + ".key -subj '" + subject + "'"
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