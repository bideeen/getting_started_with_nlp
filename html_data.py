# import the libraries
import urllib.request as urllib2
from bs4 import BeautifulSoup
# Fetch the html file
response = urllib2.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')
html_doc = response.read()
# Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')
# formating the parsed html file
strhtm = soup.prettify()
# print few lines
# print(strhtm[:1000])
# Extracting tag value
# print(soup.title)
# print(soup.title.string)
# print(soup.a.string)
# print(soup.b.string)
# Extractiing all instances of a particular tag
# for x in soup.find_all('a'): print(x.string)
# Extractiing all text of a particular tag
# for x in soup.find_all('p'): print(x.string)