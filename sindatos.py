#!/usr/local/Zope-2.6.2/bin/python

f=open('/usr/local/rtg/sindatos_exclude.txt','r')
k=f.readlines()
f.close()
lista=[]
for linea in k:
    kk=linea.strip()
    if  kk and kk[0]!='#':    
        lista.append(kk.split()[0].upper())

import MySQLdb

db= MySQLdb.connect(host="localhost",user="snmp",passwd="rtgdefault",db="rtg")
cursor = db.cursor()
cursor.execute("SELECT rid,name FROM router")
result=cursor.fetchall()

for router in result: 
	if router[1] not in lista:
		try:
			cursor.execute("SELECT count(*) FROM ifInOctets_%i where substring(dtime,1,10)=CURDATE()" % (router[0]))
			filas=cursor.fetchone()
			if (filas[0] == 0):
				print router[1]," sin datos"
		except:
			print router[1]," sin datos"
