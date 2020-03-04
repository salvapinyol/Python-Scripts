#!/usr/local/Zope-2.6.2/bin/python
# Script que se patea la BD de rtg
# e inserta los errores en la tabla errores
# Modificación creada en pull request2
import MySQLdb

db= MySQLdb.connect(host="localhost",user="snmp",passwd="rtgdefault",db="rtg")
cursor = db.cursor()
cursor.execute("SELECT id,rid,name FROM interface")
result=cursor.fetchall()

for interface in result: 
	ifInErrors=0
	ifOutErrors=0
	ifInDiscards=0
	ifOutDiscards=0
	ifFECN=0
	ifBECN=0
	try:
		cursor.execute("SELECT sum(counter) FROM ifInErrors_%i where id=%i and substring(dtime,1,10)=CURDATE()" % (interface[1],interface[0]))
		errores=cursor.fetchone()
		if errores[0]:
			ifInErrors=errores[0]
	except:
      		ifInErrors=0
	try:
		cursor.execute("SELECT sum(counter) FROM ifOutErrors_%i where id=%i and substring(dtime,1,10)=CURDATE()" % (interface[1],interface[0]))
		errores=cursor.fetchone()
		if errores[0]:
			ifOutErrors=errores[0]
	except:
      		ifOutErrors=0
	try:
		cursor.execute("SELECT sum(counter) FROM ifInDiscards_%i where id=%i and substring(dtime,1,10)=CURDATE()" % (interface[1],interface[0]))
		errores=cursor.fetchone()
		if errores[0]:
			ifInDiscards=errores[0]
	except:
      		ifInDiscards=0
	try:
		cursor.execute("SELECT sum(counter) FROM ifOutDiscards_%i where id=%i and substring(dtime,1,10)=CURDATE()" % (interface[1],interface[0]))
		errores=cursor.fetchone()
		if errores[0]:
			ifOutDiscards=errores[0]
	except:
      		ifOutDiscards=0
	try:
		cursor.execute("SELECT sum(counter) FROM frCircuitReceivedFECNs_%i where id=%i and substring(dtime,1,10)=CURDATE()" % (interface[1],interface[0]))
		errores=cursor.fetchone()
		if errores[0]:
			ifFECN=errores[0]
	except:
      		ifFECN=0
	try:
		cursor.execute("SELECT sum(counter) FROM frCircuitReceivedBECNs_%i where id=%i and substring(dtime,1,10)=CURDATE()" % (interface[1],interface[0]))
		errores=cursor.fetchone()
		if errores[0]:
			ifBECN=errores[0]
	except:
      		ifBECN=0
	# Modificación creada en pull request2
	if (ifInErrors+ifOutErrors+ifInDiscards+ifOutDiscards+ifBECN+ifFECN)>0:
#		print interface[2],"-->",ifInErrors,ifOutErrors,ifInDiscards,ifOutDiscards
		try:
			cursor.execute("INSERT INTO errores VALUES (%i,CURDATE(),%i,%i,%i,%i,%i,%i)" % (interface[0],ifInErrors,ifOutErrors,ifInDiscards,ifOutDiscards,ifFECN,ifBECN))
		except:
			pass
