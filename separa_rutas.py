import re
import sys

d={}
p=re.compile('ip route (([0-2]?\d{0,2}\.){3}([0-2]?\d{0,2})) (([0-2]?\d{0,2}\.){3}([0-2]?\d{0,2})) (([0-2]?\d{0,2}\.){3}([0-2]?\d{0,2}))\D*')
rutas = open(sys.argv[1],'r')
for linea in rutas:
    m = p.match(linea)
    ruta=m.group(1)
    mascara=m.group(4)
    gw=m.group(7)
    if d.has_key(gw)==False:
        d[gw]=open("%s.rutas" % (gw,),'w')
    d[gw].write(linea)
    
for gw in d.keys():
    print gw
    d[gw].close()


    