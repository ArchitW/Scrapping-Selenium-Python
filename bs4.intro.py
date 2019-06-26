from bs4 import BeautifulSoup


/***
downloading page via selenium PhantomJS goes here
***/

html_doc = get(....)

''' quit driver '''
driver.quit()

soup = BeautifulSoup(html_doc, 'lxml')

'''open Local file'''
soup= BeautifulSoup(open('local-file.html'),'lxml')

''' reformats HTML '''
soup.prettify()

''' search for first <p> tag '''
first_p_tag = soup.find('p')

'''search for all "a" tag, return list '''
a_tags = soup.find_all('a')
print(a_tags) '''len(a_tags)'''

'''Search with Classes'''
'''find p with class="ClassName"'''
p_tag = soup.find('p', clas_ = 'className')
'''find all p with class="ClassName"'''
p_tag = soup.find_all('p', clas_ = 'className')


'''Search with tag name and other Attributes '''
'''<a href='google.com' id="link1">Google.com</a>'''
a = soup.find_all('a', {'id':'link1'})

'''Search with tag name and String '''
'''<a href='google.com' id="link1">Google.com</a>'''
a = soup.find_all('a', string = 'google.com')

'''Search parent child sibling [tree structure] '''
'''
    <body>
        <p class="search engines">
            <a href='google.com' id="link1">Google.com</a>
            <a href='yahoo.com' id="link2">Yahoo.com</a>
            <a href='bing.com' id="link3">Bing.com</a>
            <a href='duckduckgo.com' id="link4">DuckDuckgo.com</a>
        </p>
    </body>
'''
#Search for all childs
p = soup.find_all('p', class_ = 'searchEngines')
all_p_child = p.findChildern()

# Search for parent
p = soup.find_all('p', class_ = 'searchEngines')
p_parent = soup.findParent() #will return body, cuz its a direct parent


# Search for sibling
first_a = soup.find('p')
remain_sibling = first_a.findNextSiblings() #will return body, cuz its a direct parent



#Extract Data
'''html
<p class="title">
<b>Some title that i need to extract</b>
</p>
<a href='duckduckgo.com' id="link4">DuckDuckgo.com</a>
'''

p_inner_text = soup.find('p').text
a_text = soup.find('a').text


'''Scrap all the Links'''

all_links = soup.find_all('a')
for a in all_links:
    print a['href']

'''Scrape data inside table'''
'''
<table>
  <tbody>
  <tr>
    <td>Row 1 , Col 1</td>
    <td>Row 1 , Col 2</td>
  </tr>
  <tr>
    <td>Row 2 , Col 1</td>
    <td>Row 2 , Col 2</td>
  </tr>
  </tbody>
</table>
'''


for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        print td.text
