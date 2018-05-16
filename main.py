import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.udemy import Udemy

# substitute with the udemy account data
class User:
    name = "usename"
    password = "password"

# number of pages to search
pages = 5

def lines(path):
    for line in open(path):
        yield line.replace("\r\n", "").replace("\n", "")

keywords = [line for line in lines("keywords.txt")]
print(keywords)

driver = webdriver.Firefox(executable_path="drivers/geckodriver")

udemy = Udemy(driver, keywords)
udemy.login("https://udemy.com", User.name, User.password)
udemy.extract("https://udemycoupon.learnviral.com/coupon-category/free100-discount/", pages)

driver.close()
