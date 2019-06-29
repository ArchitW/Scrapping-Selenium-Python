from selenium import webdriver
from bs4 import BeautifulSoup


""" chrome headless options
https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

# prepare the option for the chrome driver
options = webdriver.ChromeOptions()
options.add_argument('headless')

# start chrome browser
browser = webdriver.Chrome(chrome_options=options)
"""

driver = webdriver.Chrome(executable_path=r'../driver/chromedriver')

base_url = "https://stats.nba.com"
scrap_url = "https://stats.nba.com/players/list/"
driver.get(scrap_url)

#print(driver.page_source)

soup = BeautifulSoup(driver.page_source,'lxml')

div = soup.find('div', class_ = "row")

for a in div.find_all('a'):
    print(a.text)
    print(base_url + a['href'])
#print(div)
driver.quit()
