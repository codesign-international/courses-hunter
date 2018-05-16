import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.udemy import Udemy

def open_no_newline(path):
    for line in open(path):
        yield line.replace("\r\n", "").replace("\n", "")

keywords = [line for line in open_no_newline("keywords.txt")]
print(keywords)

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://udemycoupon.learnviral.com/coupon-category/free100-discount/")

udemy = Udemy(driver, keywords)
udemy.extract_page_courses()

driver.close()
