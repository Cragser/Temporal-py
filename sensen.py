# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import html5lib
import re
import unicodedata

curso = "Curso de Diseño de Interfaces Móviles/"
fileName = "interfaces-moviles.html"
with open(curso+fileName, 'r') as myfile:
  data = myfile.read()
soup = BeautifulSoup(data, 'html5lib')
## Material concept es el folder
for sip in soup.find_all("div", attrs={"class": "Material-concept"}):
  bloque = str(sip.find("h3", attrs={"class": "Material-title"}).string)
  print(bloque)
  path =  "prueba/" + bloque
  if(os.path.isdir( path )):
    print(bloque)
  else:
    os.makedirs( path)
    print("creando " + bloque )
