import urllib
from bs4 import BeautifulSoup
import re
import csv
import requests
import lxml
try:
 source=requests.get(input('enter the wikipidea url:')).text
 soup=BeautifulSoup(source,'lxml')
 html=soup.prettify()
 title=soup.title.text
 bodi=soup.body.find('div',id='content')
 Headder=bodi.h1.text
 content_test=bodi.find('div',id='mw-content-text').find('div',class_='mw-parser-output').find_all('p')

 a=open('webscrap.docs','w',encoding='utf-8')
 a.write(Headder+'\n')
 c=''
 for content in content_test:
    c=c+str(content.text)+'\n\n\n'
    #a.write((content.text))
    #a.write('\n')
 a.write(c)
 a.close()
except Exception as e:
    print('please enter an wikipidea link')
