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
#print(title)
 bodi=soup.body.find('div',id='content')
 Headder=bodi.h1.text

 print (Headder)
 content_test=bodi.find('div',id='mw-content-text').find('div',class_='mw-parser-output').find_all('p')
 csvfile=open('1stwebscep.txt','w')
 csv_write=csv.writer(csvfile)
 for content in content_test:
    print(content.text)

    print ()
except Exception as e:
    print("you didnt input an wikipidea website")


