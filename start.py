Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
import urllib2


Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from bs4 import BeautifulSoup
ImportError: No module named bs4
>>> 


page = urllib2.urlopen('http://klo.ua/')
html = page.read()
soup = BeautifulSoup(html, "html5lib")


ua95 = soup.find("div", {"class": "p-95-ua"})
sup95 = soup.find("div", {"class": "p-95-super"})
ven95 = soup.find("div", {"class": "p-95-ventus"})
dtven = soup.find("div", {"class": "p-ventus-dt"})
dp = soup.find("div", {"class": "p-dp"})


ua95 = soup.find("div", {"class": "p-95-ua"})
sup95 = soup.find("div", {"class": "p-95-super"})
ven95 = soup.find("div", {"class": "p-95-ventus"})
dtven = soup.find("div", {"class": "p-ventus-dt"})
dp = soup.find("div", {"class": "p-dp"})
