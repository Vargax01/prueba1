# -*- coding: utf-8 -*-from lxml import etree
def conv_notas(nota1):
    if nota1 == "C":
        return "do"
    elif nota1 == "D":
        return "re"
    elif nota1 == "E":
        return "mi"
    elif nota1 == "F":
        return "fa"
    elif nota1 == "G":
        return "sol"
    elif nota1 == "A":
        return "la"
    else:
        return "si"

from lxml import etree
doc = etree.parse('MozartPianoSonata.xml')
raiz=doc.getroot()
for elem in raiz.find("part"):
    notas=elem.findall("note")
    for nota in notas:
        if nota.find("notations/articulations/staccato") != None:
            print "Compás", elem.attrib["number"], "nota", conv_notas(nota.find("pitch/step").text)