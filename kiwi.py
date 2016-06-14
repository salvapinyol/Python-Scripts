
import sys

#f=open(sys.argv[1],'r')
#k=f.readlines()
#f.close()
#for linea in k:
#    ip=IP(linea.strip())
#    print ip.net(), ip.strNetmask()

f=open("c:\kk\dispositivos.txt","r")
k=f.readlines()
f.close()
group = "Yecora"
for linea in k:
	(device, ip) = linea.rstrip().split('\t')
	print device + "	Cisco.Switch.IOS	" + group + "	" + ip +"	" + device + "	Other	Direct connect	Telnet	23						KiwiCrypt-qBMwn9R96Q==	KiwiCrypt-qBMzyJRh9YE=			1	1	0																			"
	

