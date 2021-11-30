from bs4 import BeautifulSoup
import requests

url = 'https://www.getfpv.com/geprc-phantom-2-5-f411-fpv-drone-bnf-frsky-xm.html'

result = requests.get(url)  #sending http get request to retrieve info from URL

doc = BeautifulSoup(result.text, 'html.parser')

prices = doc.find_all(class_ ='price')
parent = prices[0].parent
final = parent.find('span')
print (final.string)