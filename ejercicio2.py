# -*- coding: utf-8 -*-
from lxml import etree
doc = etree.parse('MozartPianoSonata.xml')
raiz=doc.getroot()
nota=str(raw_input("Dame una nota(do,re,mi,fa,sol,la,si): "))
notas4={"do":"C","re":"D","mi":"E","fa":"F","sol":"G","la":"A","si":"B"}
nota1=notas4[nota]
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