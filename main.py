from selenium import webdriver
from selenium.webdriver.common.keys import Keys

box = "#content .box-holder > div.item"
box_title = ".item-holder .item-frame .item-panel .entry-title a"

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://udemycoupon.learnviral.com/coupon-category/free100-discount/")

for item in driver.find_elements_by_css_selector(box):
    title = item.find_element_by_css_selector(box_title).text
    print(title)

driver.close()
