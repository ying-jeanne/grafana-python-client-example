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


class RecordingRuleJSONModel(object):
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
        'active': 'bool',
        'count': 'bool',
        'description': 'str',
        'dest_data_source_uid': 'str',
        'id': 'str',
        'interval': 'int',
        'name': 'str',
        'prom_name': 'str',
        'queries': 'list[dict(str, object)]',
        'range': 'int',
        'target_ref_id': 'str'
    }

    attribute_map = {
        'active': 'active',
        'count': 'count',
        'description': 'description',
        'dest_data_source_uid': 'dest_data_source_uid',
        'id': 'id',
        'interval': 'interval',
        'name': 'name',
        'prom_name': 'prom_name',
        'queries': 'queries',
        'range': 'range',
        'target_ref_id': 'target_ref_id'
    }

    def __init__(self, active=None, count=None, description=None, dest_data_source_uid=None, id=None, interval=None, name=None, prom_name=None, queries=None, range=None, target_ref_id=None, _configuration=None):  # noqa: E501
        """RecordingRuleJSONModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._count = None
        self._description = None
        self._dest_data_source_uid = None
        self._id = None
        self._interval = None
        self._name = None
        self._prom_name = None
        self._queries = None
        self._range = None
        self._target_ref_id = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if count is not None:
            self.count = count
        if description is not None:
            self.description = description
        if dest_data_source_uid is not None:
            self.dest_data_source_uid = dest_data_source_uid
        if id is not None:
            self.id = id
        if interval is not None:
            self.interval = interval
        if name is not None:
            self.name = name
        if prom_name is not None:
            self.prom_name = prom_name
        if queries is not None:
            self.queries = queries
        if range is not None:
            self.range = range
        if target_ref_id is not None:
            self.target_ref_id = target_ref_id

    @property
    def active(self):
        """Gets the active of this RecordingRuleJSONModel.  # noqa: E501


        :return: The active of this RecordingRuleJSONModel.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this RecordingRuleJSONModel.


        :param active: The active of this RecordingRuleJSONModel.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def count(self):
        """Gets the count of this RecordingRuleJSONModel.  # noqa: E501


        :return: The count of this RecordingRuleJSONModel.  # noqa: E501
        :rtype: bool
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this RecordingRuleJSONModel.


        :param count: The count of this RecordingRuleJSONModel.  # noqa: E501
        :type: bool
        """

        self._count = count

    @property
    def description(self):
        """Gets the description of this RecordingRuleJSONModel.  # noqa: E501


        :return: The description of this RecordingRuleJSONModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RecordingRuleJSONModel.


        :param description: The description of this RecordingRuleJSONModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dest_data_source_uid(self):
        """Gets the dest_data_source_uid of this RecordingRuleJSONModel.  # noqa: E501


        :return: The dest_data_source_uid of this RecordingRuleJSONModel.  # noqa: E501
        :rtype: str
        """
        return self._dest_data_source_uid

    @dest_data_source_uid.setter
    def dest_data_source_uid(self, dest_data_source_uid):
        """Sets the dest_data_source_uid of this RecordingRuleJSONModel.


        :param dest_data_source_uid: The dest_data_source_uid of this RecordingRuleJSONModel.  # noqa: E501
        :type: str
        """

        self._dest_data_source_uid = dest_data_source_uid

    @property
    def id(self):
        """Gets the id of this RecordingRuleJSONModel.  # noqa: E501


        :return: The id of this RecordingRuleJSONModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecordingRuleJSONModel.


        :param id: The id of this RecordingRuleJSONModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def interval(self):
        """Gets the interval of this RecordingRuleJSONModel.  # noqa: E501


        :return: The interval of this RecordingRuleJSONModel.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this RecordingRuleJSONModel.


        :param interval: The interval of this RecordingRuleJSONModel.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def name(self):
        """Gets the name of this RecordingRuleJSONModel.  # noqa: E501


        :return: The name of this RecordingRuleJSONModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecordingRuleJSONModel.


        :param name: The name of this RecordingRuleJSONModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def prom_name(self):
        """Gets the prom_name of this RecordingRuleJSONModel.  # noqa: E501


        :return: The prom_name of this RecordingRuleJSONModel.  # noqa: E501
        :rtype: str
        """
        return self._prom_name

    @prom_name.setter
    def prom_name(self, prom_name):
        """Sets the prom_name of this RecordingRuleJSONModel.


        :param prom_name: The prom_name of this RecordingRuleJSONModel.  # noqa: E501
        :type: str
        """

        self._prom_name = prom_name

    @property
    def queries(self):
        """Gets the queries of this RecordingRuleJSONModel.  # noqa: E501


        :return: The queries of this RecordingRuleJSONModel.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this RecordingRuleJSONModel.


        :param queries: The queries of this RecordingRuleJSONModel.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._queries = queries

    @property
    def range(self):
        """Gets the range of this RecordingRuleJSONModel.  # noqa: E501


        :return: The range of this RecordingRuleJSONModel.  # noqa: E501
        :rtype: int
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this RecordingRuleJSONModel.


        :param range: The range of this RecordingRuleJSONModel.  # noqa: E501
        :type: int
        """

        self._range = range

    @property
    def target_ref_id(self):
        """Gets the target_ref_id of this RecordingRuleJSONModel.  # noqa: E501


        :return: The target_ref_id of this RecordingRuleJSONModel.  # noqa: E501
        :rtype: str
        """
        return self._target_ref_id

    @target_ref_id.setter
    def target_ref_id(self, target_ref_id):
        """Sets the target_ref_id of this RecordingRuleJSONModel.


        :param target_ref_id: The target_ref_id of this RecordingRuleJSONModel.  # noqa: E501
        :type: str
        """

        self._target_ref_id = target_ref_id

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
        if issubclass(RecordingRuleJSONModel, dict):
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
        if not isinstance(other, RecordingRuleJSONModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecordingRuleJSONModel):
            return True

        return self.to_dict() != other.to_dict()
