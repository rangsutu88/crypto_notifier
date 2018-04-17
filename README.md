# Crypto Notifier

[![CircleCI](https://circleci.com/gh/BrianLusina/crypto_notifier.svg?style=svg)](https://circleci.com/gh/BrianLusina/crypto_notifier)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c9e4016eaa614b0f9509008857435aaf)](https://www.codacy.com/app/BrianLusina/crypto_notifier?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BrianLusina/crypto_notifier&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/BrianLusina/crypto_notifier/branch/master/graph/badge.svg)](https://codecov.io/gh/BrianLusina/crypto_notifier)

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