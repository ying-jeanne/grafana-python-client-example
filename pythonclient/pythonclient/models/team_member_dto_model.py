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


class TeamMemberDTOModel(object):
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
        'auth_module': 'str',
        'avatar_url': 'str',
        'email': 'str',
        'labels': 'list[str]',
        'login': 'str',
        'name': 'str',
        'org_id': 'int',
        'permission': 'PermissionTypeModel',
        'team_id': 'int',
        'user_id': 'int'
    }

    attribute_map = {
        'auth_module': 'auth_module',
        'avatar_url': 'avatarUrl',
        'email': 'email',
        'labels': 'labels',
        'login': 'login',
        'name': 'name',
        'org_id': 'orgId',
        'permission': 'permission',
        'team_id': 'teamId',
        'user_id': 'userId'
    }

    def __init__(self, auth_module=None, avatar_url=None, email=None, labels=None, login=None, name=None, org_id=None, permission=None, team_id=None, user_id=None, _configuration=None):  # noqa: E501
        """TeamMemberDTOModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_module = None
        self._avatar_url = None
        self._email = None
        self._labels = None
        self._login = None
        self._name = None
        self._org_id = None
        self._permission = None
        self._team_id = None
        self._user_id = None
        self.discriminator = None

        if auth_module is not None:
            self.auth_module = auth_module
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if email is not None:
            self.email = email
        if labels is not None:
            self.labels = labels
        if login is not None:
            self.login = login
        if name is not None:
            self.name = name
        if org_id is not None:
            self.org_id = org_id
        if permission is not None:
            self.permission = permission
        if team_id is not None:
            self.team_id = team_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def auth_module(self):
        """Gets the auth_module of this TeamMemberDTOModel.  # noqa: E501


        :return: The auth_module of this TeamMemberDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._auth_module

    @auth_module.setter
    def auth_module(self, auth_module):
        """Sets the auth_module of this TeamMemberDTOModel.


        :param auth_module: The auth_module of this TeamMemberDTOModel.  # noqa: E501
        :type: str
        """

        self._auth_module = auth_module

    @property
    def avatar_url(self):
        """Gets the avatar_url of this TeamMemberDTOModel.  # noqa: E501


        :return: The avatar_url of this TeamMemberDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this TeamMemberDTOModel.


        :param avatar_url: The avatar_url of this TeamMemberDTOModel.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def email(self):
        """Gets the email of this TeamMemberDTOModel.  # noqa: E501


        :return: The email of this TeamMemberDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TeamMemberDTOModel.


        :param email: The email of this TeamMemberDTOModel.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def labels(self):
        """Gets the labels of this TeamMemberDTOModel.  # noqa: E501


        :return: The labels of this TeamMemberDTOModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this TeamMemberDTOModel.


        :param labels: The labels of this TeamMemberDTOModel.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def login(self):
        """Gets the login of this TeamMemberDTOModel.  # noqa: E501


        :return: The login of this TeamMemberDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this TeamMemberDTOModel.


        :param login: The login of this TeamMemberDTOModel.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def name(self):
        """Gets the name of this TeamMemberDTOModel.  # noqa: E501


        :return: The name of this TeamMemberDTOModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamMemberDTOModel.


        :param name: The name of this TeamMemberDTOModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this TeamMemberDTOModel.  # noqa: E501


        :return: The org_id of this TeamMemberDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this TeamMemberDTOModel.


        :param org_id: The org_id of this TeamMemberDTOModel.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def permission(self):
        """Gets the permission of this TeamMemberDTOModel.  # noqa: E501


        :return: The permission of this TeamMemberDTOModel.  # noqa: E501
        :rtype: PermissionTypeModel
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this TeamMemberDTOModel.


        :param permission: The permission of this TeamMemberDTOModel.  # noqa: E501
        :type: PermissionTypeModel
        """

        self._permission = permission

    @property
    def team_id(self):
        """Gets the team_id of this TeamMemberDTOModel.  # noqa: E501


        :return: The team_id of this TeamMemberDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this TeamMemberDTOModel.


        :param team_id: The team_id of this TeamMemberDTOModel.  # noqa: E501
        :type: int
        """

        self._team_id = team_id

    @property
    def user_id(self):
        """Gets the user_id of this TeamMemberDTOModel.  # noqa: E501


        :return: The user_id of this TeamMemberDTOModel.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TeamMemberDTOModel.


        :param user_id: The user_id of this TeamMemberDTOModel.  # noqa: E501
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
        if issubclass(TeamMemberDTOModel, dict):
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
        if not isinstance(other, TeamMemberDTOModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamMemberDTOModel):
            return True

        return self.to_dict() != other.to_dict()
