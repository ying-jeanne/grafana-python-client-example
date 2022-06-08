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
from gpyclient.api.users_api import UsersApi  # noqa: E501
from gpyclient.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = gpyclient.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user_by_id(self):
        """Test case for get_user_by_id

        Get user by id.  # noqa: E501
        """
        pass

    def test_get_user_by_login_or_email(self):
        """Test case for get_user_by_login_or_email

        Get user by login or email.  # noqa: E501
        """
        pass

    def test_get_user_org_list(self):
        """Test case for get_user_org_list

        Get organizations for user.  # noqa: E501
        """
        pass

    def test_get_user_teams(self):
        """Test case for get_user_teams

        Get teams for user.  # noqa: E501
        """
        pass

    def test_search_users(self):
        """Test case for search_users

        Get users.  # noqa: E501
        """
        pass

    def test_search_users_with_paging(self):
        """Test case for search_users_with_paging

        Get users with paging.  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()