#!/usr/bin/env python
import csv

d = {}
   
reader = csv.reader(open("d://traslado//puertos.txt", "rb"))
for row in reader:
    (nombre, velocidad, duplex, vlan, switchpuerto) = row
    (switch,modulo,puerto) = switchpuerto.split('/')
    switch=switch.upper().strip()
    modulo = modulo.strip()[1:]
    puerto = puerto.strip()[1:]
    if d.has_key(switch)==False:
        d[switch]=open("d://traslado//%s" % (switch,),'w')
    d[switch].write('interface gi%s/%s\n' % (modulo, puerto))
    d[switch].write('  description %s\n' % (nombre))
    d[switch].write('  switchport\n')
    d[switch].write('  switchport mode access\n')
    d[switch].write('  switchport access vlan %s\n' % (vlan))
    d[switch].write('  spanning-tree portfast\n')
    d[switch].write('  spanning-tree bpduguard enable\n')
    if velocidad.lower()!='auto':
        d[switch].write('  speed %s\n' % (velocidad))
        d[switch].write('  duplex %s\n' % (duplex))
    d[switch].write('  no shut\n')
    d[switch].write('  exit\n')
    d[switch].write('\n')

for switch in d.keys():
    d[switch].close()

