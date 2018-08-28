import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from . import SLEEP_APPEAR, SLEEP_LONG
from .errors import Error, LoginNotFound
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

    SESSION = "#login-form"
    USER = "#login-form #form-item-email input"
    PASSWORD = "#login-form input#id_password"
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
            NoSuchElementException if the element is not found
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

    LOG_IN = "button[data-purpose=header-login]"

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
            LoginNotFound if any of the css calls fails
        """

        self.driver.get(address)

        try:
            logbutton = self.driver.find_element_by_css_selector(Udemy.LOG_IN)
        except NoSuchElementException:
            raise LoginNotFound("Unable to find login button DOM element")
        else:
            logbutton.click()

        try:
            WebDriverWait(self.driver, SLEEP_APPEAR).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, Session.SESSION))
            )
        except TimeoutException:
            raise LoginNotFound("Unable to find login form DOM element")

        try:
            self.__fill(user, password)
        except NoSuchElementException:
            raise LoginNotFound("Unable to find the form related DOM elements")

    def __fill(self, user, password):
        """ Fills the login form on udemy

            Args:
                user (str): the user to put
                password (str): the password to put

            Returns:
                None

            Raises:
                None
        """

        Session(self.driver, user, password).login()
        time.sleep(SLEEP_LONG)

    def extract(self, address, pages=None):
        """ Extracts all the coupons that match a keyword for the udemy account

        Args:
            address (String): the url to the coupons website
            pages (int): Number of pages to extract or None to avoid a limit

        Returns:
            None

        Raises:
            None
        """

        self.driver.get(address)
        Courses(self.driver, self.main, self.keywords).extract(pages)
