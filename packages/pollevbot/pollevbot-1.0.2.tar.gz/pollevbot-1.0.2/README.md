# pollevbot

pollevbot is a bot that automatically responds to polls at [pollev.com](https://pollev.com/). It continually checks if a specified poll user has opened any polls. Once a poll has been opened, the bot submits a random response. 

Requires Python 3.7 or later.
## Dependencies

[Requests](https://pypi.org/project/requests/), [BeautifulSoup](https://pypi.org/project/beautifulsoup4/). 

[APScheduler](https://pypi.org/project/APScheduler/) if you'd like to deploy to Heroku.

## Usage

First, clone this repo:
```bash
git clone https://github.com/danielqiang/pollevbot.git
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Set your username, password, and desired poll host in [main.py](pollevbot/main.py):
```python
user = 'My Username'
password = 'My Password'
host = 'PollEverywhere URL Extension e.g. "uwpsych"'
```

And run the script.

## Deploying to Heroku



## Disclaimer

I do not promote or condone the usage of this script for any kind of academic misconduct or dishonesty. I wrote this script for the sole purpose of educating myself on cybersecurity and web protocols, and cannot be held liable for any indirect, incidental, consequential, special, or exemplary damages arising out of or in connection with the usage of this script.
