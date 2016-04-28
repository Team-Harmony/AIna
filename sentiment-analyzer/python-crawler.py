import sqlite3
import requests
from bs4 import BeautifulSoup
import re
import urllib2
from urllib2 import Request, urlopen, URLError

li=[]
b=0
url='http://feedback-test.paperplane.io/'
req=Request(url)
try:
    response=urlopen(req)
except URLError, e:
    if hasattr(e, 'reason'):
        print "Failed because ", e
else :
    htmlf = urllib2.urlopen(req)
        
soup = BeautifulSoup(htmlf,"html.parser")
for res in soup.findAll('p', attrs={'class':'lead'}):
    if res and res.get_text().strip() not in li:
        li.append(res.get_text().strip())
        
conn = sqlite3.connect('example.db')
a = 1
c = conn.cursor()
c.execute('''CREATE TABLE listdb(id int primary key,feedback text)''')
for j in li:    
    c.execute("INSERT INTO listdb VALUES(?, ?)",(a,j))
    a += 1   
conn.commit()
for row in c.execute('select feedback from listdb'):
    print row,
conn.close()
print "\n\nSuccess"
