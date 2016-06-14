import os
import commands
import shutil

PATH = "/media/datos1/Dropbox/libros/"

for fichero in os.listdir(PATH): 
    ( stat, output ) = commands.getstatusoutput( "calibredb add %s" % (PATH + fichero))
    if( stat == 0 ):
        print "Anyadido libro %s con exito." % (fichero,)
        shutil.os.unlink(PATH + fichero)
    else:
        print "ERROR: Fallo al subir a calibre: %s" % output
    