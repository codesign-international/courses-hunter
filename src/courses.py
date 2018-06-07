import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Iterator:
    """ Class to represent an iteration

    Public Properties:
        current (int): the current point
        limit (int): The max point

    Public Methods:
        inside (checks if the iterator is still on the cycle)

    """

    def __init__(self, current, limit):
        """ Creates a new iterator

            Args:
                current (int): the current point
                limit (int): The max point

            Returns:
                new Iterator

            Raises:
                None
        """

        self.current = current
        self.limit = limit

    def inside(self):
        """ Checks if the iterator is still inside

            Returns:
                bool

            Raises:
                None
        """

        return self.current < self.limit

class Courses:
    """ Base class to gestionate the website for the course coupons

    Public Properties:
        driver (WebDriver): the driver to use
        main (Window handle): The main window
        keywords (String Array): list of keywords to match

    Public Methods:
        extract (extracts the udemy coupons present on the url)
    """

    NEXT_PAGE = "#content div.content-box:nth-child(2) .paging .pages a.next"

    def __init__(self, driver, main, keywords):
        """ Creates a new Courses instance

        Args:
            driver (WebDriver): the driver to use
            main (Window handle): The main window
            keywords (String Array): list of keywords to match

        Returns:
            new Courses

        Raises:
            None
        """

        self.driver = driver
        self.main = main
        self.keywords = keywords

    def extract(self, pages):
        """ Extracts all the courses present that match a keyword for n pages

        Args:
            pages (int): Number of pages to verify or None to verify all

        Returns:
            None

        Raises:
            None
        """

        if pages is None:
            self.page_courses()
            while self.next():
                self.page_courses()
        else:
            for i in range(1, pages + 1):
                print("Courses of page ", i)
                self.page_courses()

                if not self.next(Iterator(i, pages)):
                    print("Not a next page")
                    break

    def page_courses(self):
        """ Extracts all the courses present on a single page

            Returns:
                None

            Raises:
                None
        """

        for course in self.driver.find_elements_by_css_selector(CourseBox.ELEMENT):
            box = CourseBox(self.driver, course)
            if box.check(self.keywords):
                box.get()
                self.driver.switch_to_window(self.main)

    def next(self, iterator=None):
        """ Checks if there is a next page

            Args:
                iterator (Iterator object): The itetator to keep track

            Returns:
                bool

            Raises:
                None
        """

        try:
            next = self.driver.find_element_by_css_selector(Courses.NEXT_PAGE)
            if iterator is None or iterator.inside():
                next.click()
                time.sleep(5)
        except Exception as e:
            print("Pages finished ", e)
            return False

        return True

class CourseBox:
    """ Class to represent the div containing the course

    Public Properties:
        driver (WebDriver): the driver to use
        course (CourseBoxHTML Element): The HTML element representing the course

    Public Methods:
        check (checks if the course matches the keywords)
        get (gets the course for the udemy account)
    """

    SLEEP = 7
    ELEMENT = "#content .box-holder > div.item.status-publish"
    TITLE = ".item-holder .item-frame .item-panel .entry-title a"
    LINK = ".item-holder .link-holder a"

    def __init__(self, driver, course):
        """ Creates a new instance of CourseBox

            Args:
                driver (WebDriver): the driver to use
                course (CourseBoxHTML Element): The HTML element representing the course

            Returns:
                new CourseBox

            Raises:
                None
        """

        self.course = course
        self.driver = driver

    def check(self, keywords):
        """ Checks the if the course name matches any keyword

            Args:
                keywords (String Array): List of keywords to match

            Returns:
                bool

            Raises:
                None
        """

        title = self.course.find_element_by_css_selector(CourseBox.TITLE).text
        print(title)
        for key in keywords:
            if key in title.lower().split():
                print("Course passed")
                return True

        return False

    def get(self):
        """ Adds the course to the list of courses on Udemy

            Returns:
                None

            Raises:
                None
        """

        self.course.find_element_by_css_selector(CourseBox.LINK).click()
        time.sleep(CourseBox.SLEEP)
        page = CoursePage(self.driver)
        page.focus()
        page.get()
        page.close()

class CoursePage:
    """ Class to represent the course page on udemy after clicking on the div

    Public Properties:
        driver (WebDriver): the driver to use

    Public Methods:
        focus (focus the driver on the course page)
        get (adds the course to the udemy account)
        close (closes the window)
    """

    BUY_BUTTON = "div.buy-box button.course-cta[data-purpose=\"buy-this-course-button\"]"

    def __init__(self, driver):
        """ Creates a new instance of CoursePage

            Args:
                driver (WebDriver): the driver to use

            Returns:
                new CoursePage

            Raises:
                None
        """

        self.driver = driver

    def focus(self):
        """ Sets the driver focus on the new page

            Returns:
                None

            Raises:
                None
        """

        self.driver.switch_to_window(self.driver.window_handles[1])

    def get(self):
        """ Adds the course to the udemy account

            Returns:
                None

            Raises:
                None
        """

        try:
            button = self.driver.find_element_by_css_selector(CoursePage.BUY_BUTTON)
            button.click()
            time.sleep(5)
        except Exception:
            print("Course already purchased")

    def close(self):
        """ Closes the current course page

            Returns:
                None

            Raises:
                None
        """

        self.driver.close()
