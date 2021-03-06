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
from gpyclient.api.library_elements_api import LibraryElementsApi  # noqa: E501
from gpyclient.rest import ApiException


class TestLibraryElementsApi(unittest.TestCase):
    """LibraryElementsApi unit test stubs"""

    def setUp(self):
        self.api = gpyclient.api.library_elements_api.LibraryElementsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_library_element(self):
        """Test case for create_library_element

        Create library element.  # noqa: E501
        """
        pass

    def test_delete_library_element_by_uid(self):
        """Test case for delete_library_element_by_uid

        Delete library element.  # noqa: E501
        """
        pass

    def test_get_library_element_by_name(self):
        """Test case for get_library_element_by_name

        Get library element by name.  # noqa: E501
        """
        pass

    def test_get_library_element_by_uid(self):
        """Test case for get_library_element_by_uid

        Get library element by UID.  # noqa: E501
        """
        pass

    def test_get_library_element_connections(self):
        """Test case for get_library_element_connections

        Get library element connections.  # noqa: E501
        """
        pass

    def test_get_library_elements(self):
        """Test case for get_library_elements

        Get all library elements.  # noqa: E501
        """
        pass

    def test_update_library_element(self):
        """Test case for update_library_element

        Update library element.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
