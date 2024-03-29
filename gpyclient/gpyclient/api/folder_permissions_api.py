# coding: utf-8

"""
    Grafana HTTP API.

    The Grafana backend exposes an HTTP API, the same API is used by the frontend to do everything from saving dashboards, creating users and updating data sources.  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: hello@grafana.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gpyclient.api_client import ApiClient


class FolderPermissionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_folder_permissions(self, folder_uid, **kwargs):  # noqa: E501
        """Gets all existing permissions for the folder with the given `uid`.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_folder_permissions(folder_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_uid: (required)
        :return: list[DashboardAclInfoDTOModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_folder_permissions_with_http_info(folder_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_folder_permissions_with_http_info(folder_uid, **kwargs)  # noqa: E501
            return data

    def get_folder_permissions_with_http_info(self, folder_uid, **kwargs):  # noqa: E501
        """Gets all existing permissions for the folder with the given `uid`.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_folder_permissions_with_http_info(folder_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_uid: (required)
        :return: list[DashboardAclInfoDTOModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_folder_permissions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_uid' is set
        if self.api_client.client_side_validation and ('folder_uid' not in params or
                                                       params['folder_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folder_uid` when calling `get_folder_permissions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_uid' in params:
            path_params['folder_uid'] = params['folder_uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/folders/{folder_uid}/permissions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DashboardAclInfoDTOModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_folder_permissions(self, body, folder_uid, **kwargs):  # noqa: E501
        """Updates permissions for a folder. This operation will remove existing permissions if they’re not included in the request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_folder_permissions(body, folder_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateDashboardAclCommandModel body: (required)
        :param str folder_uid: (required)
        :return: SuccessResponseBodyModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_folder_permissions_with_http_info(body, folder_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_folder_permissions_with_http_info(body, folder_uid, **kwargs)  # noqa: E501
            return data

    def update_folder_permissions_with_http_info(self, body, folder_uid, **kwargs):  # noqa: E501
        """Updates permissions for a folder. This operation will remove existing permissions if they’re not included in the request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_folder_permissions_with_http_info(body, folder_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateDashboardAclCommandModel body: (required)
        :param str folder_uid: (required)
        :return: SuccessResponseBodyModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'folder_uid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_folder_permissions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `update_folder_permissions`")  # noqa: E501
        # verify the required parameter 'folder_uid' is set
        if self.api_client.client_side_validation and ('folder_uid' not in params or
                                                       params['folder_uid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folder_uid` when calling `update_folder_permissions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_uid' in params:
            path_params['folder_uid'] = params['folder_uid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'basic']  # noqa: E501

        return self.api_client.call_api(
            '/folders/{folder_uid}/permissions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponseBodyModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
