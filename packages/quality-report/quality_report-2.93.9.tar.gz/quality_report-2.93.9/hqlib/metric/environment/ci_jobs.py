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
from typing import List
from hqlib import metric_source
from hqlib.domain import LowerIsBetterMetric
from hqlib.typing import MetricParameters


class CIJobs(LowerIsBetterMetric):
    """ Base class for FailingCIJobs and UnusedCIJobs. """

    metric_source_class = metric_source.CIServer

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def _parameters(self) -> MetricParameters:
        parameters = super()._parameters()
        parameters['number_of_jobs'] = str(self._metric_source.number_of_active_jobs()) if self._metric_source else '?'
        return parameters

    @staticmethod
    def convert_item_to_extra_info(item):
        """ Item arguments url, text, nr_of_inactive_days convey as a link and a number  """
        return ({"href": item[1], "text": item[0]}, item[2]) if item else None

    def _get_display_urls(self) -> List[str]:
        return ['dummy'] if self._metric_source.metric_source_name == 'GitLabCI' else []
