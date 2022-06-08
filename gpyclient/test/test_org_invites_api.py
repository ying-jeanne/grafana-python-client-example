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
from gpyclient.api.org_invites_api import OrgInvitesApi  # noqa: E501
from gpyclient.rest import ApiException


class TestOrgInvitesApi(unittest.TestCase):
    """OrgInvitesApi unit test stubs"""

    def setUp(self):
        self.api = gpyclient.api.org_invites_api.OrgInvitesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_invite(self):
        """Test case for add_invite

        Add invite.  # noqa: E501
        """
        pass

    def test_get_invites(self):
        """Test case for get_invites

        Get pending invites.  # noqa: E501
        """
        pass

    def test_revoke_invite(self):
        """Test case for revoke_invite

        Revoke invite.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()