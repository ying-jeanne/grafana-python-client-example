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
from gpyclient.api.dashboard_versions_api import DashboardVersionsApi  # noqa: E501
from gpyclient.rest import ApiException


class TestDashboardVersionsApi(unittest.TestCase):
    """DashboardVersionsApi unit test stubs"""

    def setUp(self):
        self.api = gpyclient.api.dashboard_versions_api.DashboardVersionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_dashboard_version(self):
        """Test case for get_dashboard_version

        Get a specific dashboard version.  # noqa: E501
        """
        pass

    def test_get_dashboard_version_by_uid(self):
        """Test case for get_dashboard_version_by_uid

        Get a specific dashboard version using UID.  # noqa: E501
        """
        pass

    def test_get_dashboard_versions(self):
        """Test case for get_dashboard_versions

        Gets all existing versions for the dashboard.  # noqa: E501
        """
        pass

    def test_get_dashboard_versions_by_uid(self):
        """Test case for get_dashboard_versions_by_uid

        Gets all existing versions for the dashboard using UID.  # noqa: E501
        """
        pass

    def test_restore_dashboard_version(self):
        """Test case for restore_dashboard_version

        Restore a dashboard to a given dashboard version.  # noqa: E501
        """
        pass

    def test_restore_dashboard_version_by_uid(self):
        """Test case for restore_dashboard_version_by_uid

        Restore a dashboard to a given dashboard version using UID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
