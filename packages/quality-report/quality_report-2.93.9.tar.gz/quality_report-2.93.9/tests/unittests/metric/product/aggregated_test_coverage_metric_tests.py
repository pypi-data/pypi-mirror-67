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

from typing import Type

from hqlib import metric, domain, metric_source
from hqlib.metric.product.aggregated_test_coverage_metrics import AggregatedTestCoverage


class FakeNCover(domain.MetricSource):
    """ Fake NCover. """
    metric_source_name = metric_source.NCover.metric_source_name

    @staticmethod
    def statement_coverage(*args):  # pylint: disable=unused-argument
        """ Return the ART coverage. """
        return 98

    branch_coverage = statement_coverage

    @staticmethod
    def datetime(*args):  # pylint: disable=unused-argument
        """ Return a fake date. """
        return datetime.datetime.today() - datetime.timedelta(hours=95)


class FakeJaCoCo(FakeNCover):
    """ Fake JaCoCo. """
    metric_source_name = metric_source.JaCoCo.metric_source_name


class FakeSubject(object):
    """ Provide for a fake subject. """
    def __init__(self, art='', metric_source_ids=None):
        self.__art = art
        self.__metric_source_ids = metric_source_ids or dict()

    @staticmethod
    def name():
        """ Return the name of the subject. """
        return 'FakeSubject'

    def metric_source_id(self, the_metric_source):
        """ Return the id of the subject for the metric source. """
        return self.__metric_source_ids.get(the_metric_source)


class AggregatedTestStatementCoverageJacocoTest(unittest.TestCase):
    """ Unit tests for the aggregated coverage metric. """
    metric_class: Type[AggregatedTestCoverage] = metric.AggregatedTestStatementCoverage
    metric_source_class: Type[FakeNCover] = FakeJaCoCo
    metric_source_id: str = 'http://jacoco'

    def setUp(self):
        self.__coverage_report = self.metric_source_class()
        self.__subject = FakeSubject(metric_source_ids={self.__coverage_report: self.metric_source_id})
        self.__project = domain.Project(metric_sources={metric_source.AggregatedCoverageReport: self.__coverage_report})
        self.__metric = self.metric_class(subject=self.__subject, project=self.__project)

    def test_value(self):
        """ Test that value of the metric equals the coverage as reported by Jacoco. """
        self.assertEqual(self.__coverage_report.statement_coverage(None), self.__metric.value())

    def test_report(self):
        """ Test that the report is correct. """
        self.assertTrue(self.__metric.report().startswith(
            'FakeSubject geaggregeerde {0} coverage is 98%'.format(self.metric_class.covered_item)))

    def test_missing_id(self):
        """ Test that the value is -1 when the metric source id hasn't been configured. """
        subject = FakeSubject()
        coverage_metric = self.metric_class(subject=subject, project=self.__project)
        self.assertEqual(-1, coverage_metric.value())


class AggregatedTestBranchCoverageJacocoTest(AggregatedTestStatementCoverageJacocoTest):
    """ Unit tests for the aggregated test branch metric. """
    metric_class = metric.AggregatedTestBranchCoverage


class AggregatedTestStatementCoverageNCoverTest(AggregatedTestStatementCoverageJacocoTest):
    """ Unit tests for the aggregated test statement coverage metric. """
    metric_source_class = FakeNCover
    metric_source_id = 'http://ncover'


class AggregatedTestBranchCoverageNCoverTest(AggregatedTestStatementCoverageNCoverTest):
    """ Unit tests for the aggregated test branch coverage metric. """
    metric_class = metric.AggregatedTestBranchCoverage


class AggregatedTestCoverageReportAgeTest(unittest.TestCase):
    """ Unit tests for the aggregated test coverage report age metric. """
    def setUp(self):
        self.__coverage_report = FakeJaCoCo()
        self.__subject = FakeSubject(metric_source_ids={self.__coverage_report: 'http://jacoco'})
        self.__project = domain.Project(metric_sources={metric_source.AggregatedCoverageReport: self.__coverage_report})
        self.__metric = metric.AggregatedTestCoverageReportAge(subject=self.__subject, project=self.__project)

    def test_value(self):
        """ Test that the value is the age of the coverage report. """
        self.assertEqual(3, self.__metric.value())

    def test_missing_metric_source_id(self):
        """ Test that the value is -1 if the metric source id hasn't been configured. """
        age = metric.AggregatedTestCoverageReportAge(subject=FakeSubject(), project=self.__project)
        self.assertEqual(-1, age.value())
