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


class PostableGrafanaRuleModel(object):
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
        'condition': 'str',
        'data': 'list[AlertQueryModel]',
        'exec_err_state': 'str',
        'no_data_state': 'str',
        'title': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'data': 'data',
        'exec_err_state': 'exec_err_state',
        'no_data_state': 'no_data_state',
        'title': 'title',
        'uid': 'uid'
    }

    def __init__(self, condition=None, data=None, exec_err_state=None, no_data_state=None, title=None, uid=None, _configuration=None):  # noqa: E501
        """PostableGrafanaRuleModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._condition = None
        self._data = None
        self._exec_err_state = None
        self._no_data_state = None
        self._title = None
        self._uid = None
        self.discriminator = None

        if condition is not None:
            self.condition = condition
        if data is not None:
            self.data = data
        if exec_err_state is not None:
            self.exec_err_state = exec_err_state
        if no_data_state is not None:
            self.no_data_state = no_data_state
        if title is not None:
            self.title = title
        if uid is not None:
            self.uid = uid

    @property
    def condition(self):
        """Gets the condition of this PostableGrafanaRuleModel.  # noqa: E501


        :return: The condition of this PostableGrafanaRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this PostableGrafanaRuleModel.


        :param condition: The condition of this PostableGrafanaRuleModel.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def data(self):
        """Gets the data of this PostableGrafanaRuleModel.  # noqa: E501


        :return: The data of this PostableGrafanaRuleModel.  # noqa: E501
        :rtype: list[AlertQueryModel]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PostableGrafanaRuleModel.


        :param data: The data of this PostableGrafanaRuleModel.  # noqa: E501
        :type: list[AlertQueryModel]
        """

        self._data = data

    @property
    def exec_err_state(self):
        """Gets the exec_err_state of this PostableGrafanaRuleModel.  # noqa: E501


        :return: The exec_err_state of this PostableGrafanaRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._exec_err_state

    @exec_err_state.setter
    def exec_err_state(self, exec_err_state):
        """Sets the exec_err_state of this PostableGrafanaRuleModel.


        :param exec_err_state: The exec_err_state of this PostableGrafanaRuleModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["OK", "Alerting", "Error"]  # noqa: E501
        if (self._configuration.client_side_validation and
                exec_err_state not in allowed_values):
            raise ValueError(
                "Invalid value for `exec_err_state` ({0}), must be one of {1}"  # noqa: E501
                .format(exec_err_state, allowed_values)
            )

        self._exec_err_state = exec_err_state

    @property
    def no_data_state(self):
        """Gets the no_data_state of this PostableGrafanaRuleModel.  # noqa: E501


        :return: The no_data_state of this PostableGrafanaRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._no_data_state

    @no_data_state.setter
    def no_data_state(self, no_data_state):
        """Sets the no_data_state of this PostableGrafanaRuleModel.


        :param no_data_state: The no_data_state of this PostableGrafanaRuleModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Alerting", "NoData", "OK"]  # noqa: E501
        if (self._configuration.client_side_validation and
                no_data_state not in allowed_values):
            raise ValueError(
                "Invalid value for `no_data_state` ({0}), must be one of {1}"  # noqa: E501
                .format(no_data_state, allowed_values)
            )

        self._no_data_state = no_data_state

    @property
    def title(self):
        """Gets the title of this PostableGrafanaRuleModel.  # noqa: E501


        :return: The title of this PostableGrafanaRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PostableGrafanaRuleModel.


        :param title: The title of this PostableGrafanaRuleModel.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def uid(self):
        """Gets the uid of this PostableGrafanaRuleModel.  # noqa: E501


        :return: The uid of this PostableGrafanaRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this PostableGrafanaRuleModel.


        :param uid: The uid of this PostableGrafanaRuleModel.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if issubclass(PostableGrafanaRuleModel, dict):
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
        if not isinstance(other, PostableGrafanaRuleModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostableGrafanaRuleModel):
            return True

        return self.to_dict() != other.to_dict()