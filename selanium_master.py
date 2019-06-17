'''
vid:https://www.youtube.com/watch?v=zjo9yFHoUl8
scrap: http://econpy.pythonanywhere.com/ex/001.html

setting up env

$ pip3 install selenium

download : https://github.com/mozilla/geckodriver/releases

sudo cp geckodriver /usr/bin/geckodriver

'''

from selenium import webdriver

#1.open up a firefox browser and navigate to webpage

driver = webdriver.Firefox()
driver.get('http://econpy.pythonanywhere.com/ex/001.html')

#extract list of buyers and prices based on xpath
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# print all buyer prices on current page
num_page_items = len(buyers)
for i in range(num_page_items):
    print(buyers[i].text +" : "+prices[i].text) 

#close driver
driver.close()














