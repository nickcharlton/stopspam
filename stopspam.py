import sys
import urllib2 as requests
import json
import socket
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


def request(url):
    r = requests.urlopen(url)
    try:
        if r.getcode() == 200:
            return r.read()
    except:
        return False


def check_ip(ip, format):
    url = 'http://stopforumspam.com/api?ip='
    format = check_format(format)
    return request(url + ip + format)


def check_ip_confidence(ip):
    data = json.loads(check_ip(ip, 'json'))
    if data['ip']['appears'] == 1:
        return data['ip']['confidence']
    else:
        return 0


def check_username(username, format):
    url = 'http://stopforumspam.com/api?username='
    format = check_format(format)
    return request(url + username + format)


def check_username_confidence(username):
    data = json.loads(check_username(username, 'json'))
    if data['username']['appears'] == 1:
        return data['username']['confidence']
    else:
        return 0


def check_email(email, format):
    url = 'http://stopforumspam.com/api?email='
    format = check_format(format)
    return request(url + email + format)


def check_email_confidence(email):
    data = json.loads(check_email(email, 'json'))
    if data['email']['appears'] == 1:
        return data['email']['confidence']
    else:
        return 0


def check_format(format):
    if 'json' in format:
        return '&f=json'
    if 'xml' in format:
        return ''


# Takes anything, returns True or False if likely to be spam.
def is_spam(item):
    format = check_format('json')
    try:
        socket.inet_aton(item)
        d = check_ip(item, format)
        i = 'ip'
        print 'ip'
    except socket.error:  # Not an IP address
        if '@' in item:  # Probably an email
            d = check_email(item, format)
            i = 'email'
        else:
            d = check_username(item, format)
            i = 'username'

    data = json.loads(d)
    if data[i]['appears'] == 1:
        return True
    else:
        return False


def check_param(param):
    if '-ip=' in param:
        return {'ip': param.replace('-ip=', '')}
    if '-email=' in param:
        return {'email': param.replace('-email=', '')}
    if '-username=' in param:
        return {'username': param.replace('-username=', '')}
    else:
        return False


def terminal_check_ip(ip):
    data = json.loads(check_ip(ip, 'json'))
    if data['ip']['appears'] == 1:
        results = ip + ' IS SPAM '
        results += 'with a confidence of ' + str(data['ip']['confidence']) + '%'
    else:
        results = ip + ' is probably not spam'

    return results


def terminal_check_email(email):
    data = json.loads(check_email(email, 'json'))
    if data['email']['appears'] == 1:
        results = email + ' IS SPAM '
        results += 'with a confidence of ' + str(data['email']['confidence']) + '%'
    else:
        results = email + ' is probably not spam'

    return results


def terminal_check_username(username):
    data = json.loads(check_username(username, 'json'))
    if data['username']['appears'] == 1:
        results = username + ' IS SPAM '
        results += 'with a confidence of ' + str(data['username']['confidence']) + '%'
    else:
        results = username + ' is probably not spam'

    return results


def print_help():
    print '\nTerminal usage'
    print '----------------\n'
    print 'python stopspam.py -ip=IP or -email=EMAIL or -username=USERNAME'
    print '\nFor example:'
    print 'python stomspam.py -ip=212.59.28.8'
    print '\nThis will return:'
    print '212.59.28.8 IS SPAM with a confidence of 99.85%'


if __name__ == "__main__":

    try:
        i_param = sys.argv[1]
        param = check_param(i_param)

        if i_param == '--help':
            print_help()
        if '-ip=' in i_param:
            print terminal_check_ip(param['ip'])
        elif '-email=' in i_param:
            print terminal_check_email(param['email'])
        elif '-username=' in i_param:
            print terminal_check_username(param['username'])
        else:
            print 'Incorrect parameters supplied, type --help for help'

    except:
        print '\nNo parameters supplied, type stopspam.py --help for help'
