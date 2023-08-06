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

import logging
import unittest
from unittest.mock import patch, call

from hqlib.metric_source import Jira, JiraFilter


class JiraFilterTest(unittest.TestCase):
    """ Test the Jira filter metric source. """

    def test_get_issue_url(self):
        """ Test Jira issue url formatting. """
        jira_filter = JiraFilter('url/', '', '')
        self.assertEqual('url/browse/key', jira_filter.get_issue_url('key'))

    @patch.object(Jira, 'get_query')
    def test_nr_issues(self, get_query_url_mock):
        """ Test that the number of items equals the sum of totals per metric source returned by Jira. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = \
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": [
                {"key": "ISS-1", "fields": {"summary": "First Issue", "customfield_11700": "20.3"}},
                {"key": "ISS-2", "fields": {"summary": "2nd Issue", "customfield_11700": 100}}]}

        result, issue_list = jira_filter.nr_issues('12345')

        get_query_url_mock.assert_called_once()
        self.assertEqual(5, result)  # pay attention, it reads 'total' and does not count the issues
        self.assertEqual([
            {"href": "http://jira/browse/ISS-1", "text": "First Issue"},
            {"href": "http://jira/browse/ISS-2", "text": "2nd Issue"}
        ], issue_list)

    @patch.object(Jira, 'get_query')
    def test_nr_issues_when_no_issues(self, get_query_url_mock):
        """ Test that the number of issues is zero and the issue list is empty when there is no issues. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = \
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "0", "issues": []}

        result, issue_list = jira_filter.nr_issues('12345')

        get_query_url_mock.assert_called_once()
        self.assertEqual(0, result)  # pay attention, it reads 'total' and does not count the issues
        self.assertEqual([], issue_list)

    @patch.object(Jira, 'get_query')
    def test_nr_issues_with_empty_jira_answer(self, get_query_url_mock):
        """ Test that the sum is -1 and the issue list is empty when jira returns empty json. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = []

        result, issue_list = jira_filter.nr_issues('12345')

        get_query_url_mock.assert_called_once()
        self.assertEqual(-1, result)
        self.assertEqual([], issue_list)

    @patch.object(JiraFilter, '_query_total')
    def test_nr_issues_multiple_sources(self, query_sum_mock):
        """ Test that the field is summed correctly and that involved issues are in the issue list. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        query_sum_mock.return_value = (0, ([]))

        jira_filter.nr_issues('12345', '78910')

        self.assertTrue(query_sum_mock.has_calls([call('12345'), call('78910')]))

    @patch.object(Jira, 'get_query')
    def test_issues_with_field_exceeding_value(self, get_query_url_mock):
        """ Test that the issues are returned correctly with their field values. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = \
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": [
                {"key": "ISS-1", "fields": {"summary": "First Issue", "customfield_11700": 20.3}},
                {"key": "ISS-2", "fields": {"summary": "2nd Issue", "customfield_11700": 100}},
                {"key": "ISS-3", "fields": {"summary": "The Last Issue", "customfield_11700": None}}]}

        issue_list = jira_filter.issues_with_field_exceeding_value('12345', limit_value=25)

        get_query_url_mock.assert_called_once()
        self.assertEqual([
            ("http://jira/browse/ISS-1", "First Issue", 20.3)
        ], issue_list)

    @patch.object(logging, 'error')
    @patch.object(Jira, 'get_query')
    def test_issues_with_field_exceeding_value_invalid(self, get_query_url_mock, mock_error):
        """ Test that the errors with issues having invalid data are logged. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = \
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": [
                {"key": "ISS-1", "fields": {"summary": "First Issue", "customfield_11700": 20.3}},
                {"key": "ISS-1", "fields": ''}]}

        issue_list = jira_filter.issues_with_field_exceeding_value('12345', limit_value=25)

        get_query_url_mock.assert_called_once()
        self.assertEqual([
            ("http://jira/browse/ISS-1", "First Issue", 20.3)
        ], issue_list)
        self.assertEqual("Error processing jira issues: %s.", mock_error.call_args_list[0][0][0])
        self.assertIsInstance(mock_error.call_args_list[0][0][1], AttributeError)

    @patch.object(logging, 'error')
    @patch.object(Jira, 'get_query')
    def test_issues_with_field_exceeding_value_invalid2(self, get_query_url_mock, mock_error):
        """ Test that the errors with issues having invalid data are logged. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = \
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": [
                {"key": "ISS-1", "no-fields": ''}]}

        issue_list = jira_filter.issues_with_field_exceeding_value('12345', limit_value=25)

        get_query_url_mock.assert_called_once()
        self.assertEqual([], issue_list)
        self.assertEqual("Error processing jira issues: %s.", mock_error.call_args_list[0][0][0])
        self.assertIsInstance(mock_error.call_args_list[0][0][1], KeyError)

    @patch.object(Jira, 'get_query')
    def test_issues_with_field_exceeding_value_2_sources(self, get_query_url_mock):
        """ Test that the issues are returned correctly with their field values. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.side_effect = [
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": [
                {"key": "ISS-1", "fields": {"summary": "First Issue", "customfield_11700": 20.3}}]},
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": [
                {"key": "ISS-11", "fields": {"summary": "Issue 11", "customfield_11700": 11}}]}]

        issue_list = jira_filter.issues_with_field_exceeding_value('12345', '22345', limit_value=25)

        self.assertTrue(get_query_url_mock.has_calls([call('12345'), call('22345')]))
        self.assertEqual([
            ("http://jira/browse/ISS-1", "First Issue", 20.3),
            ("http://jira/browse/ISS-11", "Issue 11", 11)
        ], issue_list)

    @patch.object(Jira, 'get_query')
    def test_issues_with_field_exceeding_value_date(self, get_query_url_mock):
        """ Test that the issues are returned correctly with their field values. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='duedate')
        get_query_url_mock.return_value = \
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": [
                {"key": "ISS-1",
                 "fields": {"summary": "First Issue", "custom": 20.3, "duedate": "2018-10-22T19:12:36.000+0100"}},
                {"key": "ISS-2",
                 "fields": {"summary": "2nd Issue", "custom": 100, "duedate": "2017-12-28T13:10:46.000+0100"}},
                {"key": "ISS-3", "fields": {"summary": "The Last Issue", "custom": 55, "duedate": None}}]}

        issue_list = jira_filter.issues_with_field_exceeding_value(
            '12345', limit_value="2018-03-22T19:12", extra_fields=['custom', 'non-existent-field'])

        get_query_url_mock.assert_called_once()
        self.assertEqual([
            ("http://jira/browse/ISS-2", "2nd Issue", "2017-12-28T13:10:46.000+0100", 100, None)
        ], issue_list)

    @patch.object(Jira, 'get_query')
    def test_issues_with_field(self, get_query_url_mock):
        """ Test that the issues are returned correctly with their field values. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = \
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": [
                {"key": "ISS-1", "fields": {"summary": "First Issue", "customfield_11700": "20.3"}},
                {"key": "ISS-2", "fields": {"summary": "2nd Issue", "customfield_11700": 100}},
                {"key": "ISS-3", "fields": {"summary": "The Last Issue", "customfield_11700": None}}]}

        issue_list = jira_filter.issues_with_field('12345')

        get_query_url_mock.assert_called_once()
        self.assertEqual([
            ({"href": "http://jira/browse/ISS-1", "text": "First Issue"}, 20.3),
            ({"href": "http://jira/browse/ISS-2", "text": "2nd Issue"}, 100.0)
        ], issue_list)

    @patch.object(Jira, 'get_query')
    def test_issues_with_field_without_issues(self, get_query_url_mock):
        """ Test that the issue list is empty when there are no issues. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = \
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": []}

        issue_list = jira_filter.issues_with_field('12345')

        get_query_url_mock.assert_called_once()
        self.assertEqual([], issue_list)

    @patch.object(logging, 'error')
    @patch.object(Jira, 'get_query')
    def test_issues_with_field_with_empty_jira_answer(self, get_query_url_mock, mock_error):
        """ Test that the issue list is empty when jira returns empty json. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = []

        issue_list = jira_filter.issues_with_field('12345')

        get_query_url_mock.assert_called_once()
        self.assertEqual([], issue_list)
        self.assertEqual("Couldn't get issues from Jira filter %s: %s.", mock_error.call_args_list[0][0][0])
        self.assertEqual("12345", mock_error.call_args_list[0][0][1])
        self.assertIsInstance(mock_error.call_args_list[0][0][2], TypeError)

    @patch.object(Jira, 'get_query')
    def test_nr_issues_with_field_empty(self, get_query_url_mock):
        """ Test that the number of items equals those without the value. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = \
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": [
                {"key": "ISS-1", "fields": {"summary": "First Issue", "customfield_11700": None}},
                {"key": "ISS-2", "fields": {"summary": "2nd Issue", "customfield_11700": 100}}]}

        result, issue_list = jira_filter.nr_issues_with_field_empty('12345')

        get_query_url_mock.assert_called_once()
        self.assertEqual(1, result)
        self.assertEqual([{"href": "http://jira/browse/ISS-1", "text": "First Issue"}], issue_list)

    @patch.object(Jira, 'get_query')
    def test_nr_issues_with_field_omitted(self, get_query_url_mock):
        """ Test that the number of items equals those that do not have specified field. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = \
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": [
                {"key": "ISS-1", "fields": {"summary": "First Issue"}},
                {"key": "ISS-2", "fields": {"summary": "2nd Issue", "customfield_11700": 100}}]}

        result, issue_list = jira_filter.nr_issues_with_field_empty('12345')

        get_query_url_mock.assert_called_once()
        self.assertEqual(1, result)
        self.assertEqual([{"href": "http://jira/browse/ISS-1", "text": "First Issue"}], issue_list)

    @patch.object(Jira, 'get_query')
    def test_nr_issues_with_field_empty_when_no_issues(self, get_query_url_mock):
        """ Test that the number of issues is zero and the issue list is empty when there is no issues. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = \
            {"searchUrl": "http://jira/search", "viewUrl": "http://jira/view", "total": "5", "issues": []}

        result, issue_list = jira_filter.nr_issues_with_field_empty('12345')

        get_query_url_mock.assert_called_once()
        self.assertEqual(0, result)
        self.assertEqual([], issue_list)

    @patch.object(Jira, 'get_query')
    def test_nr_issues_with_field_empty_and_empty_jira(self, get_query_url_mock):
        """ Test that the sum is -1 and the issue list is empty when jira returns empty json. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        get_query_url_mock.return_value = []

        result, issue_list = jira_filter.nr_issues_with_field_empty('12345')

        get_query_url_mock.assert_called_once()
        self.assertEqual(-1, result)
        self.assertEqual([], issue_list)

    @patch.object(JiraFilter, '_query_field_empty')
    def test_nr_issues_with_field_empty_multiple_sources(self, query_sum_mock):
        """ Test that the field is summed correctly and that involved issues are in the issue list. """
        jira_filter = JiraFilter('http://jira/', 'username', 'password', field_name='customfield_11700')
        query_sum_mock.return_value = (0, ([]))

        jira_filter.nr_issues_with_field_empty('12345', '78910')

        self.assertTrue(query_sum_mock.has_calls([call('12345'), call('78910')]))

    @patch.object(Jira, 'get_query_url')
    def test_url(self, get_query_url_mock):
        """ Test that the Jira filter returns the correct urls for the filters. """
        jira1 = 'http://jira1/view'
        jira2 = 'http://jira2/view'
        get_query_url_mock.side_effect = [jira1, jira2]

        result = JiraFilter('', '', '').metric_source_urls(123, 567)

        get_query_url_mock.assert_has_calls([call(123, search=False), call(567, search=False)])
        self.assertEqual([jira1, jira2], result)
