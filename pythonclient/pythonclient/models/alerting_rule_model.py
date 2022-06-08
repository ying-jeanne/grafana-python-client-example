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


class AlertingRuleModel(object):
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
        'alerts': 'list[AlertModel]',
        'annotations': 'OverrideLabelsModel',
        'duration': 'float',
        'evaluation_time': 'float',
        'health': 'str',
        'labels': 'OverrideLabelsModel',
        'last_error': 'str',
        'last_evaluation': 'datetime',
        'name': 'str',
        'query': 'str',
        'state': 'str',
        'type': 'RuleTypeModel'
    }

    attribute_map = {
        'alerts': 'alerts',
        'annotations': 'annotations',
        'duration': 'duration',
        'evaluation_time': 'evaluationTime',
        'health': 'health',
        'labels': 'labels',
        'last_error': 'lastError',
        'last_evaluation': 'lastEvaluation',
        'name': 'name',
        'query': 'query',
        'state': 'state',
        'type': 'type'
    }

    def __init__(self, alerts=None, annotations=None, duration=None, evaluation_time=None, health=None, labels=None, last_error=None, last_evaluation=None, name=None, query=None, state=None, type=None, _configuration=None):  # noqa: E501
        """AlertingRuleModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alerts = None
        self._annotations = None
        self._duration = None
        self._evaluation_time = None
        self._health = None
        self._labels = None
        self._last_error = None
        self._last_evaluation = None
        self._name = None
        self._query = None
        self._state = None
        self._type = None
        self.discriminator = None

        self.alerts = alerts
        self.annotations = annotations
        if duration is not None:
            self.duration = duration
        if evaluation_time is not None:
            self.evaluation_time = evaluation_time
        self.health = health
        if labels is not None:
            self.labels = labels
        if last_error is not None:
            self.last_error = last_error
        if last_evaluation is not None:
            self.last_evaluation = last_evaluation
        self.name = name
        self.query = query
        self.state = state
        self.type = type

    @property
    def alerts(self):
        """Gets the alerts of this AlertingRuleModel.  # noqa: E501


        :return: The alerts of this AlertingRuleModel.  # noqa: E501
        :rtype: list[AlertModel]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this AlertingRuleModel.


        :param alerts: The alerts of this AlertingRuleModel.  # noqa: E501
        :type: list[AlertModel]
        """
        if self._configuration.client_side_validation and alerts is None:
            raise ValueError("Invalid value for `alerts`, must not be `None`")  # noqa: E501

        self._alerts = alerts

    @property
    def annotations(self):
        """Gets the annotations of this AlertingRuleModel.  # noqa: E501


        :return: The annotations of this AlertingRuleModel.  # noqa: E501
        :rtype: OverrideLabelsModel
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this AlertingRuleModel.


        :param annotations: The annotations of this AlertingRuleModel.  # noqa: E501
        :type: OverrideLabelsModel
        """
        if self._configuration.client_side_validation and annotations is None:
            raise ValueError("Invalid value for `annotations`, must not be `None`")  # noqa: E501

        self._annotations = annotations

    @property
    def duration(self):
        """Gets the duration of this AlertingRuleModel.  # noqa: E501


        :return: The duration of this AlertingRuleModel.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AlertingRuleModel.


        :param duration: The duration of this AlertingRuleModel.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def evaluation_time(self):
        """Gets the evaluation_time of this AlertingRuleModel.  # noqa: E501


        :return: The evaluation_time of this AlertingRuleModel.  # noqa: E501
        :rtype: float
        """
        return self._evaluation_time

    @evaluation_time.setter
    def evaluation_time(self, evaluation_time):
        """Sets the evaluation_time of this AlertingRuleModel.


        :param evaluation_time: The evaluation_time of this AlertingRuleModel.  # noqa: E501
        :type: float
        """

        self._evaluation_time = evaluation_time

    @property
    def health(self):
        """Gets the health of this AlertingRuleModel.  # noqa: E501


        :return: The health of this AlertingRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this AlertingRuleModel.


        :param health: The health of this AlertingRuleModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and health is None:
            raise ValueError("Invalid value for `health`, must not be `None`")  # noqa: E501

        self._health = health

    @property
    def labels(self):
        """Gets the labels of this AlertingRuleModel.  # noqa: E501


        :return: The labels of this AlertingRuleModel.  # noqa: E501
        :rtype: OverrideLabelsModel
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this AlertingRuleModel.


        :param labels: The labels of this AlertingRuleModel.  # noqa: E501
        :type: OverrideLabelsModel
        """

        self._labels = labels

    @property
    def last_error(self):
        """Gets the last_error of this AlertingRuleModel.  # noqa: E501


        :return: The last_error of this AlertingRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._last_error

    @last_error.setter
    def last_error(self, last_error):
        """Sets the last_error of this AlertingRuleModel.


        :param last_error: The last_error of this AlertingRuleModel.  # noqa: E501
        :type: str
        """

        self._last_error = last_error

    @property
    def last_evaluation(self):
        """Gets the last_evaluation of this AlertingRuleModel.  # noqa: E501


        :return: The last_evaluation of this AlertingRuleModel.  # noqa: E501
        :rtype: datetime
        """
        return self._last_evaluation

    @last_evaluation.setter
    def last_evaluation(self, last_evaluation):
        """Sets the last_evaluation of this AlertingRuleModel.


        :param last_evaluation: The last_evaluation of this AlertingRuleModel.  # noqa: E501
        :type: datetime
        """

        self._last_evaluation = last_evaluation

    @property
    def name(self):
        """Gets the name of this AlertingRuleModel.  # noqa: E501


        :return: The name of this AlertingRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlertingRuleModel.


        :param name: The name of this AlertingRuleModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def query(self):
        """Gets the query of this AlertingRuleModel.  # noqa: E501


        :return: The query of this AlertingRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this AlertingRuleModel.


        :param query: The query of this AlertingRuleModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def state(self):
        """Gets the state of this AlertingRuleModel.  # noqa: E501

        State can be \"pending\", \"firing\", \"inactive\".  # noqa: E501

        :return: The state of this AlertingRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AlertingRuleModel.

        State can be \"pending\", \"firing\", \"inactive\".  # noqa: E501

        :param state: The state of this AlertingRuleModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def type(self):
        """Gets the type of this AlertingRuleModel.  # noqa: E501


        :return: The type of this AlertingRuleModel.  # noqa: E501
        :rtype: RuleTypeModel
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlertingRuleModel.


        :param type: The type of this AlertingRuleModel.  # noqa: E501
        :type: RuleTypeModel
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(AlertingRuleModel, dict):
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
        if not isinstance(other, AlertingRuleModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertingRuleModel):
            return True

        return self.to_dict() != other.to_dict()
