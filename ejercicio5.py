# -*- coding: utf-8 -*-from lxml import etree
def conv_notas(nota1):
    notas={"C":"do","D":"re","E":"mi","F":"fa","G":"sol","A":"la","B":"si"}
    return notas[nota1]


from lxml import etree
doc = etree.parse('MozartPianoSonata.xml')
raiz=doc.getroot()
for elem in raiz.find("part"):
    notas=elem.findall("note")
    for nota in notas:
        if nota.find("notations/articulations/staccato") != None:
            print "Compás", elem.attrib["number"], "nota", conv_notas(nota.find("pitch/step").text)
