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
from gpyclient.api.sync_team_groups_api import SyncTeamGroupsApi  # noqa: E501
from gpyclient.rest import ApiException


class TestSyncTeamGroupsApi(unittest.TestCase):
    """SyncTeamGroupsApi unit test stubs"""

    def setUp(self):
        self.api = gpyclient.api.sync_team_groups_api.SyncTeamGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_team_group_api(self):
        """Test case for add_team_group_api

        Add External Group.  # noqa: E501
        """
        pass

    def test_get_team_groups_api(self):
        """Test case for get_team_groups_api

        Get External Groups.  # noqa: E501
        """
        pass

    def test_remove_team_group_api(self):
        """Test case for remove_team_group_api

        Remove External Group.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
