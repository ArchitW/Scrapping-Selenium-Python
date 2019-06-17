'''
vid:https://www.youtube.com/watch?v=zjo9yFHoUl8
scrap: http://econpy.pythonanywhere.com/ex/001.html

setting up env

$ pip3 install selenium

download : https://github.com/mozilla/geckodriver/releases

sudo cp geckodriver /usr/bin/geckodriver

'''
import csv
from selenium import webdriver


MAX_PAGE_NUM = 5
MAX_PAGE_DIGIT = 3

with open('results.csv','w') as f:
    f.write("Buyers,Price \n")
#1.open up a firefox browser and navigate to webpage

driver = webdriver.Firefox()

for i in range(MAX_PAGE_NUM + 1):
    page_num = (MAX_PAGE_DIGIT - len(str(i))) * "0" + str(i)
    url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"
    driver.get(url)

    #extract list of buyers and prices based on xpath
    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

    # print all buyer prices on current page
    num_page_items = len(buyers)
    with open('results.csv','a') as f:
            for i in range(num_page_items):
                f.write(buyers[i].text +" , "+prices[i].text + "\n") 

#close driver
driver.close()














