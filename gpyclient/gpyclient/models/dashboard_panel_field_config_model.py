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


class DashboardPanelFieldConfigModel(object):
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
        'defaults': 'DashboardPanelFieldConfigDefaultsModel',
        'overrides': 'list[DashboardPanelFieldConfigOverridesModel]'
    }

    attribute_map = {
        'defaults': 'defaults',
        'overrides': 'overrides'
    }

    def __init__(self, defaults=None, overrides=None, _configuration=None):  # noqa: E501
        """DashboardPanelFieldConfigModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._defaults = None
        self._overrides = None
        self.discriminator = None

        self.defaults = defaults
        self.overrides = overrides

    @property
    def defaults(self):
        """Gets the defaults of this DashboardPanelFieldConfigModel.  # noqa: E501


        :return: The defaults of this DashboardPanelFieldConfigModel.  # noqa: E501
        :rtype: DashboardPanelFieldConfigDefaultsModel
        """
        return self._defaults

    @defaults.setter
    def defaults(self, defaults):
        """Sets the defaults of this DashboardPanelFieldConfigModel.


        :param defaults: The defaults of this DashboardPanelFieldConfigModel.  # noqa: E501
        :type: DashboardPanelFieldConfigDefaultsModel
        """
        if self._configuration.client_side_validation and defaults is None:
            raise ValueError("Invalid value for `defaults`, must not be `None`")  # noqa: E501

        self._defaults = defaults

    @property
    def overrides(self):
        """Gets the overrides of this DashboardPanelFieldConfigModel.  # noqa: E501


        :return: The overrides of this DashboardPanelFieldConfigModel.  # noqa: E501
        :rtype: list[DashboardPanelFieldConfigOverridesModel]
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this DashboardPanelFieldConfigModel.


        :param overrides: The overrides of this DashboardPanelFieldConfigModel.  # noqa: E501
        :type: list[DashboardPanelFieldConfigOverridesModel]
        """
        if self._configuration.client_side_validation and overrides is None:
            raise ValueError("Invalid value for `overrides`, must not be `None`")  # noqa: E501

        self._overrides = overrides

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
        if issubclass(DashboardPanelFieldConfigModel, dict):
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
        if not isinstance(other, DashboardPanelFieldConfigModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardPanelFieldConfigModel):
            return True

        return self.to_dict() != other.to_dict()
