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
from pythonclient.api.admin_api import AdminApi  # noqa: E501
from pythonclient.rest import ApiException


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = pythonclient.api.admin_api.AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_settings(self):
        """Test case for get_settings

        Fetch settings.  # noqa: E501
        """
        pass

    def test_get_stats(self):
        """Test case for get_stats

        Fetch Grafana Stats.  # noqa: E501
        """
        pass

    def test_pause_all_alerts(self):
        """Test case for pause_all_alerts

        Pause/unpause all (legacy) alerts.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()