# -*- coding: utf-8 -*-
def conv_notas(nota1):
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


from lxml import etree
doc = etree.parse('MozartPianoSonata.xml')
raiz=doc.getroot()
clave=str(raw_input("Dame una clave(sol o fa): "))
fa=[]
sol=[]
for elem in raiz.find("part"):
    notas=elem.findall("note/pitch")
    for nota in notas:
        if int(nota.find("octave").text) < 4:
                fa.append(nota.find("step").text)
        else:
                sol.append(nota.find("step").text)

if clave == "sol":
    print "Todas las notas de la clave de sol"
    for nota in sol:
        conv_notas(nota)
elif clave == "fa":
    print "Todas las notas de la clave de fa"
    for nota in fa:
        conv_notas(nota)
