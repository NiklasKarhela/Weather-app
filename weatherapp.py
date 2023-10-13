import requests 
from bs4 import BeautifulSoup

city = input("Mistä kaupungista haluat tietää sään: ")
url = "https://www.foreca.fi/Finland/" + city

html = requests.get(url).text
doc = BeautifulSoup(html, 'html.parser')

latest = doc.find_all(class_="obs")
parent = latest[0].parent
temp = parent.find(class_="temp")

print(city + " lämpötila on: " + temp.string)
