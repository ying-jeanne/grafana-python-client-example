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
from pythonclient.models.postable_user_config_model import PostableUserConfigModel  # noqa: E501
from pythonclient.rest import ApiException


class TestPostableUserConfigModel(unittest.TestCase):
    """PostableUserConfigModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPostableUserConfigModel(self):
        """Test PostableUserConfigModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = pythonclient.models.postable_user_config_model.PostableUserConfigModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
