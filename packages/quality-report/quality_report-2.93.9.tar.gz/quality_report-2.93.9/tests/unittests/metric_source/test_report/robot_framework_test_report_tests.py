"""
Copyright 2012-2019 Ministerie van Sociale Zaken en Werkgelegenheid

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import datetime
import unittest
import urllib.error

from hqlib.metric_source import RobotFrameworkTestReport


class FakeUrlOpener(object):  # pylint: disable=too-few-public-methods
    """ Fake URL opener. """
    contents = ''

    def url_read(self, url):
        """ Return the html or raise an exception. """
        if 'raise' in url:
            raise urllib.error.HTTPError(None, None, None, None, None)
        else:
            return self.contents


class RobotFrameworkTestReportTest(unittest.TestCase):
    """ Unit tests for the Robot Framework test report class. """
    def setUp(self):
        self.__opener = FakeUrlOpener()
        self.__robot = RobotFrameworkTestReport(url_read=self.__opener.url_read)

    def test_test_report(self):
        """ Test retrieving a test report. """
        self.__opener.contents = '''
<robot generated="20171208 07:00:03.650" generator="Robot 3.0.2 (Python 2.7.13 on linux2)">
  <statistics>
    <total>
      <stat fail="0" pass="281">Critical Tests</stat>
      <stat fail="0" pass="281">All Tests</stat>
    </total>
  </statistics>
</robot>'''
        self.assertEqual(0, self.__robot.failed_tests('url'))
        self.assertEqual(281, self.__robot.passed_tests('url'))
        self.assertEqual(0, self.__robot.skipped_tests('url'))

    def test_http_error(self):
        """ Test that the default is returned when a HTTP error occurs. """
        self.assertEqual(-1, self.__robot.failed_tests('raise'))
        self.assertEqual(-1, self.__robot.passed_tests('raise'))
        self.assertEqual(0, self.__robot.skipped_tests('raise'))

    def test_missing_url(self):
        """ Test that the default is returned when no urls are provided. """
        self.assertEqual(-1, self.__robot.failed_tests())
        self.assertEqual(-1, self.__robot.passed_tests())
        self.assertEqual(-1, self.__robot.skipped_tests())
        self.assertEqual(datetime.datetime.min, self.__robot.datetime())

    def test_incomplete_xml(self):
        """ Test that the default is returned when the xml is incomplete. """
        self.__opener.contents = '<robot></robot>'
        self.assertEqual(-1, self.__robot.failed_tests('url'))

    def test_faulty_xml(self):
        """ Test incorrect XML. """
        self.__opener.contents = '<foo><bar>'
        self.assertEqual(-1, self.__robot.failed_tests('url'))

    def test_datetime_with_faulty_xml(self):
        """ Test incorrect XML. """
        self.__opener.contents = '<robot><suite></robot>'
        self.assertEqual(datetime.datetime.min, self.__robot.datetime('url'))

    def test_report_datetime(self):
        """ Test that the date and time of the test suite is returned. """
        self.__opener.contents = '<robot generated="20171208 07:00:03.650" ' \
                                 'generator="Robot 3.0.2 (Python 2.7.13 on linux2)"></robot>'
        self.assertEqual(datetime.datetime(2017, 12, 8, 7, 0, 3, 650000), self.__robot.datetime('url'))

    def test_missing_report_datetime(self):
        """ Test that the minimum datetime is returned if the url can't be opened. """
        self.assertEqual(datetime.datetime.min, self.__robot.datetime('raise'))

    def test_incomplete_xml_datetime(self):
        """ Test that the minimum datetime is returned when the xml is incomplete. """
        self.__opener.contents = '<robot></robot>'
        self.assertEqual(datetime.datetime.min, self.__robot.datetime('url'))

    def test_incomplete_xml_no_timestamp(self):
        """ Test that the minimum datetime is returned when the xml is incomplete. """
        self.__opener.contents = '<robot><suite></suite></robot>'
        self.assertEqual(datetime.datetime.min, self.__robot.datetime('url'))

    def test_urls(self):
        """ Test that the urls point to the HTML versions of the reports. """
        self.assertEqual(['http://server/robot/report.html'],
                         self.__robot.metric_source_urls('http://server/robot/output.xml'))
