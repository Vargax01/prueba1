# -*- coding: utf-8 -*-from lxml import etree
doc = etree.parse('MozartPianoSonata.xml')
raiz=doc.getroot()
clave=str(raw_input("Dame una clave(sol o fa): "))
for elem in raiz.find("part"):
    notas=notas.findall("note")
    for nota in notas:
        if nota.find("notations/articulations/staccato") != None:
            print nota.find("notations/articulations/staccato")