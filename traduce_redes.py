from IPy import IP
import sys

f=open(sys.argv[1],'r')
k=f.readlines()
f.close()
for linea in k:
    ip=IP(linea.strip())
    print ip.net(), ip.strNetmask()