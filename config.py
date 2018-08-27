from configparser import ConfigParser

UDEMY = "https://udemy.com"
COUPONS = "https://udemycoupon.learnviral.com/coupon-category/free100-discount/"

def lines(path):
    for line in open(path):
        yield line.replace("\r\n", "").replace("\n", "")

class Config:
    """ Used to make the configuration for the bot

    Public properties:
        driver (str): path to the driver file
        user (str): udemy account username
        password (str): udemy account password
        pages (int): Number of pages to scan

    Public methods:
        parse(Parses the config file)
        pages(Sets the number of pages to be scaned by the app)
        keywords(Sets the keywords path to be used by the app)
        driver(Sets the driverpath to be used by the app)
        account(Gets the account data from the config file)

    """

    def __init__(self, file, pages, keywords, driverpath):
        """ Create a new Config instance

        If the arg is defined then it will be prioritized, else
        the fallback value from the config file will be used or an error
        will be raised

        Args:
            file (str): Path to the config file
            pages (int or None): Number of pages to scan
            keywords (str or None): Path to the keywords file
            driverpath (str or None): Path to the driver

        Returns:
            new Config

        Raises:
            None
        """

        self.parser = ConfigParser()
        self.parser.read(file)
        
        self.user = self.parser["Account"]["user"]
        self.password = self.parser["Account"]["password"]

        if pages is None:
            self.pages = self.parser["Bot"]["pages"]
        else:
            self.pages = int(pages)

        if keywords is None:
            self.keys = self.parser["Bot"]["keywords"]
        else:
            self.keys = str(keywords)

        if driverpath is None:
            self.driver = self.parser["Bot"]["driver"]
        else:
            self.driver = str(driverpath)

    def keywords(self):
        """

        """

        return lines(self.keys)
