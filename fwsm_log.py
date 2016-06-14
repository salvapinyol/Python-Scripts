import sys

#f=open(sys.argv[1],'r')
#k=f.readlines()
#f.close()
#for linea in k:
#    ip=IP(linea.strip())
#    print ip.net(), ip.strNetmask()

ips_dst = {}
ips_org = {}
f=open("c:\\kk\\fw-yecora\\dns.txt","r")
k=f.readlines()
f.close()
for linea in k:
	#UDP Usuarios 172.29.193.23:53 VDC 10.92.134.153:34699 idle 0:01:29 Bytes 364 FLAGS - D
	if linea[-4:-1]=='- D':
		array = linea.rstrip().split(' ')
		(dst,kk) = array[2].split(":")
		(org,kk) = array[4].split(':')
		if ips_dst.has_key(dst):
			ips_dst[dst] += 1
		else:
			ips_dst[dst] = 1
		if ips_org.has_key(org):
			ips_org[org] += 1
		else:
			ips_org[org] = 1
		
for (key,val) in ips_dst.items():
	if val > 5000:
		print "%s - %s" % (key,val)
	
print "------------------------------------------------------------------"
for (key,val) in ips_org.items():
	if val > 500:
		print "%s - %s" % (key,val)

	 
	  
	
	

