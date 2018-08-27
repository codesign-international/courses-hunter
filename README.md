# Courses hunter

This is a bot that searches and applies automatically for free course coupons in udemy.
In order to do it, it searches on known websites that offer coupons for udemy courses and
applies for them if the course matches the search criteria.

## Getting Started

### Prerequisites

In order to use this bot you need to have:

- An udemy account
- Firefox browser installed
- Python 3.5.2 or later installed
- Python virtualenv (Optional, for installing everything in a virtualenv)

### Installing

The preferred way to use the bot is in a python virtual enviroment. To install in a virtual
enviroment run:

```bash
virtualenv ./
source bin/activate
pip install -U selenium
pip install -U plac
```

The next step is to get the driver needed to communicate with firefox. The driver can be
downloaded from [here](https://github.com/mozilla/geckodriver/releases). Make sure to select
the proper driver for your OS. Once you have downloaded the driver put it on
${workspaceRoot}/drivers/geckodriver.

## Usage

Right now, you have to specify the parameters needed for the bot to work on
${workspaceRoot}/.config/config.ini. After that put on the ${workspaceRoot}/.config/keywords.txt
file the list of keywords you wish to match the course against.

To launch the bot simply run in your terminal:

```bash
source bin/activate
python main.py
```

Setting specific bot-execution options is also allowed, here is the current list:

```bash
usage: main.py [-h] [-pages PAGES] [-keywords KEYWORDS]
               [-driverpath DRIVERPATH] [-config .config/config.ini]
               [--version]

optional arguments:
  -h, --help            show this help message and exit
  -pages PAGES          Number of pages to scan
  -keywords KEYWORDS    Path to the keywords file
  -driverpath DRIVERPATH
                        Path to the web driver
  -config .config/config.ini
                        Path to the config file
  --version, -v         show program's version number and exit
```

## Authors

- **Gabriel Dos Ramos** - *Initial Work and Maintainer* - [gabo01](https:://github.com/gabo01)

See also the list of [contributors](https://github.com/codesign-international/courses-hunter)
who participated in this project.

## License

This is project is licensed under the MIT license, see [LICENSE](LICENSE) for more details.