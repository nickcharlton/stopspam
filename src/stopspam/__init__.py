import stopspam


def main():
    print 'hello world'


def is_spam(item):
    return stopspam.is_spam(item)


def check_ip(ip, format):
    return stopspam.check_ip(ip, format)


def check_email(email, format):
    return stopspam.check_email(email, format)


def check_username(username, format):
    return stopspam.check_username(username, format)


def check_ip_confidence(ip):
    return stopspam.check_ip_confidence(ip)


def check_email_confidence(email):
    return stopspam.check_email_confidence(email)


def check_username_confidence(username):
    return stopspam.check_username_confidence(username)
