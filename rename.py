import os

fichero = open("e:\\INE-CCIEv5-R&S\\indice.txt","r")

for line in fichero:
    (dest, orig) = [x.strip() for x in line.split("@")]
    print "%s--%s" % (dest, orig)
    os.rename("e:\\INE-CCIEv5-R&S\\"+orig, "e:\\INE-CCIEv5-R&S\\"+dest+".mkv")

fichero.close()    
    