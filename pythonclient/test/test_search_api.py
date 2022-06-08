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
from pythonclient.api.search_api import SearchApi  # noqa: E501
from pythonclient.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = pythonclient.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search(self):
        """Test case for search

        """
        pass

    def test_search_sorting(self):
        """Test case for search_sorting

        """
        pass


if __name__ == '__main__':
    unittest.main()
