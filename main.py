import plac
from selenium import webdriver
from src.udemy import Udemy

import configparser
from config import UDEMY, COUPONS, Config

@plac.annotations(
    pages=plac.Annotation("Number of pages to scan", "option"),
    keywords=plac.Annotation("Path to the keywords file", "option"),
    driverpath=plac.Annotation("Path to the web driver", "option"),
    config=plac.Annotation("Path to the config file", "option")
)
def main(pages, keywords, driverpath, config=".config/config.ini"):
    try:
        options = Config(config, pages, keywords, driverpath)
    except configparser.Error:
        print("Impossible to parse the config file")
        exit(1)
    except KeyError:
        print("Invalid configuration file")
        exit(1)

    try:
        keys = list(options.keywords())
    except (IOError, FileNotFoundError):
        print("Impossible to open keywords file")
        exit(1)

    driver = webdriver.Firefox(executable_path=options.driver)
    driver.implicitly_wait(2)

    udemy = Udemy(driver, keys)
    udemy.login(UDEMY, options.user, options.password)
    udemy.extract(COUPONS, options.pages)
    driver.close()

if __name__ == "__main__":
    plac.call(main, version="0.2.0")
