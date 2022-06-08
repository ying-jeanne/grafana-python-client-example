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

from gpyclient.configuration import Configuration


class DashboardPanelFieldConfigOverridesModel(object):
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
        'matcher': 'DashboardPanelFieldConfigMatcherModel',
        'properties': 'list[DashboardPanelFieldConfigPropertiesModel]'
    }

    attribute_map = {
        'matcher': 'matcher',
        'properties': 'properties'
    }

    def __init__(self, matcher=None, properties=None, _configuration=None):  # noqa: E501
        """DashboardPanelFieldConfigOverridesModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._matcher = None
        self._properties = None
        self.discriminator = None

        self.matcher = matcher
        self.properties = properties

    @property
    def matcher(self):
        """Gets the matcher of this DashboardPanelFieldConfigOverridesModel.  # noqa: E501


        :return: The matcher of this DashboardPanelFieldConfigOverridesModel.  # noqa: E501
        :rtype: DashboardPanelFieldConfigMatcherModel
        """
        return self._matcher

    @matcher.setter
    def matcher(self, matcher):
        """Sets the matcher of this DashboardPanelFieldConfigOverridesModel.


        :param matcher: The matcher of this DashboardPanelFieldConfigOverridesModel.  # noqa: E501
        :type: DashboardPanelFieldConfigMatcherModel
        """
        if self._configuration.client_side_validation and matcher is None:
            raise ValueError("Invalid value for `matcher`, must not be `None`")  # noqa: E501

        self._matcher = matcher

    @property
    def properties(self):
        """Gets the properties of this DashboardPanelFieldConfigOverridesModel.  # noqa: E501


        :return: The properties of this DashboardPanelFieldConfigOverridesModel.  # noqa: E501
        :rtype: list[DashboardPanelFieldConfigPropertiesModel]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DashboardPanelFieldConfigOverridesModel.


        :param properties: The properties of this DashboardPanelFieldConfigOverridesModel.  # noqa: E501
        :type: list[DashboardPanelFieldConfigPropertiesModel]
        """
        if self._configuration.client_side_validation and properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

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
        if issubclass(DashboardPanelFieldConfigOverridesModel, dict):
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
        if not isinstance(other, DashboardPanelFieldConfigOverridesModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardPanelFieldConfigOverridesModel):
            return True

        return self.to_dict() != other.to_dict()
