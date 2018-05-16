import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Courses:
    NEXT_PAGE = "#content div.content-box:nth-child(2) .paging .pages a.next"

    def __init__(self, driver, mainWindow, keywords):
        self.driver = driver
        self.main = mainWindow
        self.keywords = keywords

    def extract(self, pages):
        for i in range(1, pages + 1):
            print("Courses of page ", i)
            self.page_courses()

            if not self.next_page(i, pages):
                print("Not a next page")
                break

    def page_courses(self):
        for course in self.driver.find_elements_by_css_selector(CourseBox.ELEMENT):
            box = CourseBox(course)
            if box.check(self.keywords):
                box.get(self.driver)
                self.driver.switch_to_window(self.main)

    def next_page(self, current, limit):
        try:
            next = self.driver.find_element_by_css_selector(Courses.NEXT_PAGE)
            if current < limit:
                next.click()
                time.sleep(5)
        except Exception as e:
            print("Pages finished ", e)
            return False

        return True

class CourseBox:
    SLEEP = 7
    ELEMENT = "#content .box-holder > div.item.status-publish"
    TITLE = ".item-holder .item-frame .item-panel .entry-title a"
    LINK = ".item-holder .link-holder a"

    def __init__(self, course):
        self.course = course

    def check(self, keywords):
        title = self.course.find_element_by_css_selector(CourseBox.TITLE).text
        print(title)
        for key in keywords:
            if key in title.lower().split():
                print("Course passed")
                return True

        return False

    def get(self, driver):
        self.course.find_element_by_css_selector(CourseBox.LINK).click()
        time.sleep(CourseBox.SLEEP)
        page = CoursePage(driver)
        page.focus()
        page.get()
        page.close()

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

class Session:
    USER = "#login-form #id_email"
    PASSWORD = "#login-form #id_password"
    SUBMIT = "#login-form #submit-id-submit"

    def __init__(self, driver, user, password):
        self.driver = driver
        self.user = user
        self.password = password

    def login(self):
        user = self.driver.find_element_by_css_selector(Session.USER)
        user.clear()
        user.send_keys(self.user)
        password = self.driver.find_element_by_css_selector(Session.PASSWORD)
        password.clear()
        password.send_keys(self.password)
        submit = self.driver.find_element_by_css_selector(Session.SUBMIT)
        submit.click()

class Udemy:
    LOG_IN = "require-auth[data-purpose=header-login] a"

    def __init__(self, driver, keywords):
        self.keywords = keywords
        self.driver = driver
        self.main = self.driver.current_window_handle

    def login(self, address, user, password):
        self.driver.get(address)
        self.driver.find_element_by_css_selector(Udemy.LOG_IN).click()
        time.sleep(1)
        self.fill_form(user, password)

    def fill_form(self, user, password):
        try:
            Session(self.driver, user, password).login()
            time.sleep(10)
        except Exception as e:
            print("Unable to login", e)
            exit(1)

    def extract(self, address, pages):
        self.driver.get(address)
        time.sleep(5)
        Courses(self.driver, self.main, self.keywords).extract(pages)
