from hashlib import new
from webbrowser import Chrome
from selenium import webdriver

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get('https://www.youtube.com/watch?v=Xjv1sY630Uc&t=55s')
print(driver.title)



