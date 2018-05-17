
# username of the udemy account
USER_NAME = "username"

# username password of the udemy account
USER_PASS = "password"

# number of pages to search
PAGES = 5

def lines(path):
    for line in open(path):
        yield line.replace("\r\n", "").replace("\n", "")

# keywords to match
KEYWORDS = [line for line in lines("keywords.txt")]
