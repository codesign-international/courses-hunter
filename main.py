import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser
from src import SLEEP_REDO
from src.udemy import Udemy

def lines(path):
    for line in open(path):
        yield line.replace("\r\n", "").replace("\n", "")

config = ConfigParser()
config.read("config.ini")

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.implicitly_wait(2)

udemy = Udemy(driver, [line for line in lines(config["Bot"]["keywords"])])
udemy.login("https://udemy.com", config["Account"]["user"], config["Account"]["password"])

udemy.extract(config["Bot"]["coupons"]) # on first extraction, get all the pages
while True:
    udemy.extract(config["Bot"]["coupons"], int(config["Bot"]["pages"]))
    time.sleep(SLEEP_REDO)

driver.close()
