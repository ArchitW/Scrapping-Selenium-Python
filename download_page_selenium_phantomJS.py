/***
why : phantom provides selenium to run in headleass mode, i.e no browser popup window

dl: phantomjs.org
***/

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'path to PhantomJS')
driver.get('google.com')

html_doc=driver.page_source

print html_doc