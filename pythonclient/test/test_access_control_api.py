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
from pythonclient.api.access_control_api import AccessControlApi  # noqa: E501
from pythonclient.rest import ApiException


class TestAccessControlApi(unittest.TestCase):
    """AccessControlApi unit test stubs"""

    def setUp(self):
        self.api = pythonclient.api.access_control_api.AccessControlApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_builtin_role(self):
        """Test case for add_builtin_role

        Create a built-in role assignment.  # noqa: E501
        """
        pass

    def test_add_team_role(self):
        """Test case for add_team_role

        Add team role.  # noqa: E501
        """
        pass

    def test_add_user_role(self):
        """Test case for add_user_role

        Add a user role assignment.  # noqa: E501
        """
        pass

    def test_create_role_with_permissions(self):
        """Test case for create_role_with_permissions

        Create a new custom role.  # noqa: E501
        """
        pass

    def test_delete_custom_role(self):
        """Test case for delete_custom_role

        Delete a custom role.  # noqa: E501
        """
        pass

    def test_get_access_control_status(self):
        """Test case for get_access_control_status

        Get status.  # noqa: E501
        """
        pass

    def test_get_all_roles(self):
        """Test case for get_all_roles

        Get all roles.  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Get a role.  # noqa: E501
        """
        pass

    def test_list_builtin_roles(self):
        """Test case for list_builtin_roles

        Get all built-in role assignments.  # noqa: E501
        """
        pass

    def test_list_team_roles(self):
        """Test case for list_team_roles

        Get team roles.  # noqa: E501
        """
        pass

    def test_list_user_roles(self):
        """Test case for list_user_roles

        List roles assigned to a user.  # noqa: E501
        """
        pass

    def test_remove_builtin_role(self):
        """Test case for remove_builtin_role

        Remove a built-in role assignment.  # noqa: E501
        """
        pass

    def test_remove_team_role(self):
        """Test case for remove_team_role

        Remove team role.  # noqa: E501
        """
        pass

    def test_remove_user_role(self):
        """Test case for remove_user_role

        Remove a user role assignment.  # noqa: E501
        """
        pass

    def test_set_team_roles(self):
        """Test case for set_team_roles

        Update team role.  # noqa: E501
        """
        pass

    def test_set_user_roles(self):
        """Test case for set_user_roles

        Set user role assignments.  # noqa: E501
        """
        pass

    def test_update_role_with_permissions(self):
        """Test case for update_role_with_permissions

        Update a custom role.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
