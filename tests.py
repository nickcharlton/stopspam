import stopspam
import unittest
import simplejson as json
import xml.etree.ElementTree as xml
from test import test_support


class TestStopSpam(unittest.TestCase):

    def setUp(self):
        #  The most common spamming ip address, username and email
        self.bad_ip = '212.59.28.8'
        self.bad_username = 'crvenkapica'
        self.bad_email = 'crvenkapica@serphawk.com'
        self.json = 'json'
        self.xml = 'xml'
        #  Hopefully the most good ip address, username and email
        self.good_ip = '127.0.0.1'
        self.good_username = 'paulhallett'
        self.good_email = 'hello@phalt.co'

    def test_check_ip_json(self):
        '''
        Assert that we can check for ip and get json data back
        '''
        results = stopspam.check_ip(self.bad_ip, self.json)
        results = json.loads(results)
        self.assertEquals(results['success'], 1)

    def test_check_ip_xml(self):
        results = stopspam.check_ip(self.bad_ip, self.xml)
        results = xml.fromstring(results)
        test = results.attrib
        self.assertEquals(test['success'], 'true')

    def test_check_username_json(self):
        results = stopspam.check_username(self.bad_username, self.json)
        results = json.loads(results)
        self.assertEquals(results['success'], 1)

    def test_check_username_xml(self):
        results = stopspam.check_username(self.bad_username, self.xml)
        results = xml.fromstring(results)
        test = results.attrib
        self.assertEquals(test['success'], 'true')

    def test_check_email_json(self):
        results = stopspam.check_email(self.bad_email, self.json)
        results = json.loads(results)
        self.assertEquals(results['success'], 1)

    def test_check_email_xml(self):
        results = stopspam.check_email(self.bad_email, self.xml)
        results = xml.fromstring(results)
        test = results.attrib
        self.assertEquals(test['success'], 'true')

    def test_ip_confidence_bad(self):
        self.assertNotEqual(stopspam.check_ip_confidence(self.bad_ip), 0)

    def test_ip_confidence_good(self):
        self.assertEqual(stopspam.check_ip_confidence(self.good_ip), 0)

    def test_username_confidence_bad(self):
        self.assertNotEqual(stopspam.check_username_confidence(self.bad_username), 0)

    def test_username_confidence_good(self):
        self.assertEqual(stopspam.check_username_confidence(self.good_username), 0)

    def test_email_confidence_bad(self):
        self.assertNotEqual(stopspam.check_email_confidence(self.bad_email), 0)

    def test_email_confidence_good(self):
        self.assertEqual(stopspam.check_email_confidence(self.good_email), 0)


def test_main():
    test_support.run_unittest(TestStopSpam)

if __name__ == '__main__':
    test_main()
