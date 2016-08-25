#!/usr/bin/python
 
import os 
import periscope 
import datetime 

now = str(datetime.datetime.now())[:16]

subdl = periscope.Periscope('/home/xbmc/.config/periscope') #IGNORE:E1101
 
skippingWalk = lambda targetDirectory, includedExtentions: (
    (root, dirs, [F for F in files if os.path.splitext(F)[1] in includedExtentions and os.path.splitext(F)[0]+'.srt' not in files])
    for (root, dirs, files) in os.walk(targetDirectory)
)

for line in skippingWalk("/media/datos1/series/nosub", [".avi",".mkv",".mp4"]):
    for fichero in line[2]:
        filepath = line[0] + '/' + fichero
        subtitle = subdl.downloadSubtitle(filepath, ['es'])
        
        print "%s - Subtitulo para %s : %s" % (now, filepath, subtitle and "Bajado" or "No disponible")

        if subtitle: 
            serie = subdl.guessFileData(fichero)['name']
            dest = line[0] + '/../VOS/' + serie + '/' + fichero
            print "%s - Moviendo %s a %s" % (now, filepath, dest)
            os.rename(filepath, dest)           
            subt = os.path.splitext(fichero)[0] + '.srt'
            dest = line[0] + '/../VOS/' + serie + '/' + subt
            os.rename(line[0] + '/' + subt, dest)
