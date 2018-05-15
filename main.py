import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def open_no_newline(path):
    for line in open(path):
        yield line.replace("\r\n", "").replace("\n", "")

keywords = [line for line in open_no_newline("keywords.txt")]
print(keywords)

box = "#content .box-holder > div.item.status-publish"
box_title = ".item-holder .item-frame .item-panel .entry-title a"
box_link = ".item-holder .link-holder a"
course = "div.buy-box button.course-cta[data-purpose=\"buy-this-course-button\"]"

driver = webdriver.Firefox(executable_path="drivers/geckodriver")
driver.get("https://udemycoupon.learnviral.com/coupon-category/free100-discount/")

main_window = driver.current_window_handle

def course_set(title, firefoxElement):
    print(title)
    firefoxElement.find_element_by_css_selector(box_link).click()

    time.sleep(5)
    link_window = driver.window_handles[1]
    driver.switch_to_window(link_window)

    try:
        get_button = driver.find_element_by_css_selector(course)
        print(get_button.text)
    except Exception as e:
        print(e)
        
    driver.close()
    driver.switch_to_window(main_window)

for item in driver.find_elements_by_css_selector(box):
    title = item.find_element_by_css_selector(box_title).text
    for key in keywords:
        if key in title.lower():
            course_set(title, item)

driver.close()
