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


class RouteModel(object):
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
        '_continue': 'bool',
        'group_by': 'list[str]',
        'group_interval': 'DurationModel',
        'group_wait': 'DurationModel',
        'match': 'dict(str, str)',
        'match_re': 'MatchRegexpsModel',
        'matchers': 'MatchersModel',
        'mute_time_intervals': 'list[str]',
        'object_matchers': 'ObjectMatchersModel',
        'provenance': 'ProvenanceModel',
        'receiver': 'str',
        'repeat_interval': 'DurationModel',
        'routes': 'list[RouteModel]'
    }

    attribute_map = {
        '_continue': 'continue',
        'group_by': 'group_by',
        'group_interval': 'group_interval',
        'group_wait': 'group_wait',
        'match': 'match',
        'match_re': 'match_re',
        'matchers': 'matchers',
        'mute_time_intervals': 'mute_time_intervals',
        'object_matchers': 'object_matchers',
        'provenance': 'provenance',
        'receiver': 'receiver',
        'repeat_interval': 'repeat_interval',
        'routes': 'routes'
    }

    def __init__(self, _continue=None, group_by=None, group_interval=None, group_wait=None, match=None, match_re=None, matchers=None, mute_time_intervals=None, object_matchers=None, provenance=None, receiver=None, repeat_interval=None, routes=None, _configuration=None):  # noqa: E501
        """RouteModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__continue = None
        self._group_by = None
        self._group_interval = None
        self._group_wait = None
        self._match = None
        self._match_re = None
        self._matchers = None
        self._mute_time_intervals = None
        self._object_matchers = None
        self._provenance = None
        self._receiver = None
        self._repeat_interval = None
        self._routes = None
        self.discriminator = None

        if _continue is not None:
            self._continue = _continue
        if group_by is not None:
            self.group_by = group_by
        if group_interval is not None:
            self.group_interval = group_interval
        if group_wait is not None:
            self.group_wait = group_wait
        if match is not None:
            self.match = match
        if match_re is not None:
            self.match_re = match_re
        if matchers is not None:
            self.matchers = matchers
        if mute_time_intervals is not None:
            self.mute_time_intervals = mute_time_intervals
        if object_matchers is not None:
            self.object_matchers = object_matchers
        if provenance is not None:
            self.provenance = provenance
        if receiver is not None:
            self.receiver = receiver
        if repeat_interval is not None:
            self.repeat_interval = repeat_interval
        if routes is not None:
            self.routes = routes

    @property
    def _continue(self):
        """Gets the _continue of this RouteModel.  # noqa: E501


        :return: The _continue of this RouteModel.  # noqa: E501
        :rtype: bool
        """
        return self.__continue

    @_continue.setter
    def _continue(self, _continue):
        """Sets the _continue of this RouteModel.


        :param _continue: The _continue of this RouteModel.  # noqa: E501
        :type: bool
        """

        self.__continue = _continue

    @property
    def group_by(self):
        """Gets the group_by of this RouteModel.  # noqa: E501


        :return: The group_by of this RouteModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this RouteModel.


        :param group_by: The group_by of this RouteModel.  # noqa: E501
        :type: list[str]
        """

        self._group_by = group_by

    @property
    def group_interval(self):
        """Gets the group_interval of this RouteModel.  # noqa: E501


        :return: The group_interval of this RouteModel.  # noqa: E501
        :rtype: DurationModel
        """
        return self._group_interval

    @group_interval.setter
    def group_interval(self, group_interval):
        """Sets the group_interval of this RouteModel.


        :param group_interval: The group_interval of this RouteModel.  # noqa: E501
        :type: DurationModel
        """

        self._group_interval = group_interval

    @property
    def group_wait(self):
        """Gets the group_wait of this RouteModel.  # noqa: E501


        :return: The group_wait of this RouteModel.  # noqa: E501
        :rtype: DurationModel
        """
        return self._group_wait

    @group_wait.setter
    def group_wait(self, group_wait):
        """Sets the group_wait of this RouteModel.


        :param group_wait: The group_wait of this RouteModel.  # noqa: E501
        :type: DurationModel
        """

        self._group_wait = group_wait

    @property
    def match(self):
        """Gets the match of this RouteModel.  # noqa: E501

        Deprecated. Remove before v1.0 release.  # noqa: E501

        :return: The match of this RouteModel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this RouteModel.

        Deprecated. Remove before v1.0 release.  # noqa: E501

        :param match: The match of this RouteModel.  # noqa: E501
        :type: dict(str, str)
        """

        self._match = match

    @property
    def match_re(self):
        """Gets the match_re of this RouteModel.  # noqa: E501


        :return: The match_re of this RouteModel.  # noqa: E501
        :rtype: MatchRegexpsModel
        """
        return self._match_re

    @match_re.setter
    def match_re(self, match_re):
        """Sets the match_re of this RouteModel.


        :param match_re: The match_re of this RouteModel.  # noqa: E501
        :type: MatchRegexpsModel
        """

        self._match_re = match_re

    @property
    def matchers(self):
        """Gets the matchers of this RouteModel.  # noqa: E501


        :return: The matchers of this RouteModel.  # noqa: E501
        :rtype: MatchersModel
        """
        return self._matchers

    @matchers.setter
    def matchers(self, matchers):
        """Sets the matchers of this RouteModel.


        :param matchers: The matchers of this RouteModel.  # noqa: E501
        :type: MatchersModel
        """

        self._matchers = matchers

    @property
    def mute_time_intervals(self):
        """Gets the mute_time_intervals of this RouteModel.  # noqa: E501


        :return: The mute_time_intervals of this RouteModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._mute_time_intervals

    @mute_time_intervals.setter
    def mute_time_intervals(self, mute_time_intervals):
        """Sets the mute_time_intervals of this RouteModel.


        :param mute_time_intervals: The mute_time_intervals of this RouteModel.  # noqa: E501
        :type: list[str]
        """

        self._mute_time_intervals = mute_time_intervals

    @property
    def object_matchers(self):
        """Gets the object_matchers of this RouteModel.  # noqa: E501


        :return: The object_matchers of this RouteModel.  # noqa: E501
        :rtype: ObjectMatchersModel
        """
        return self._object_matchers

    @object_matchers.setter
    def object_matchers(self, object_matchers):
        """Sets the object_matchers of this RouteModel.


        :param object_matchers: The object_matchers of this RouteModel.  # noqa: E501
        :type: ObjectMatchersModel
        """

        self._object_matchers = object_matchers

    @property
    def provenance(self):
        """Gets the provenance of this RouteModel.  # noqa: E501


        :return: The provenance of this RouteModel.  # noqa: E501
        :rtype: ProvenanceModel
        """
        return self._provenance

    @provenance.setter
    def provenance(self, provenance):
        """Sets the provenance of this RouteModel.


        :param provenance: The provenance of this RouteModel.  # noqa: E501
        :type: ProvenanceModel
        """

        self._provenance = provenance

    @property
    def receiver(self):
        """Gets the receiver of this RouteModel.  # noqa: E501


        :return: The receiver of this RouteModel.  # noqa: E501
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this RouteModel.


        :param receiver: The receiver of this RouteModel.  # noqa: E501
        :type: str
        """

        self._receiver = receiver

    @property
    def repeat_interval(self):
        """Gets the repeat_interval of this RouteModel.  # noqa: E501


        :return: The repeat_interval of this RouteModel.  # noqa: E501
        :rtype: DurationModel
        """
        return self._repeat_interval

    @repeat_interval.setter
    def repeat_interval(self, repeat_interval):
        """Sets the repeat_interval of this RouteModel.


        :param repeat_interval: The repeat_interval of this RouteModel.  # noqa: E501
        :type: DurationModel
        """

        self._repeat_interval = repeat_interval

    @property
    def routes(self):
        """Gets the routes of this RouteModel.  # noqa: E501


        :return: The routes of this RouteModel.  # noqa: E501
        :rtype: list[RouteModel]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this RouteModel.


        :param routes: The routes of this RouteModel.  # noqa: E501
        :type: list[RouteModel]
        """

        self._routes = routes

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
        if issubclass(RouteModel, dict):
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
        if not isinstance(other, RouteModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RouteModel):
            return True

        return self.to_dict() != other.to_dict()
