from bs4 import BeautifulSoup
import html5lib
import re

with open('sample.html', 'r') as myfile:
  data = myfile.read()

soup = BeautifulSoup(data, 'html5lib')

for sip in soup.find_all("section", attrs={"class": "MaterialList"}):
  # sep = BeautifulSoup(sip, 'html.parser')
  print(sip.find("h3", attrs={"class": "MaterialList-title"}).string  )
  for ase in (sip.find_all("div", attrs={"class": "Material-name"})):
    print(ase.string)
  print("##################")
# print(soup.prettify())
# ara = re.findall('h3.*Material-title.*?>(.*)</h3.*>', data)
# print(ara)
# ara = re.findall('p.*MaterialItem-copy-title.*?>(.*)</p.*>', data)
# print(ara)



# blocktags = '''\
# <address    <article    <aside
# <blockquote
# <canvas
# <dd    <div    <dl
# <fieldset    <figcaption    <figure    <footer    <form
# <h1    <h2    <h3    <h4    <h5    <h6    <header    <hgroup    <hr
# <li
# <main
# <nav    <noscript
# <ol    <output
# <p    <pre
# <section
# <table    <tfoot
# <ul
# <video'''.split()

# pat = re.compile('(' + '|'.join(blocktags) + ')')

# blocked_str = pat.sub(r'\n\1', str(data))