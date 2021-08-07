[![PyPi version](https://img.shields.io/pypi/v/transparentemail.svg)](https://pypi.org/project/transparentemail/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Downloads](https://pepy.tech/badge/transparentemail)](https://pepy.tech/project/transparentemail)
[![Downloads](https://img.shields.io/pypi/l/transparentemail.svg)](https://github.com/akash-codes93/TransparentEmail/LICENSE)

# Transparent Email

Transparent Email clears aliases from email address. Email `John.Doe+alias@gmail.com` will be transformed to `johndoe@gmail.com`.

**Inspired by** : [bkrukowski/transparent-email](https://github.com/bkrukowski/transparent-email) 

## Why?

To detect multi-accounts on your website.

## Supported mailboxes

* [gmail.com](https://gmail.com)
* [33mail.com](https://www.33mail.com)
* [outlook.com](http://outlook.com)
* [yahoo.com](http://mail.yahoo.com)

## Installation

```
pip install transparentemail
```

## Usage

```python
from transparentemail.src import get_primary_email
from transparentemail.services.Emails.emailException import InvalidEmailException

try:
    
    transformed_email = get_primary_email('John.Doe+alias@gmail.com')
    print(transformed_email)  # John.Doe@gmail.com

except InvalidEmailException:
    print('Invalid Email')
```


## Yahoo.com

Aliases work different on Yahoo than on Gmail. On Gmail part after plus is skipped.
For example message sent to `janedoe+alias@gmail.com` will be redirected to `janedoe@gmail.com`.

Yahoo uses the following pattern[*](https://help.yahoo.com/kb/SLN16026.html):

*baseName*-*keyword*@yahoo.com

* *baseName* - value defined by the user, different than email login;
* *keyword* - one from a list of keywords defined by the user.

Therefore we do not know what is the real email, so in this case result will be `baseName@yahoo.com`,
which actually does not exist.