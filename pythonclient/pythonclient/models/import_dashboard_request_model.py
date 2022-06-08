# coding: utf-8

"""
    Grafana HTTP API.

    The Grafana backend exposes an HTTP API, the same API is used by the frontend to do everything from saving dashboards, creating users and updating data sources.  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: hello@grafana.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pythonclient.configuration import Configuration


class ImportDashboardRequestModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dashboard': 'JsonModel',
        'folder_id': 'int',
        'folder_uid': 'str',
        'inputs': 'list[ImportDashboardInputModel]',
        'overwrite': 'bool',
        'path': 'str',
        'plugin_id': 'str'
    }

    attribute_map = {
        'dashboard': 'dashboard',
        'folder_id': 'folderId',
        'folder_uid': 'folderUid',
        'inputs': 'inputs',
        'overwrite': 'overwrite',
        'path': 'path',
        'plugin_id': 'pluginId'
    }

    def __init__(self, dashboard=None, folder_id=None, folder_uid=None, inputs=None, overwrite=None, path=None, plugin_id=None, _configuration=None):  # noqa: E501
        """ImportDashboardRequestModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dashboard = None
        self._folder_id = None
        self._folder_uid = None
        self._inputs = None
        self._overwrite = None
        self._path = None
        self._plugin_id = None
        self.discriminator = None

        if dashboard is not None:
            self.dashboard = dashboard
        if folder_id is not None:
            self.folder_id = folder_id
        if folder_uid is not None:
            self.folder_uid = folder_uid
        if inputs is not None:
            self.inputs = inputs
        if overwrite is not None:
            self.overwrite = overwrite
        if path is not None:
            self.path = path
        if plugin_id is not None:
            self.plugin_id = plugin_id

    @property
    def dashboard(self):
        """Gets the dashboard of this ImportDashboardRequestModel.  # noqa: E501


        :return: The dashboard of this ImportDashboardRequestModel.  # noqa: E501
        :rtype: JsonModel
        """
        return self._dashboard

    @dashboard.setter
    def dashboard(self, dashboard):
        """Sets the dashboard of this ImportDashboardRequestModel.


        :param dashboard: The dashboard of this ImportDashboardRequestModel.  # noqa: E501
        :type: JsonModel
        """

        self._dashboard = dashboard

    @property
    def folder_id(self):
        """Gets the folder_id of this ImportDashboardRequestModel.  # noqa: E501


        :return: The folder_id of this ImportDashboardRequestModel.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this ImportDashboardRequestModel.


        :param folder_id: The folder_id of this ImportDashboardRequestModel.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def folder_uid(self):
        """Gets the folder_uid of this ImportDashboardRequestModel.  # noqa: E501


        :return: The folder_uid of this ImportDashboardRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._folder_uid

    @folder_uid.setter
    def folder_uid(self, folder_uid):
        """Sets the folder_uid of this ImportDashboardRequestModel.


        :param folder_uid: The folder_uid of this ImportDashboardRequestModel.  # noqa: E501
        :type: str
        """

        self._folder_uid = folder_uid

    @property
    def inputs(self):
        """Gets the inputs of this ImportDashboardRequestModel.  # noqa: E501


        :return: The inputs of this ImportDashboardRequestModel.  # noqa: E501
        :rtype: list[ImportDashboardInputModel]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ImportDashboardRequestModel.


        :param inputs: The inputs of this ImportDashboardRequestModel.  # noqa: E501
        :type: list[ImportDashboardInputModel]
        """

        self._inputs = inputs

    @property
    def overwrite(self):
        """Gets the overwrite of this ImportDashboardRequestModel.  # noqa: E501


        :return: The overwrite of this ImportDashboardRequestModel.  # noqa: E501
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        """Sets the overwrite of this ImportDashboardRequestModel.


        :param overwrite: The overwrite of this ImportDashboardRequestModel.  # noqa: E501
        :type: bool
        """

        self._overwrite = overwrite

    @property
    def path(self):
        """Gets the path of this ImportDashboardRequestModel.  # noqa: E501


        :return: The path of this ImportDashboardRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ImportDashboardRequestModel.


        :param path: The path of this ImportDashboardRequestModel.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def plugin_id(self):
        """Gets the plugin_id of this ImportDashboardRequestModel.  # noqa: E501


        :return: The plugin_id of this ImportDashboardRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this ImportDashboardRequestModel.


        :param plugin_id: The plugin_id of this ImportDashboardRequestModel.  # noqa: E501
        :type: str
        """

        self._plugin_id = plugin_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ImportDashboardRequestModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportDashboardRequestModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportDashboardRequestModel):
            return True

        return self.to_dict() != other.to_dict()
