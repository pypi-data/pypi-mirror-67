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

import unittest
from unittest.mock import MagicMock
from hqlib import metric, domain, metric_source


class UnusedCIJobsTests(unittest.TestCase):
    """ Unit tests for the unused CI builds metric. """

    expected_report = '1 van de 2 actieve CI-builds is ongebruikt.'

    def setUp(self):
        """ Create the text fixture. """
        self._jenkins = MagicMock()
        self._project = domain.Project(metric_sources={metric_source.CIServer: self._jenkins},
                                       metric_source_ids={self._jenkins: "dummy"})
        self._metric = metric.UnusedCIJobs(subject=self._project, project=self._project)

    def test_norm_template_default_values(self):
        """ Test that the right values are returned to fill in the norm template. """
        self.assertTrue(metric.UnusedCIJobs.norm_template % metric.UnusedCIJobs.norm_template_default_values())

    def test_value(self):
        """ Test that the value equals the number of failing builds. """
        self._jenkins.number_of_unused_jobs.return_value = 1
        self.assertEqual(1, self._metric.value())

    def test_report(self):
        """ Test the metric report. """
        self._jenkins.number_of_unused_jobs.return_value = 1
        self._jenkins.number_of_active_jobs.return_value = 2
        self.assertEqual(self.expected_report, self._metric.report())

    def test_label(self):
        """ Test that the label to use in the HTML report is correct. """
        self.assertEqual('Ongebruikte builds', self._metric.url_label_text)

    def test_extra_info_urls(self):
        """ Test that the metric source method is called. """
        self._jenkins.unused_jobs_url.return_value = [('1', '2', '3')]

        result = self._metric.extra_info_rows()

        self.assertEqual([('1', '2', '3')], result)
        self._jenkins.unused_jobs_url.assert_called_once()
