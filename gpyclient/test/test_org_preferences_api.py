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
from gpyclient.api.org_preferences_api import OrgPreferencesApi  # noqa: E501
from gpyclient.rest import ApiException


class TestOrgPreferencesApi(unittest.TestCase):
    """OrgPreferencesApi unit test stubs"""

    def setUp(self):
        self.api = gpyclient.api.org_preferences_api.OrgPreferencesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_org_preferences(self):
        """Test case for get_org_preferences

        Get Current Org Prefs.  # noqa: E501
        """
        pass

    def test_patch_org_preferences(self):
        """Test case for patch_org_preferences

        Patch Current Org Prefs.  # noqa: E501
        """
        pass

    def test_update_org_preferences(self):
        """Test case for update_org_preferences

        Update Current Org Prefs.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
