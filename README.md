# stopspam

Version 0.4

A Python libary to check ip addresses, usernames and email address for their potential as spam against the stopforumspam ([http://stopforumspam.com](http://stopforumspam.com)) database.


## Installation
=

* Install via pip:

```bash
pip install stopspam
```

* Use it in your app:

```python
import stopspam
stopspam.check('testuser')
>>> True
```

Simple!

## Docs
=

### check(item)
Check to see if an item is in the spam database

Requirements:

* item - string. Examples: '192.168.0.1', 'hello@phalt.co', 'phalt'

Returns:

* Boolean, True if item is present in spam database.


example:
```python
import stopspam

stopspam.check('127.0.0.1')
>>> True
```

###confidence(item)
Returns the likelyhood of an item being spam

Requirements:

* item - string. Examples: '192.168.0.1', 'hello@phalt.co', 'phalt'

Returns:
* float - representing likelyhood (out of 100) that item is spam.


example:
```python
import stopspam

stopspam.confidence('hello@test.com')
>>> 99.0
```

###raw(item, format)
Returns a raw request from the stopforumspam database

Requirements:

* item - string. Examples:  '192.168.0.1', 'hello@phalt.co', 'phalt'
* format - string. Must be 'json' or 'xml'

Returns:
* string - JSON or XML formatted.

example:
```python
import stopspam

stopspam.raw('127.0.0.1', 'json')
>>>{"success":1,"ip":{"frequency":0,"appears":0}}
'''

###batch(list)
Check a list of items against the stopforumspam database.

Requirements:

* list - a list of strings

Returns:

* a dictionary of {'string' : boolean} for each item fed

example:
```python
import stopspam

items = ['127.0.0.1', '192.168.0.1']
stopspam.batch(items)
>>>{'127.0.0.1': 'True', '192.168.0.1': 'False'}

## Tests
=

The application works and all tests pass.
In order to check the tests in this version, download this repo and run:
```bash
python tests.py
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
