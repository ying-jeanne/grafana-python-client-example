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


class ActiveUserStatsModel(object):
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
        'active_admins_and_editors': 'int',
        'active_users': 'int',
        'active_viewers': 'int'
    }

    attribute_map = {
        'active_admins_and_editors': 'active_admins_and_editors',
        'active_users': 'active_users',
        'active_viewers': 'active_viewers'
    }

    def __init__(self, active_admins_and_editors=None, active_users=None, active_viewers=None, _configuration=None):  # noqa: E501
        """ActiveUserStatsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_admins_and_editors = None
        self._active_users = None
        self._active_viewers = None
        self.discriminator = None

        if active_admins_and_editors is not None:
            self.active_admins_and_editors = active_admins_and_editors
        if active_users is not None:
            self.active_users = active_users
        if active_viewers is not None:
            self.active_viewers = active_viewers

    @property
    def active_admins_and_editors(self):
        """Gets the active_admins_and_editors of this ActiveUserStatsModel.  # noqa: E501


        :return: The active_admins_and_editors of this ActiveUserStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._active_admins_and_editors

    @active_admins_and_editors.setter
    def active_admins_and_editors(self, active_admins_and_editors):
        """Sets the active_admins_and_editors of this ActiveUserStatsModel.


        :param active_admins_and_editors: The active_admins_and_editors of this ActiveUserStatsModel.  # noqa: E501
        :type: int
        """

        self._active_admins_and_editors = active_admins_and_editors

    @property
    def active_users(self):
        """Gets the active_users of this ActiveUserStatsModel.  # noqa: E501


        :return: The active_users of this ActiveUserStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._active_users

    @active_users.setter
    def active_users(self, active_users):
        """Sets the active_users of this ActiveUserStatsModel.


        :param active_users: The active_users of this ActiveUserStatsModel.  # noqa: E501
        :type: int
        """

        self._active_users = active_users

    @property
    def active_viewers(self):
        """Gets the active_viewers of this ActiveUserStatsModel.  # noqa: E501


        :return: The active_viewers of this ActiveUserStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._active_viewers

    @active_viewers.setter
    def active_viewers(self, active_viewers):
        """Sets the active_viewers of this ActiveUserStatsModel.


        :param active_viewers: The active_viewers of this ActiveUserStatsModel.  # noqa: E501
        :type: int
        """

        self._active_viewers = active_viewers

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
        if issubclass(ActiveUserStatsModel, dict):
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
        if not isinstance(other, ActiveUserStatsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActiveUserStatsModel):
            return True

        return self.to_dict() != other.to_dict()
