# stopspam
=

Version 0.2

A Python app to check ip addresses, usernames and email address for their potential as spam, using the stopforumspam ([http://stopforumspam.com](http://stopforumspam.com)) database.

This application was built because I couldn't find anything simple that worked as a library as well as a terminal application.

This is great for use in a Django, flask or web.py application!

## Installation
=

* Download from github:

```bash
git clone https://github.com/phalt/stopspam.git
```

* Make sure you have the requirements:

```bash
pip install -r requirements.txt
```
This will install [requests](http://docs.python-requests.org), a required app.

* Add it to your app:

```python
import stopspam
```

Simple!

## Tests
=

The application works and all tests pass.
In order to check the tests run:
```bash
python tests.py
```

# Termnial usage
=

stopspam can be used in the terminal.

Examples:

```bash
python stopspam.py -ip=127.0.0.1

python stopspam.py -email=hello@test.com

python stopspam.py -username=phalt
```

These will all produce a single line print out:

```bash
127.0.0.1 is probably not spam
```

or

```bash
ztest@test.com IS SPAM with a confidence of 99.87%
```

## API usage
=

stopspam can also be used in your Python projects.
Here is a list of api calls and examples that you can use.

#### check_ip(ip, format)
Check an ip address is spam

Requirements:

* ip - string
* format - string ('json' or 'xml')


example:
```python
import stopspam
import json

result = stopspam.check_ip('127.0.0.1','json')
data = json.loads(result)
```

#### check_email(email, format)
Check an email address is spam

Requirements:

* email - string
* format - string ('json' or 'xml')


example:
```python
import stopspam
import json

result = stopspam.check_email('hello@test.com','json')
data = json.loads(result)
```

#### check_username(username, format)
Check a username is spam

Requirements:

* username - string
* format - string ('json' or 'xml')


example:
```python
import stopspam
import json

result = stopspam.check_username('badaccount','json')
data = json.loads(result)
```

#### check_ip_confidence(ip)
Returns the confidence level that an ip is spam

Requirements:

* ip - string

Returns:
* float


example:
```python
import stopspam

result = stopspam.check_ip_confidence('127.0.0.1')

print result
>>> 95.68
```

#### check_email_confidence(email)
Returns the confidence level that an email is spam

Requirements:

* email - string

Returns:
* float


example:
```python
import stopspam

result = stopspam.check_email_confidence('test@helloc.om')

print result
>>> 99.0
```

#### check_username_confidence(email)
Returns the confidence level that an username is spam

Requirements:

* username - string

Returns:
* float


example:
```python
import stopspam

result = stopspam.check_username_confidence('testuser')

print result
>>> 97.0
```

# Legal stuff
==

Copyright (c) Paul Hallett 2013

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
