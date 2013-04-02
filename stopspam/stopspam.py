import urllib2 as requests  # Imagine what people will say when they see this
import json
import socket

VERSION = '0.4'
'''

stopspam.py

Created by Paul Hallett
http://phalt.co
hello@phalt.co

This is a simple spam prevention application that checks an ip, username or email
against the giant spam databases at http://stopforumspam.com

This application can be used in the terminal or as part of a larger application.

TERMINAL USE:
--------------

python stopspam.py --help

Will show a list of commands at any time

python stopspam.py -ip=IP OR -email=EMAIL OR -username=USERNAME

For example:

python stopspam.py -ip=127.0.0.1

Will return results on the above ip.

API USE:
--------

You can import this app into your own applications:

Check the README.md for a list of api calls.

Here is an example:

import stopspam
result = stopspam.check_ip('127.0.0.1', 'json')


Legal stuff
-----------

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
--------
'''


def version():
    return VERSION


def _request(url):
    r = requests.urlopen(url)
    try:
        if r.getcode() == 200:
            return r.read()
    except:
        return False


def _get_format(format):
    if 'json' in format:
        return '&f=json'
    elif 'xml' in format:
        return ''
    else:  # JSON by default
        return '&f=json'


def _get_type(item):
    try:  # Create a socket to the ip, if we can then it must be an ip!
        socket.inet_aton(item)
        i = 'ip'
    except socket.error:
        if '@' in item:
            i = 'email'
        else:
            i = 'username'
    return i


def _get_url(item):
    return 'http://stopforumspam.com/api?' + _get_type(item) + '='


def raw(item, format):
    return _request(_get_url(item) + item + _get_format(format))


def check(item):
    returned = _request(_get_url(item) + item + _get_format('json'))
    data = json.loads(returned)
    if data[_get_type(item)]['appears'] == 1:
        return True
    else:
        return False


def confidence(item):
    data = json.loads(raw(item, 'json'))
    if data[_get_type(item)]['appears'] == 1:
        return data[_get_type(item)]['confidence']
    else:
        return 0

if __name__ == "__main__":
    print 'Stopspam version ' + VERSION
    print 'Usage:\n    import stopspam\n    print stopspam.check(\'127.0.0.1\')\n    >>>True'
