# -*- coding: utf-8 -*-
def conv_notas(nota1):
    notas={"C":"do","D":"re","E":"mi","F":"fa","G":"sol","A":"la","B":"si"}
    return notas[nota1]


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
        print conv_notas(nota)
elif clave == "fa":
    print "Todas las notas de la clave de fa"
    for nota in fa:
        print conv_notas(nota)
