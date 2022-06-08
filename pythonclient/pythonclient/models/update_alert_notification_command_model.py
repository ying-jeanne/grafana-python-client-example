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


class UpdateAlertNotificationCommandModel(object):
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
        'disable_resolve_message': 'bool',
        'frequency': 'str',
        'id': 'int',
        'is_default': 'bool',
        'name': 'str',
        'secure_settings': 'dict(str, str)',
        'send_reminder': 'bool',
        'settings': 'JsonModel',
        'type': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'disable_resolve_message': 'disableResolveMessage',
        'frequency': 'frequency',
        'id': 'id',
        'is_default': 'isDefault',
        'name': 'name',
        'secure_settings': 'secureSettings',
        'send_reminder': 'sendReminder',
        'settings': 'settings',
        'type': 'type',
        'uid': 'uid'
    }

    def __init__(self, disable_resolve_message=None, frequency=None, id=None, is_default=None, name=None, secure_settings=None, send_reminder=None, settings=None, type=None, uid=None, _configuration=None):  # noqa: E501
        """UpdateAlertNotificationCommandModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._disable_resolve_message = None
        self._frequency = None
        self._id = None
        self._is_default = None
        self._name = None
        self._secure_settings = None
        self._send_reminder = None
        self._settings = None
        self._type = None
        self._uid = None
        self.discriminator = None

        if disable_resolve_message is not None:
            self.disable_resolve_message = disable_resolve_message
        if frequency is not None:
            self.frequency = frequency
        if id is not None:
            self.id = id
        if is_default is not None:
            self.is_default = is_default
        if name is not None:
            self.name = name
        if secure_settings is not None:
            self.secure_settings = secure_settings
        if send_reminder is not None:
            self.send_reminder = send_reminder
        if settings is not None:
            self.settings = settings
        if type is not None:
            self.type = type
        if uid is not None:
            self.uid = uid

    @property
    def disable_resolve_message(self):
        """Gets the disable_resolve_message of this UpdateAlertNotificationCommandModel.  # noqa: E501


        :return: The disable_resolve_message of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :rtype: bool
        """
        return self._disable_resolve_message

    @disable_resolve_message.setter
    def disable_resolve_message(self, disable_resolve_message):
        """Sets the disable_resolve_message of this UpdateAlertNotificationCommandModel.


        :param disable_resolve_message: The disable_resolve_message of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :type: bool
        """

        self._disable_resolve_message = disable_resolve_message

    @property
    def frequency(self):
        """Gets the frequency of this UpdateAlertNotificationCommandModel.  # noqa: E501


        :return: The frequency of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this UpdateAlertNotificationCommandModel.


        :param frequency: The frequency of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :type: str
        """

        self._frequency = frequency

    @property
    def id(self):
        """Gets the id of this UpdateAlertNotificationCommandModel.  # noqa: E501


        :return: The id of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateAlertNotificationCommandModel.


        :param id: The id of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_default(self):
        """Gets the is_default of this UpdateAlertNotificationCommandModel.  # noqa: E501


        :return: The is_default of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this UpdateAlertNotificationCommandModel.


        :param is_default: The is_default of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def name(self):
        """Gets the name of this UpdateAlertNotificationCommandModel.  # noqa: E501


        :return: The name of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAlertNotificationCommandModel.


        :param name: The name of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def secure_settings(self):
        """Gets the secure_settings of this UpdateAlertNotificationCommandModel.  # noqa: E501


        :return: The secure_settings of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._secure_settings

    @secure_settings.setter
    def secure_settings(self, secure_settings):
        """Sets the secure_settings of this UpdateAlertNotificationCommandModel.


        :param secure_settings: The secure_settings of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :type: dict(str, str)
        """

        self._secure_settings = secure_settings

    @property
    def send_reminder(self):
        """Gets the send_reminder of this UpdateAlertNotificationCommandModel.  # noqa: E501


        :return: The send_reminder of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :rtype: bool
        """
        return self._send_reminder

    @send_reminder.setter
    def send_reminder(self, send_reminder):
        """Sets the send_reminder of this UpdateAlertNotificationCommandModel.


        :param send_reminder: The send_reminder of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :type: bool
        """

        self._send_reminder = send_reminder

    @property
    def settings(self):
        """Gets the settings of this UpdateAlertNotificationCommandModel.  # noqa: E501


        :return: The settings of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :rtype: JsonModel
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this UpdateAlertNotificationCommandModel.


        :param settings: The settings of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :type: JsonModel
        """

        self._settings = settings

    @property
    def type(self):
        """Gets the type of this UpdateAlertNotificationCommandModel.  # noqa: E501


        :return: The type of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateAlertNotificationCommandModel.


        :param type: The type of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this UpdateAlertNotificationCommandModel.  # noqa: E501


        :return: The uid of this UpdateAlertNotificationCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this UpdateAlertNotificationCommandModel.


        :param uid: The uid of this UpdateAlertNotificationCommandModel.  # noqa: E501
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
        if issubclass(UpdateAlertNotificationCommandModel, dict):
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
        if not isinstance(other, UpdateAlertNotificationCommandModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAlertNotificationCommandModel):
            return True

        return self.to_dict() != other.to_dict()
