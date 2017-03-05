# -*- coding: utf-8 -*-
from lxml import etree
doc = etree.parse('MozartPianoSonata.xml')
raiz=doc.getroot()
nota=str(raw_input("Dame una nota(do,re,mi,fa,sol,la,si): "))
if nota == "do":
    nota1="C"
elif nota == "re":
    nota1="D"
elif nota == "mi":
    nota1="E"
elif nota == "fa":
    nota1="F"
elif nota == "sol":
    nota1="G"
elif nota == "la":
    nota1="A"
else:
    nota1="B"
for elem in raiz.find("part"):
    print "Compas", elem.attrib["number"], ":"
    notas=elem.findall("note/pitch/step")
    cont=0
    for nota2 in notas:
        if nota2.text == nota1:
            cont=cont+1
    if cont == 0:
        print "La nota", nota, "no aparece en este compás"
    else:
        print "La nota", nota,"aparece", cont, "veces"