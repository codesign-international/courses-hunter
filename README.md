# Courses hunter

Bot that searchs and applies automatically to free courses in udemy

### Prerequisites

Firefox browser

python3

Udemy account

### Installing

On the project folder

```
virtualenv ./
pip install -U selenium
```

the geckodriver that must be put in $PROJECT/drivers/geckodriver

### Configuration

Update config.ini with the parameters for your udemy account
Update keywords.txt with the line-separated keywords to match against

### Usage

```
source bin/activate
python3 main.py
```
