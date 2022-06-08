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


class PagerdutyImageModel(object):
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
        'alt': 'str',
        'href': 'str',
        'src': 'str'
    }

    attribute_map = {
        'alt': 'alt',
        'href': 'href',
        'src': 'src'
    }

    def __init__(self, alt=None, href=None, src=None, _configuration=None):  # noqa: E501
        """PagerdutyImageModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alt = None
        self._href = None
        self._src = None
        self.discriminator = None

        if alt is not None:
            self.alt = alt
        if href is not None:
            self.href = href
        if src is not None:
            self.src = src

    @property
    def alt(self):
        """Gets the alt of this PagerdutyImageModel.  # noqa: E501


        :return: The alt of this PagerdutyImageModel.  # noqa: E501
        :rtype: str
        """
        return self._alt

    @alt.setter
    def alt(self, alt):
        """Sets the alt of this PagerdutyImageModel.


        :param alt: The alt of this PagerdutyImageModel.  # noqa: E501
        :type: str
        """

        self._alt = alt

    @property
    def href(self):
        """Gets the href of this PagerdutyImageModel.  # noqa: E501


        :return: The href of this PagerdutyImageModel.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PagerdutyImageModel.


        :param href: The href of this PagerdutyImageModel.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def src(self):
        """Gets the src of this PagerdutyImageModel.  # noqa: E501


        :return: The src of this PagerdutyImageModel.  # noqa: E501
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """Sets the src of this PagerdutyImageModel.


        :param src: The src of this PagerdutyImageModel.  # noqa: E501
        :type: str
        """

        self._src = src

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
        if issubclass(PagerdutyImageModel, dict):
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
        if not isinstance(other, PagerdutyImageModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PagerdutyImageModel):
            return True

        return self.to_dict() != other.to_dict()
