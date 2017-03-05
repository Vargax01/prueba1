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
print nota1