import plac
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser
from src import SLEEP_REDO
from src.udemy import Udemy

def lines(path):
    for line in open(path):
        yield line.replace("\r\n", "").replace("\n", "")

confpath = "config/config.ini"
keyspath = "config/keywords.txt"
driverpath = "drivers/geckodriver"

class NoParser(Exception):
    """ This exception is thrown if the user tries to get a value from an unexistant parser
    """

    pass


class Config:
    """ Used to make the configuration for the bot

    Public properties:
        None

    Public methods:
        parse(Parses the config file)
        pages(Sets the number of pages to be scaned by the app)
        keywords(Sets the keywords path to be used by the app)
        driver(Sets the driverpath to be used by the app)
        account(Gets the account data from the config file)

    """

    def __init__(self):
        """ Create a new Config instance

        Returns:
            new Config

        Raises:
            None
        """

        self.parser = ConfigParser()

    def parse(self, config):
        """ Parses the config file

        Args:
            config (str or None): Path to the config file

        Returns:
            None

        Raises:
            None
        """

        if config is None:
            self.parser = None
            return

        self.parser.read(config)

    def pages(self, pages):
        """ Sets the number of pages to be scaned by the app

        This function controls if the option has been set in the config file,
        if not, it will return it's argument

        Args:
            pages (int or None): Number of pages to scan

        Returns:
            The number of pages to scan

        Raises:
            None
        """

        try:
            if self.parser is None:
                raise NoParser()

            return int(self.parser["Bot"]["pages"])
        except Exception:
            return int(pages)

    def keywords(self, keywords):
        """ Sets the keywords path to be used by the app

        This function controls if the option has been set in the config file,
        if not, it will return it's argument

        Args:
            keywords (str or None): Path to the keywords file

        Returns:
            The path to the keywords file

        Raises:
            None
        """

        try:
            if self.parser is None:
                raise NoParser()

            return str(self.parser["Bot"]["keywords"])
        except Exception:
            return str(keywords)

    def driver(self, driver):
        """ Sets the driverpath to be used by the app

        This function controls if the option has been set in the config file,
        if not, it will return it's argument

        Args:
            driver (str or None): Path to the driver file

        Returns:
            The path to the driver file

        Raises:
            None
        """

        try:
            if self.parser is None:
                raise NoParser()

            return str(self.parser["Bot"]["driver"])
        except Exception:
            return str(driver)

    def account(self):
        """ Gets the account data from the config file

        Returns:
            The user and password set on the config file

        Raises:
            None
        """

        return (self.parser["Account"]["user"], self.parser["Account"]["password"])

def parse(parser, pages, keywords, driverpath):
    """ Convenience function to parse the important command line elements

    Args:
        pages (int or None): The numer of pages to scan
        keywords (str or None): The path to the keywords file
        driverpath (str or None): The path to the driver file

    Returns:
        The pages, keywords and driverpath for the app

    Raises:
        None
    """

    pages = parser.pages(pages)
    keywords = parser.keywords(keywords)
    driverpath = parser.driver(driverpath)

    return (pages, keywords, driverpath)

@plac.annotations(
    config=plac.Annotation("Path to the config file", "option"),
    pages=plac.Annotation("Number of pages to scan", "option"),
    keywords=plac.Annotation("Path to the keywords file", "option"),
    driverpath=plac.Annotation("Path to the web driver", "option")
)
def main(config=confpath, pages=5, keywords=keyspath, driverpath=driverpath):
    parser = Config()
    parser.parse(config)
    pages, keywords, driverpath = parse(parser, pages, keywords, driverpath)
    user, password = parser.account()

    driver = webdriver.Firefox(executable_path=driverpath)
    driver.implicitly_wait(2)

    udemy = Udemy(driver, [line for line in lines(keywords)])
    udemy.login("https://udemy.com", user, password)
    udemy.extract(parser.parser["Bot"]["coupons"], pages)
    driver.close()

if __name__ == "__main__":
    plac.call(main, version="0.2.0")
