import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .courses import Courses

class Session:
    """ Class for handling the udemy login

    Public Properties:
        driver (WebDriver): the driver to use
        user (String): the user to put
        password (String): the password to put

    Public Methods:
        login (efectuates the login)
    """

    USER = "#login-form #id_email"
    PASSWORD = "#login-form #id_password"
    SUBMIT = "#login-form #submit-id-submit"

    def __init__(self, driver, user, password):
        """ Creates a new instance of Session

        Args:
            driver (WebDriver): the driver to use
            user (String): the udemy user
            password (String): the udemy password

        Returns:
            new Session

        Raises:
            None
        """

        self.driver = driver
        self.user = user
        self.password = password

    def login(self):
        """ Makes the login on udemy

        Returns:
            None

        Raises:
            None
        """

        user = self.driver.find_element_by_css_selector(Session.USER)
        user.clear()
        user.send_keys(self.user)
        password = self.driver.find_element_by_css_selector(Session.PASSWORD)
        password.clear()
        password.send_keys(self.password)
        submit = self.driver.find_element_by_css_selector(Session.SUBMIT)
        submit.click()

class Udemy:
    """ Base class for udemy related ops

    Public Properties:
        driver (WebDriver): the driver to use
        main (Window handle): The main window
        keywords (String Array): list of keywords to match

    Public Methods:
        login (efectuates the login on udemy url)
        extract (extracts the udemy coupons present on the url)
    """

    LOG_IN = "require-auth[data-purpose=header-login] a"

    def __init__(self, driver, keywords):
        """ Creates a new instance of Udemy

        Args:
            driver (WebDriver): the driver to use
            keywords (String Array): list of keywords to match

        Returns:
            new Udemy

        Raises:
            None
        """

        self.keywords = keywords
        self.driver = driver
        self.main = self.driver.current_window_handle

    def login(self, address, user, password):
        """ Makes the login on udemy

        Args:
            address (String): the udemy url
            user (String): the udemy user
            password (String): the udemy password

        Returns:
            None

        Raises:
            None
        """

        self.driver.get(address)
        self.driver.find_element_by_css_selector(Udemy.LOG_IN).click()
        time.sleep(1)
        self.fill_form(user, password)

    def fill_form(self, user, password):
        """ Fills the login form on udemy

            Args:
                user (String): the user to put
                password (String): the password to put

            Returns:
                None

            Raises:
                None
        """

        try:
            Session(self.driver, user, password).login()
            time.sleep(10)
        except Exception as e:
            print("Unable to login", e)
            exit(1)

    def extract(self, address, pages):
        """ Extracts all the coupons that match a keyword for the udemy account

        Args:
            address (String): the url to the coupons website
            pages (int): Number of pages to 

        Returns:
            None

        Raises:
            None
        """

        self.driver.get(address)
        time.sleep(5)
        Courses(self.driver, self.main, self.keywords).extract(pages)
