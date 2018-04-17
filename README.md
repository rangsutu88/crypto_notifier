# Crypto Notifier



A very basic Flask application that notifies on crypto currency price updates.
Notification updates are send to [IFTTT](https://ifttt.com) and [Telegram](https://telegram.org/).


### Setup

You will need to have [Python 3](https://www.python.org/download/releases/3.0/) configured, preferrably Python 3.6.+. Also,
have [virtualenv](https://virtualenv.pypa.io/en/stable/) setup in your environment or if you use [pipenv](https://docs.pipenv.org/).

Install dependencies

```bash
$ pip install -r requirements.txt
# if using pipenv
$ pipenv install
```

### Run tests

Tests have been configured to run with [pytest](https://docs.pytest.org/en/latest/).

```bash
$ python manage.py test
```
> This will run the tests in the [tests](./tests) directory.


[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)