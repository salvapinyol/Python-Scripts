import xml.etree.ElementTree as ET
import urllib

url = 'http://192.168.1.3:32400/library/sections/7/all'

tree = ET.parse(urllib.urlopen(url))
root = tree.getroot()

for child in root:
#    print child.attrib
   t=child.attrib['title']
   for subchild in child:
       for subchild2 in subchild:
           f=subchild2.attrib['file']
           print "%s  @ %s" % (t.ljust(68),f)

