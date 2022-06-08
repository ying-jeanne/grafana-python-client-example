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


class MessageTemplateModel(object):
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
        'name': 'str',
        'template': 'str',
        'provenance': 'ProvenanceModel'
    }

    attribute_map = {
        'name': 'Name',
        'template': 'Template',
        'provenance': 'provenance'
    }

    def __init__(self, name=None, template=None, provenance=None, _configuration=None):  # noqa: E501
        """MessageTemplateModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._template = None
        self._provenance = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if template is not None:
            self.template = template
        if provenance is not None:
            self.provenance = provenance

    @property
    def name(self):
        """Gets the name of this MessageTemplateModel.  # noqa: E501


        :return: The name of this MessageTemplateModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MessageTemplateModel.


        :param name: The name of this MessageTemplateModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def template(self):
        """Gets the template of this MessageTemplateModel.  # noqa: E501


        :return: The template of this MessageTemplateModel.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this MessageTemplateModel.


        :param template: The template of this MessageTemplateModel.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def provenance(self):
        """Gets the provenance of this MessageTemplateModel.  # noqa: E501


        :return: The provenance of this MessageTemplateModel.  # noqa: E501
        :rtype: ProvenanceModel
        """
        return self._provenance

    @provenance.setter
    def provenance(self, provenance):
        """Sets the provenance of this MessageTemplateModel.


        :param provenance: The provenance of this MessageTemplateModel.  # noqa: E501
        :type: ProvenanceModel
        """

        self._provenance = provenance

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
        if issubclass(MessageTemplateModel, dict):
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
        if not isinstance(other, MessageTemplateModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageTemplateModel):
            return True

        return self.to_dict() != other.to_dict()