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

import gpyclient
from gpyclient.models.data_table_model import DataTableModel  # noqa: E501
from gpyclient.rest import ApiException


class TestDataTableModel(unittest.TestCase):
    """DataTableModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDataTableModel(self):
        """Test DataTableModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = gpyclient.models.data_table_model.DataTableModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
