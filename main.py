import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.udemy import Udemy

def open_no_newline(path):
    for line in open(path):
        yield line.replace("\r\n", "").replace("\n", "")

keywords = [line for line in open_no_newline("keywords.txt")]
print(keywords)

user = "dosramosgabriel@gmail.com"
password = "rustdev2018##"

driver = webdriver.Firefox(executable_path="drivers/geckodriver")

udemy = Udemy(driver, keywords)
udemy.login("https://udemy.com", user, password)
try:
    udemy.extract_page_courses("https://udemycoupon.learnviral.com/coupon-category/free100-discount/")
except Exception as e:
    print(e)

driver.close()
