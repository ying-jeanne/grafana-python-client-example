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


class PrefsModel(object):
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
        'home_dashboard_id': 'int',
        'home_dashboard_uid': 'str',
        'navbar': 'NavbarPreferenceModel',
        'query_history': 'QueryHistoryPreferenceModel',
        'theme': 'str',
        'timezone': 'str',
        'week_start': 'str'
    }

    attribute_map = {
        'home_dashboard_id': 'homeDashboardId',
        'home_dashboard_uid': 'homeDashboardUID',
        'navbar': 'navbar',
        'query_history': 'queryHistory',
        'theme': 'theme',
        'timezone': 'timezone',
        'week_start': 'weekStart'
    }

    def __init__(self, home_dashboard_id=None, home_dashboard_uid=None, navbar=None, query_history=None, theme=None, timezone=None, week_start=None, _configuration=None):  # noqa: E501
        """PrefsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._home_dashboard_id = None
        self._home_dashboard_uid = None
        self._navbar = None
        self._query_history = None
        self._theme = None
        self._timezone = None
        self._week_start = None
        self.discriminator = None

        if home_dashboard_id is not None:
            self.home_dashboard_id = home_dashboard_id
        if home_dashboard_uid is not None:
            self.home_dashboard_uid = home_dashboard_uid
        if navbar is not None:
            self.navbar = navbar
        if query_history is not None:
            self.query_history = query_history
        if theme is not None:
            self.theme = theme
        if timezone is not None:
            self.timezone = timezone
        if week_start is not None:
            self.week_start = week_start

    @property
    def home_dashboard_id(self):
        """Gets the home_dashboard_id of this PrefsModel.  # noqa: E501


        :return: The home_dashboard_id of this PrefsModel.  # noqa: E501
        :rtype: int
        """
        return self._home_dashboard_id

    @home_dashboard_id.setter
    def home_dashboard_id(self, home_dashboard_id):
        """Sets the home_dashboard_id of this PrefsModel.


        :param home_dashboard_id: The home_dashboard_id of this PrefsModel.  # noqa: E501
        :type: int
        """

        self._home_dashboard_id = home_dashboard_id

    @property
    def home_dashboard_uid(self):
        """Gets the home_dashboard_uid of this PrefsModel.  # noqa: E501


        :return: The home_dashboard_uid of this PrefsModel.  # noqa: E501
        :rtype: str
        """
        return self._home_dashboard_uid

    @home_dashboard_uid.setter
    def home_dashboard_uid(self, home_dashboard_uid):
        """Sets the home_dashboard_uid of this PrefsModel.


        :param home_dashboard_uid: The home_dashboard_uid of this PrefsModel.  # noqa: E501
        :type: str
        """

        self._home_dashboard_uid = home_dashboard_uid

    @property
    def navbar(self):
        """Gets the navbar of this PrefsModel.  # noqa: E501


        :return: The navbar of this PrefsModel.  # noqa: E501
        :rtype: NavbarPreferenceModel
        """
        return self._navbar

    @navbar.setter
    def navbar(self, navbar):
        """Sets the navbar of this PrefsModel.


        :param navbar: The navbar of this PrefsModel.  # noqa: E501
        :type: NavbarPreferenceModel
        """

        self._navbar = navbar

    @property
    def query_history(self):
        """Gets the query_history of this PrefsModel.  # noqa: E501


        :return: The query_history of this PrefsModel.  # noqa: E501
        :rtype: QueryHistoryPreferenceModel
        """
        return self._query_history

    @query_history.setter
    def query_history(self, query_history):
        """Sets the query_history of this PrefsModel.


        :param query_history: The query_history of this PrefsModel.  # noqa: E501
        :type: QueryHistoryPreferenceModel
        """

        self._query_history = query_history

    @property
    def theme(self):
        """Gets the theme of this PrefsModel.  # noqa: E501


        :return: The theme of this PrefsModel.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this PrefsModel.


        :param theme: The theme of this PrefsModel.  # noqa: E501
        :type: str
        """

        self._theme = theme

    @property
    def timezone(self):
        """Gets the timezone of this PrefsModel.  # noqa: E501


        :return: The timezone of this PrefsModel.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this PrefsModel.


        :param timezone: The timezone of this PrefsModel.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def week_start(self):
        """Gets the week_start of this PrefsModel.  # noqa: E501


        :return: The week_start of this PrefsModel.  # noqa: E501
        :rtype: str
        """
        return self._week_start

    @week_start.setter
    def week_start(self, week_start):
        """Sets the week_start of this PrefsModel.


        :param week_start: The week_start of this PrefsModel.  # noqa: E501
        :type: str
        """

        self._week_start = week_start

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
        if issubclass(PrefsModel, dict):
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
        if not isinstance(other, PrefsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrefsModel):
            return True

        return self.to_dict() != other.to_dict()
