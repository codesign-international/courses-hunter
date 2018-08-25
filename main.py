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

confpath = "config.ini"
keyspath = "keywords.txt"
driverpath = "drivers/geckodriver"

class NoParser(Exception):
    """

    """

    pass


class Config:
    """

    """

    def __init__(self):
        """

        """

        self.parser = ConfigParser()

    def parse(self, config):
        """

        """

        if config is None:
            self.parser = None
            return

        self.parser.read(config)

    def pages(self, pages):
        """

        """

        try:
            if self.parser is None:
                raise NoParser()

            return int(self.parser["Bot"]["pages"])
        except Exception:
            return int(pages)

    def keywords(self, keywords):
        """

        """

        try:
            if self.parser is None:
                raise NoParser()

            return str(self.parser["Bot"]["keywords"])
        except Exception:
            return str(keywords)

    def driver(self, driver):
        """

        """

        try:
            if self.parser is None:
                raise NoParser()

            return str(self.parser["Bot"]["driver"])
        except Exception:
            return str(driver)

    def account(self):
        """

        """

        return (self.parser["Account"]["user"], self.parser["Account"]["password"])

def parse(parser, pages, keywords, driverpath):
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
