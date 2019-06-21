import requests
import bs4

#res = requests.get('https://pirateproxy.ch/browse/101')

res = requests.get('https://1337x.unblocked.lc/top-100')
soup = bs4.BeautifulSoup(res.text,'lxml')

#divs2= soup.select('.detName')
#mydivs = soup.findAll("div", {"class": "detName"})


for a in soup.find_all('a', href=True):
        print(a['href'])
        print(a.string)
    #print(a.text)
    
    #if 'magnet:?xt=' in a['href']:


    #
#for d in divs2:
 #   print(d['href'],d.text)
 #   exit