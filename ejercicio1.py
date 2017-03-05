# -*- coding: utf-8 -*-
from lxml import etree
doc = etree.parse('MozartPianoSonata.xml')
raiz=doc.getroot()
notas1=[]
compas=str(raw_input("Dame número de compás de 1 a 5: "))
for elem in raiz.find("part"):
    if elem.attrib["number"] == compas:
        notas=elem.findall("note/pitch/step")
        for nota in notas:
            if nota.text not in notas1:
                notas1.append(nota.text)

print "Las notas que aparecén en el compás", compas, "son:"
for nota1 in notas1:
    if nota1 == "C":
        print "do"
    elif nota1 == "D":
        print "re"
    elif nota1 == "E":
        print "mi"
    elif nota1 == "F":
        print "fa"
    elif nota1 == "G":
        print "sol"
    elif nota1 == "A":
        print "la"
    else:
        print "si"