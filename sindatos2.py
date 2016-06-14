
f=open('c:\kk\sindatos_exclude.txt','r')
k=f.readlines()
f.close()
lista=[]
for linea in k:
    kk=linea.strip()
    if  kk and kk[0]!='#':    
        lista.append(kk.split()[0].upper())
if 'kk' not in lista:
    print 'no esta'
    
