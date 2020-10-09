from bs4 import BeautifulSoup
import urllib.request
import re

html_page = urllib.request.urlopen('http://automationpractice.com/index.php')
soup = BeautifulSoup(html_page)
links = []
counter = 0

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
	#print("\n")
	#print(link['href'])
	#title = link.get('text')
	#print(title)
	#counter=counter+1
	print(link.text+"\n")

#print(links)


#page = urllib.request.urlopen('http://automationpractice.com/index.php')
#print(page.read())