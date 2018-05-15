from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def open_no_newline(path):
    for line in open(path):
        yield line.replace("\r\n", "").replace("\n", "")

keywords = [line for line in open_no_newline("keywords.txt")]
print(keywords)

box = "#content .box-holder > div.item"
box_title = ".item-holder .item-frame .item-panel .entry-title a"
box_link = ".item-holder .link-holder a"

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://udemycoupon.learnviral.com/coupon-category/free100-discount/")

for item in driver.find_elements_by_css_selector(box):
    title = item.find_element_by_css_selector(box_title).text
    for key in keywords:
        if key in title.lower():
            print(title)
            item.find_element_by_css_selector(box_link).click()

driver.close()
