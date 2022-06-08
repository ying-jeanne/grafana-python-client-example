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


class ItemDTOModel(object):
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
        'alert_id': 'int',
        'alert_name': 'str',
        'avatar_url': 'str',
        'created': 'int',
        'dashboard_id': 'int',
        'dashboard_uid': 'str',
        'data': 'JsonModel',
        'email': 'str',
        'id': 'int',
        'login': 'str',
        'new_state': 'str',
        'panel_id': 'int',
        'prev_state': 'str',
        'tags': 'list[str]',
        'text': 'str',
        'time': 'int',
        'time_end': 'int',
        'updated': 'int',
        'user_id': 'int'
    }

    attribute_map = {
        'alert_id': 'alertId',
        'alert_name': 'alertName',
        'avatar_url': 'avatarUrl',
        'created': 'created',
        'dashboard_id': 'dashboardId',
        'dashboard_uid': 'dashboardUID',
        'data': 'data',
        'email': 'email',
        'id': 'id',
        'login': 'login',
        'new_state': 'newState',
        'panel_id': 'panelId',
        'prev_state': 'prevState',
        'tags': 'tags',
        'text': 'text',
        'time': 'time',
        'time_end': 'timeEnd',
        'updated': 'updated',
        'user_id': 'userId'
    }

    def __init__(self, alert_id=None, alert_name=None, avatar_url=None, created=None, dashboard_id=None, dashboard_uid=None, data=None, email=None, id=None, login=None, new_state=None, panel_id=None, prev_state=None, tags=None, text=None, time=None, time_end=None, updated=None, user_id=None, _configuration=None):  # noqa: E501
        """ItemDTOModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alert_id = None
        self._alert_name = None
        self._avatar_url = None
        self._created = None
        self._dashboard_id = None
        self._dashboard_uid = None
        self._data = None
        self._email = None
        self._id = None
        self._login = None
        self._new_state = None
        self._panel_id = None
        self._prev_state = None
        self._tags = None
        self._text = None
        self._time = None
        self._time_end = None
        self._updated = None
        self._user_id = None
        self.discriminator = None

        if alert_id is not None:
            self.alert_id = alert_id
        if alert_name is not None:
            self.alert_name = alert_name
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if created is not None:
            self.created = created
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if dashboard_uid is not None:
            self.dashboard_uid = dashboard_uid
        if data is not None:
            self.data = data
        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if login is not None:
            self.login = login
        if new_state is not None:
            self.new_state = new_state
        if panel_id is not None:
            self.panel_id = panel_id
        if prev_state is not None:
            self.prev_state = prev_state
        if tags is not None:
            self.tags = tags
        if text is not None:
            self.text = text
        if time is not None:
            self.time = time
        if time_end is not None:
            self.time_end = time_end
        if updated is not None:
            self.updated = updated
        if user_id is not None:
            self.user_id = user_id

    @property
    def alert_id(self):
        """Gets the alert_id of this ItemDTOModel.  # noqa: E501


        :return: The alert_id of this ItemDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        """Sets the alert_id of this ItemDTOModel.


        :param alert_id: The alert_id of this ItemDTOModel.  # noqa: E501
        :type: int
        """

        self._alert_id = alert_id

    @property
    def alert_name(self):
        """Gets the alert_name of this ItemDTOModel.  # noqa: E501


        :return: The alert_name of this ItemDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._alert_name

    @alert_name.setter
    def alert_name(self, alert_name):
        """Sets the alert_name of this ItemDTOModel.


        :param alert_name: The alert_name of this ItemDTOModel.  # noqa: E501
        :type: str
        """

        self._alert_name = alert_name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this ItemDTOModel.  # noqa: E501


        :return: The avatar_url of this ItemDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this ItemDTOModel.


        :param avatar_url: The avatar_url of this ItemDTOModel.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def created(self):
        """Gets the created of this ItemDTOModel.  # noqa: E501


        :return: The created of this ItemDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ItemDTOModel.


        :param created: The created of this ItemDTOModel.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this ItemDTOModel.  # noqa: E501


        :return: The dashboard_id of this ItemDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this ItemDTOModel.


        :param dashboard_id: The dashboard_id of this ItemDTOModel.  # noqa: E501
        :type: int
        """

        self._dashboard_id = dashboard_id

    @property
    def dashboard_uid(self):
        """Gets the dashboard_uid of this ItemDTOModel.  # noqa: E501


        :return: The dashboard_uid of this ItemDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_uid

    @dashboard_uid.setter
    def dashboard_uid(self, dashboard_uid):
        """Sets the dashboard_uid of this ItemDTOModel.


        :param dashboard_uid: The dashboard_uid of this ItemDTOModel.  # noqa: E501
        :type: str
        """

        self._dashboard_uid = dashboard_uid

    @property
    def data(self):
        """Gets the data of this ItemDTOModel.  # noqa: E501


        :return: The data of this ItemDTOModel.  # noqa: E501
        :rtype: JsonModel
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ItemDTOModel.


        :param data: The data of this ItemDTOModel.  # noqa: E501
        :type: JsonModel
        """

        self._data = data

    @property
    def email(self):
        """Gets the email of this ItemDTOModel.  # noqa: E501


        :return: The email of this ItemDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ItemDTOModel.


        :param email: The email of this ItemDTOModel.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this ItemDTOModel.  # noqa: E501


        :return: The id of this ItemDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemDTOModel.


        :param id: The id of this ItemDTOModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def login(self):
        """Gets the login of this ItemDTOModel.  # noqa: E501


        :return: The login of this ItemDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this ItemDTOModel.


        :param login: The login of this ItemDTOModel.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def new_state(self):
        """Gets the new_state of this ItemDTOModel.  # noqa: E501


        :return: The new_state of this ItemDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._new_state

    @new_state.setter
    def new_state(self, new_state):
        """Sets the new_state of this ItemDTOModel.


        :param new_state: The new_state of this ItemDTOModel.  # noqa: E501
        :type: str
        """

        self._new_state = new_state

    @property
    def panel_id(self):
        """Gets the panel_id of this ItemDTOModel.  # noqa: E501


        :return: The panel_id of this ItemDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._panel_id

    @panel_id.setter
    def panel_id(self, panel_id):
        """Sets the panel_id of this ItemDTOModel.


        :param panel_id: The panel_id of this ItemDTOModel.  # noqa: E501
        :type: int
        """

        self._panel_id = panel_id

    @property
    def prev_state(self):
        """Gets the prev_state of this ItemDTOModel.  # noqa: E501


        :return: The prev_state of this ItemDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._prev_state

    @prev_state.setter
    def prev_state(self, prev_state):
        """Sets the prev_state of this ItemDTOModel.


        :param prev_state: The prev_state of this ItemDTOModel.  # noqa: E501
        :type: str
        """

        self._prev_state = prev_state

    @property
    def tags(self):
        """Gets the tags of this ItemDTOModel.  # noqa: E501


        :return: The tags of this ItemDTOModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ItemDTOModel.


        :param tags: The tags of this ItemDTOModel.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def text(self):
        """Gets the text of this ItemDTOModel.  # noqa: E501


        :return: The text of this ItemDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ItemDTOModel.


        :param text: The text of this ItemDTOModel.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def time(self):
        """Gets the time of this ItemDTOModel.  # noqa: E501


        :return: The time of this ItemDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ItemDTOModel.


        :param time: The time of this ItemDTOModel.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def time_end(self):
        """Gets the time_end of this ItemDTOModel.  # noqa: E501


        :return: The time_end of this ItemDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """Sets the time_end of this ItemDTOModel.


        :param time_end: The time_end of this ItemDTOModel.  # noqa: E501
        :type: int
        """

        self._time_end = time_end

    @property
    def updated(self):
        """Gets the updated of this ItemDTOModel.  # noqa: E501


        :return: The updated of this ItemDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ItemDTOModel.


        :param updated: The updated of this ItemDTOModel.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def user_id(self):
        """Gets the user_id of this ItemDTOModel.  # noqa: E501


        :return: The user_id of this ItemDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ItemDTOModel.


        :param user_id: The user_id of this ItemDTOModel.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(ItemDTOModel, dict):
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
        if not isinstance(other, ItemDTOModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemDTOModel):
            return True

        return self.to_dict() != other.to_dict()