# -*- coding: utf-8 -*-
from lxml import etree
doc = etree.parse('MozartPianoSonata.xml')
raiz=doc.getroot()
compas=str(raw_input("Dame un compas de 1 a 5: "))
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
comp=False
notas3=[]
for elem in raiz.find("part"):
    if elem.attrib["number"] == compas:
        notas=elem.findall("note/pitch")
        for nota2 in notas:
            if nota2.find("step").text == nota1 and nota2.find("alter") != None:
                comp=True
                notas3.append(nota2.find("step").text)
            elif nota2.find("step").text == nota1:
                notas3.append(nota2.find("step").text)
if len(notas3) == 0:
    print "La nota", nota, "no aparece en el compas", compas
elif comp == False:
    print "La nota", nota, "no esta alterada en el compás", compas
else:
    print "La nota", nota, "esta alterada en el compás", compas