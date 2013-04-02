import stopspam
import unittest
import json
import xml.etree.ElementTree as xml
from test import test_support


class TestStopSpam(unittest.TestCase):

    def setUp(self):
        #  The most common spamming ip address, username and email
        self.bad_ip = '212.59.28.8'
        self.bad_username = 'crvenkapica'
        self.bad_email = 'crvenkapica@serphawk.com'
        #  Hopefully the most good ip address, username and email
        self.good_ip = '127.0.0.1'
        self.good_username = 'paulhallett'
        self.good_email = 'hello@phalt.co'

        def test_good_check_ip(self):
            self.assertFalse(stopspam.check(self.good_ip))

        def test_good_check_email(self):
            self.assertFalse(stopspam.check(self.good_email))

        def test_good_check_user(self):
            self.assertFalse(stopspam.check(self.good_username))

        def test_bad_check_ip(self):
            self.assertTrue(stopspam.check(self.bad_ip))

        def test_bad_check_email(self):
            self.assertTrue(stopspam.check(self.bad_email))

        def test_bad_check_user(self):
            self.assertTrue(stopspam.check(self.bad_username))

        def test_good_confidence_ip(self):
            self.assertEquals(stopspam.confidence(self.good_ip), 0)

        def test_good_confidence_email(self):
            self.assertEquals(stopspam.confidence(self.good_email), 0)

        def test_good_confidence_user(self):
            self.assertEquals(stopspam.confidence(self.good_username), 0)

        def test_bad_confidence_ip(self):
            self.assertNotEqual(stopspam.confidence(self.bad_ip), 0)

        def test_bad_confidence_email(self):
            self.assertNotEqual(stopspam.confidence(self.bad_email), 0)

        def test_bad_confidence_user(self):
            self.assertNotEqual(stopspam.confidence(self.bad_username), 0)

        def test_raw_json(self):
            data = stopspam.raw(self.bad_ip, 'json')
            try:
                data_j = json.loads(data)
            except:
                data_j = 'not json'
            self.assertEquals(data_j['success'], 1)

        def test_raw_xml(self):
            data = stopspam.raw(self.bad_ip, 'xml')
            try:
                data_x = xml.fromstring(data)
            except:
                data_x = 'not xml'
            self.assertEquals(data_x['success'], 'true')

        def test_batch(self):
            items = [self.bad_ip, self.bad_email, self.bad_username]
            results = stopspam.batch(items)
            self.assertTrue(results[self.bad_ip])


def test_main():
    test_support.run_unittest(TestStopSpam)

if __name__ == '__main__':
    test_main()
