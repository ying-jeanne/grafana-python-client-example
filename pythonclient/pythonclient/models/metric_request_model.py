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


class MetricRequestModel(object):
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
        'debug': 'bool',
        '_from': 'str',
        'queries': 'list[JsonModel]',
        'to': 'str'
    }

    attribute_map = {
        'debug': 'debug',
        '_from': 'from',
        'queries': 'queries',
        'to': 'to'
    }

    def __init__(self, debug=None, _from=None, queries=None, to=None, _configuration=None):  # noqa: E501
        """MetricRequestModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._debug = None
        self.__from = None
        self._queries = None
        self._to = None
        self.discriminator = None

        if debug is not None:
            self.debug = debug
        self._from = _from
        self.queries = queries
        self.to = to

    @property
    def debug(self):
        """Gets the debug of this MetricRequestModel.  # noqa: E501


        :return: The debug of this MetricRequestModel.  # noqa: E501
        :rtype: bool
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this MetricRequestModel.


        :param debug: The debug of this MetricRequestModel.  # noqa: E501
        :type: bool
        """

        self._debug = debug

    @property
    def _from(self):
        """Gets the _from of this MetricRequestModel.  # noqa: E501

        From Start time in epoch timestamps in milliseconds or relative using Grafana time units.  # noqa: E501

        :return: The _from of this MetricRequestModel.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this MetricRequestModel.

        From Start time in epoch timestamps in milliseconds or relative using Grafana time units.  # noqa: E501

        :param _from: The _from of this MetricRequestModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def queries(self):
        """Gets the queries of this MetricRequestModel.  # noqa: E501

        queries.refId – Specifies an identifier of the query. Is optional and default to “A”. queries.datasourceId – Specifies the data source to be queried. Each query in the request must have an unique datasourceId. queries.maxDataPoints - Species maximum amount of data points that dashboard panel can render. Is optional and default to 100. queries.intervalMs - Specifies the time interval in milliseconds of time series. Is optional and defaults to 1000.  # noqa: E501

        :return: The queries of this MetricRequestModel.  # noqa: E501
        :rtype: list[JsonModel]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this MetricRequestModel.

        queries.refId – Specifies an identifier of the query. Is optional and default to “A”. queries.datasourceId – Specifies the data source to be queried. Each query in the request must have an unique datasourceId. queries.maxDataPoints - Species maximum amount of data points that dashboard panel can render. Is optional and default to 100. queries.intervalMs - Specifies the time interval in milliseconds of time series. Is optional and defaults to 1000.  # noqa: E501

        :param queries: The queries of this MetricRequestModel.  # noqa: E501
        :type: list[JsonModel]
        """
        if self._configuration.client_side_validation and queries is None:
            raise ValueError("Invalid value for `queries`, must not be `None`")  # noqa: E501

        self._queries = queries

    @property
    def to(self):
        """Gets the to of this MetricRequestModel.  # noqa: E501

        To End time in epoch timestamps in milliseconds or relative using Grafana time units.  # noqa: E501

        :return: The to of this MetricRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this MetricRequestModel.

        To End time in epoch timestamps in milliseconds or relative using Grafana time units.  # noqa: E501

        :param to: The to of this MetricRequestModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

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
        if issubclass(MetricRequestModel, dict):
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
        if not isinstance(other, MetricRequestModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricRequestModel):
            return True

        return self.to_dict() != other.to_dict()
