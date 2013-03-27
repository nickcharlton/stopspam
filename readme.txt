
Check if an ip address, username or email is likely to be spam.

Also allows you to check the confidence levels to get a finer grain determination.

Uses the api from stopforumspam.com

Installation is simple::

    pip install stopspam

and usage is even easier::

    import stopspam
    print stopspam.is_spam('testuser')
    >>> True

see https://github.com/phalt/stopspam for all documentation and usage.

This version has been tested on Python 2.7.