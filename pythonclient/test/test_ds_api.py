# coding: utf-8

"""
    Grafana HTTP API.

    The Grafana backend exposes an HTTP API, the same API is used by the frontend to do everything from saving dashboards, creating users and updating data sources.  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: hello@grafana.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import pythonclient
from pythonclient.api.ds_api import DsApi  # noqa: E501
from pythonclient.rest import ApiException


class TestDsApi(unittest.TestCase):
    """DsApi unit test stubs"""

    def setUp(self):
        self.api = pythonclient.api.ds_api.DsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_query_metrics_with_expressions(self):
        """Test case for query_metrics_with_expressions

        Query metrics with expressions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
