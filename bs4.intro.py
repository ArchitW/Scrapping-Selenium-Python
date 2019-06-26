from bs4 import BeautifulSoup


/***
downloading page via selenium PhantomJS goes here
***/

html_doc = 'some html'

''' quit driver '''
driver.quit()

soup = BeautifulSoup(html_doc, 'lxml')

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
