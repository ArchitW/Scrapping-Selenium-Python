from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'path to driver saved')

driver.get('http://python.org')

html_page = driver.page_source

print html_page