import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CoursePage:
    BUY_BUTTON = "div.buy-box button.course-cta[data-purpose=\"buy-this-course-button\"]"

    def __init__(self, driver):
        self.driver = driver

    def focus(self):
        self.driver.switch_to_window(self.driver.window_handles[1])

    def get(self):
        try:
            button = self.driver.find_element_by_css_selector(CoursePage.BUY_BUTTON)
            button.click()
            time.sleep(5)
        except Exception:
            print("Course already purchased")

    def close(self):
        self.driver.close()

class CourseBox:
    SLEEP = 5
    ELEMENT = "#content .box-holder > div.item.status-publish"
    TITLE = ".item-holder .item-frame .item-panel .entry-title a"
    LINK = ".item-holder .link-holder a"

    def __init__(self, course):
        self.course = course

    def check(self, keywords):
        title = self.course.find_element_by_css_selector(CourseBox.TITLE).text
        for key in keywords:
            if key in title.lower().split():
                print(title)
                return True

        return False

    def get(self, driver):
        self.course.find_element_by_css_selector(CourseBox.LINK).click()
        time.sleep(CourseBox.SLEEP)
        page = CoursePage(driver)
        page.focus()
        page.get()
        page.close()

class Udemy:
    def __init__(self, driver, keywords):
        self.keywords = keywords
        self.driver = driver
        self.main = self.driver.current_window_handle

    def extract_page_courses(self):
        for course in self.driver.find_elements_by_css_selector(CourseBox.ELEMENT):
            box = CourseBox(course)
            if box.check(self.keywords):
                box.get(self.driver)
                self.driver.switch_to_window(self.main)
