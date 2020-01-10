# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import html5lib
import re
import unicodedata
# sys.setdefaultencoding() does not exist, here!
f = open("execution.py", "w")
g = open("clases.py", "w")
curso = "F:/platzi/Curso de Diseño de Interfaces Móviles/"
fileName = "interfaces-moviles.html"
with open(curso+fileName, 'r') as myfile:
  data = myfile.read()
soup = BeautifulSoup(data, 'html5lib')
folders = []
clases = []

## Material concept es el folder
for sip in soup.find_all("section", attrs={"class": "MaterialList"}):
  bloque = sip.find("h3", attrs={"class": "MaterialList-title"}).contents
  for sep in sip.find_all("div", attrs={"class": "Material-name"}):
    clases.append("'"+sep.string+"'")
  folders.append("'"+bloque[0]+"'")
f.write("def returi():\n\treturn ["+','.join(folders) + "]")
g.write("def returi():\n\treturn ["+','.join(folders) + "]")
f.close()
g.close()
import execution
for folder in execution.returi():
  path =  "prueba/" + folder
  if(os.path.isdir( path )):
    (bloque)
  else:
    os.makedirs( path)
    # print("creando " + folder )
