import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# configuration parameters of the bot
from config import USER_NAME, USER_PASS, PAGES, KEYWORDS

from src.udemy import Udemy

driver = webdriver.Firefox(executable_path="drivers/geckodriver")

udemy = Udemy(driver, KEYWORDS)
udemy.login("https://udemy.com", USER_NAME, USER_PASS)
udemy.extract("https://udemycoupon.learnviral.com/coupon-category/free100-discount/", PAGES)

driver.close()
