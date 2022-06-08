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


class SettingsDTOModel(object):
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
        'branding': 'BrandingOptionsDTOModel',
        'id': 'int',
        'org_id': 'int',
        'user_id': 'int'
    }

    attribute_map = {
        'branding': 'branding',
        'id': 'id',
        'org_id': 'orgId',
        'user_id': 'userId'
    }

    def __init__(self, branding=None, id=None, org_id=None, user_id=None, _configuration=None):  # noqa: E501
        """SettingsDTOModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._branding = None
        self._id = None
        self._org_id = None
        self._user_id = None
        self.discriminator = None

        if branding is not None:
            self.branding = branding
        if id is not None:
            self.id = id
        if org_id is not None:
            self.org_id = org_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def branding(self):
        """Gets the branding of this SettingsDTOModel.  # noqa: E501


        :return: The branding of this SettingsDTOModel.  # noqa: E501
        :rtype: BrandingOptionsDTOModel
        """
        return self._branding

    @branding.setter
    def branding(self, branding):
        """Sets the branding of this SettingsDTOModel.


        :param branding: The branding of this SettingsDTOModel.  # noqa: E501
        :type: BrandingOptionsDTOModel
        """

        self._branding = branding

    @property
    def id(self):
        """Gets the id of this SettingsDTOModel.  # noqa: E501


        :return: The id of this SettingsDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SettingsDTOModel.


        :param id: The id of this SettingsDTOModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this SettingsDTOModel.  # noqa: E501


        :return: The org_id of this SettingsDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this SettingsDTOModel.


        :param org_id: The org_id of this SettingsDTOModel.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def user_id(self):
        """Gets the user_id of this SettingsDTOModel.  # noqa: E501


        :return: The user_id of this SettingsDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SettingsDTOModel.


        :param user_id: The user_id of this SettingsDTOModel.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(SettingsDTOModel, dict):
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
        if not isinstance(other, SettingsDTOModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsDTOModel):
            return True

        return self.to_dict() != other.to_dict()
