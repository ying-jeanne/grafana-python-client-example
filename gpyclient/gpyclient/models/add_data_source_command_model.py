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


class AddDataSourceCommandModel(object):
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
        'access': 'DsAccessModel',
        'basic_auth': 'bool',
        'basic_auth_password': 'str',
        'basic_auth_user': 'str',
        'database': 'str',
        'is_default': 'bool',
        'json_data': 'JsonModel',
        'name': 'str',
        'password': 'str',
        'secure_json_data': 'dict(str, str)',
        'type': 'str',
        'uid': 'str',
        'url': 'str',
        'user': 'str',
        'with_credentials': 'bool'
    }

    attribute_map = {
        'access': 'access',
        'basic_auth': 'basicAuth',
        'basic_auth_password': 'basicAuthPassword',
        'basic_auth_user': 'basicAuthUser',
        'database': 'database',
        'is_default': 'isDefault',
        'json_data': 'jsonData',
        'name': 'name',
        'password': 'password',
        'secure_json_data': 'secureJsonData',
        'type': 'type',
        'uid': 'uid',
        'url': 'url',
        'user': 'user',
        'with_credentials': 'withCredentials'
    }

    def __init__(self, access=None, basic_auth=None, basic_auth_password=None, basic_auth_user=None, database=None, is_default=None, json_data=None, name=None, password=None, secure_json_data=None, type=None, uid=None, url=None, user=None, with_credentials=None, _configuration=None):  # noqa: E501
        """AddDataSourceCommandModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access = None
        self._basic_auth = None
        self._basic_auth_password = None
        self._basic_auth_user = None
        self._database = None
        self._is_default = None
        self._json_data = None
        self._name = None
        self._password = None
        self._secure_json_data = None
        self._type = None
        self._uid = None
        self._url = None
        self._user = None
        self._with_credentials = None
        self.discriminator = None

        if access is not None:
            self.access = access
        if basic_auth is not None:
            self.basic_auth = basic_auth
        if basic_auth_password is not None:
            self.basic_auth_password = basic_auth_password
        if basic_auth_user is not None:
            self.basic_auth_user = basic_auth_user
        if database is not None:
            self.database = database
        if is_default is not None:
            self.is_default = is_default
        if json_data is not None:
            self.json_data = json_data
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password
        if secure_json_data is not None:
            self.secure_json_data = secure_json_data
        if type is not None:
            self.type = type
        if uid is not None:
            self.uid = uid
        if url is not None:
            self.url = url
        if user is not None:
            self.user = user
        if with_credentials is not None:
            self.with_credentials = with_credentials

    @property
    def access(self):
        """Gets the access of this AddDataSourceCommandModel.  # noqa: E501


        :return: The access of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: DsAccessModel
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this AddDataSourceCommandModel.


        :param access: The access of this AddDataSourceCommandModel.  # noqa: E501
        :type: DsAccessModel
        """

        self._access = access

    @property
    def basic_auth(self):
        """Gets the basic_auth of this AddDataSourceCommandModel.  # noqa: E501


        :return: The basic_auth of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: bool
        """
        return self._basic_auth

    @basic_auth.setter
    def basic_auth(self, basic_auth):
        """Sets the basic_auth of this AddDataSourceCommandModel.


        :param basic_auth: The basic_auth of this AddDataSourceCommandModel.  # noqa: E501
        :type: bool
        """

        self._basic_auth = basic_auth

    @property
    def basic_auth_password(self):
        """Gets the basic_auth_password of this AddDataSourceCommandModel.  # noqa: E501


        :return: The basic_auth_password of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._basic_auth_password

    @basic_auth_password.setter
    def basic_auth_password(self, basic_auth_password):
        """Sets the basic_auth_password of this AddDataSourceCommandModel.


        :param basic_auth_password: The basic_auth_password of this AddDataSourceCommandModel.  # noqa: E501
        :type: str
        """

        self._basic_auth_password = basic_auth_password

    @property
    def basic_auth_user(self):
        """Gets the basic_auth_user of this AddDataSourceCommandModel.  # noqa: E501


        :return: The basic_auth_user of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._basic_auth_user

    @basic_auth_user.setter
    def basic_auth_user(self, basic_auth_user):
        """Sets the basic_auth_user of this AddDataSourceCommandModel.


        :param basic_auth_user: The basic_auth_user of this AddDataSourceCommandModel.  # noqa: E501
        :type: str
        """

        self._basic_auth_user = basic_auth_user

    @property
    def database(self):
        """Gets the database of this AddDataSourceCommandModel.  # noqa: E501


        :return: The database of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this AddDataSourceCommandModel.


        :param database: The database of this AddDataSourceCommandModel.  # noqa: E501
        :type: str
        """

        self._database = database

    @property
    def is_default(self):
        """Gets the is_default of this AddDataSourceCommandModel.  # noqa: E501


        :return: The is_default of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this AddDataSourceCommandModel.


        :param is_default: The is_default of this AddDataSourceCommandModel.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def json_data(self):
        """Gets the json_data of this AddDataSourceCommandModel.  # noqa: E501


        :return: The json_data of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: JsonModel
        """
        return self._json_data

    @json_data.setter
    def json_data(self, json_data):
        """Sets the json_data of this AddDataSourceCommandModel.


        :param json_data: The json_data of this AddDataSourceCommandModel.  # noqa: E501
        :type: JsonModel
        """

        self._json_data = json_data

    @property
    def name(self):
        """Gets the name of this AddDataSourceCommandModel.  # noqa: E501


        :return: The name of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddDataSourceCommandModel.


        :param name: The name of this AddDataSourceCommandModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def password(self):
        """Gets the password of this AddDataSourceCommandModel.  # noqa: E501


        :return: The password of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AddDataSourceCommandModel.


        :param password: The password of this AddDataSourceCommandModel.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def secure_json_data(self):
        """Gets the secure_json_data of this AddDataSourceCommandModel.  # noqa: E501


        :return: The secure_json_data of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._secure_json_data

    @secure_json_data.setter
    def secure_json_data(self, secure_json_data):
        """Sets the secure_json_data of this AddDataSourceCommandModel.


        :param secure_json_data: The secure_json_data of this AddDataSourceCommandModel.  # noqa: E501
        :type: dict(str, str)
        """

        self._secure_json_data = secure_json_data

    @property
    def type(self):
        """Gets the type of this AddDataSourceCommandModel.  # noqa: E501


        :return: The type of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddDataSourceCommandModel.


        :param type: The type of this AddDataSourceCommandModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this AddDataSourceCommandModel.  # noqa: E501


        :return: The uid of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AddDataSourceCommandModel.


        :param uid: The uid of this AddDataSourceCommandModel.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def url(self):
        """Gets the url of this AddDataSourceCommandModel.  # noqa: E501


        :return: The url of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AddDataSourceCommandModel.


        :param url: The url of this AddDataSourceCommandModel.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user(self):
        """Gets the user of this AddDataSourceCommandModel.  # noqa: E501


        :return: The user of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AddDataSourceCommandModel.


        :param user: The user of this AddDataSourceCommandModel.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def with_credentials(self):
        """Gets the with_credentials of this AddDataSourceCommandModel.  # noqa: E501


        :return: The with_credentials of this AddDataSourceCommandModel.  # noqa: E501
        :rtype: bool
        """
        return self._with_credentials

    @with_credentials.setter
    def with_credentials(self, with_credentials):
        """Sets the with_credentials of this AddDataSourceCommandModel.


        :param with_credentials: The with_credentials of this AddDataSourceCommandModel.  # noqa: E501
        :type: bool
        """

        self._with_credentials = with_credentials

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
        if issubclass(AddDataSourceCommandModel, dict):
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
        if not isinstance(other, AddDataSourceCommandModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddDataSourceCommandModel):
            return True

        return self.to_dict() != other.to_dict()
