# -*- coding: utf-8 -*-
from lxml import etree
doc = etree.parse('MozartPianoSonata.xml')
raiz=doc.getroot()
clave=str(raw_input("Dame una clave(sol o fa): "))
fa=[]
sol=[]
for elem in raiz.find("part"):
    notas=elem.findall("note/pitch")
    for nota in notas:
        if nota.find("octave").text < 4:
            print "fa", nota.find("octave").text
        else:
            print "fsol", nota.find("octave").text