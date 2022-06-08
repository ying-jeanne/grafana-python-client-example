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


class GettableUserConfigModel(object):
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
        'alertmanager_config': 'GettableApiAlertingConfigModel',
        'template_file_provenances': 'dict(str, ProvenanceModel)',
        'template_files': 'dict(str, str)'
    }

    attribute_map = {
        'alertmanager_config': 'alertmanager_config',
        'template_file_provenances': 'template_file_provenances',
        'template_files': 'template_files'
    }

    def __init__(self, alertmanager_config=None, template_file_provenances=None, template_files=None, _configuration=None):  # noqa: E501
        """GettableUserConfigModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alertmanager_config = None
        self._template_file_provenances = None
        self._template_files = None
        self.discriminator = None

        if alertmanager_config is not None:
            self.alertmanager_config = alertmanager_config
        if template_file_provenances is not None:
            self.template_file_provenances = template_file_provenances
        if template_files is not None:
            self.template_files = template_files

    @property
    def alertmanager_config(self):
        """Gets the alertmanager_config of this GettableUserConfigModel.  # noqa: E501


        :return: The alertmanager_config of this GettableUserConfigModel.  # noqa: E501
        :rtype: GettableApiAlertingConfigModel
        """
        return self._alertmanager_config

    @alertmanager_config.setter
    def alertmanager_config(self, alertmanager_config):
        """Sets the alertmanager_config of this GettableUserConfigModel.


        :param alertmanager_config: The alertmanager_config of this GettableUserConfigModel.  # noqa: E501
        :type: GettableApiAlertingConfigModel
        """

        self._alertmanager_config = alertmanager_config

    @property
    def template_file_provenances(self):
        """Gets the template_file_provenances of this GettableUserConfigModel.  # noqa: E501


        :return: The template_file_provenances of this GettableUserConfigModel.  # noqa: E501
        :rtype: dict(str, ProvenanceModel)
        """
        return self._template_file_provenances

    @template_file_provenances.setter
    def template_file_provenances(self, template_file_provenances):
        """Sets the template_file_provenances of this GettableUserConfigModel.


        :param template_file_provenances: The template_file_provenances of this GettableUserConfigModel.  # noqa: E501
        :type: dict(str, ProvenanceModel)
        """

        self._template_file_provenances = template_file_provenances

    @property
    def template_files(self):
        """Gets the template_files of this GettableUserConfigModel.  # noqa: E501


        :return: The template_files of this GettableUserConfigModel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._template_files

    @template_files.setter
    def template_files(self, template_files):
        """Sets the template_files of this GettableUserConfigModel.


        :param template_files: The template_files of this GettableUserConfigModel.  # noqa: E501
        :type: dict(str, str)
        """

        self._template_files = template_files

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
        if issubclass(GettableUserConfigModel, dict):
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
        if not isinstance(other, GettableUserConfigModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GettableUserConfigModel):
            return True

        return self.to_dict() != other.to_dict()
