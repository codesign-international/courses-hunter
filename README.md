# Courses hunter

Bot that searchs and applies automatically to free courses in udemy

### Prerequisites

Firefox browser

python3

Udemy account

### Installing

On the project folder

```term
virtualenv ./
Selenium: pip install -U selenium
```

the geckodriver that must be put in $PROJECT/drivers/geckodriver

### Configuration

On the config.py file add the username and password of your udemy account

Also add the number of pages you want the bot to search (a higher number will take more time but will let you execute
the bot less frequently

Additional to that, on the keywords.txt file add the keywords you want to search about (each keyword in a single line
and in lowercase)

### Usage

```term
source bin/activate (virtualenv)
python3 main.py
```
## Deployment

python3 main.py and wait for the bot to do the job
