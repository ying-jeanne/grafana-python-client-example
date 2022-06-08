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


class URLModel(object):
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
        'force_query': 'bool',
        'fragment': 'str',
        'host': 'str',
        'opaque': 'str',
        'path': 'str',
        'raw_fragment': 'str',
        'raw_path': 'str',
        'raw_query': 'str',
        'scheme': 'str',
        'user': 'UserinfoModel'
    }

    attribute_map = {
        'force_query': 'ForceQuery',
        'fragment': 'Fragment',
        'host': 'Host',
        'opaque': 'Opaque',
        'path': 'Path',
        'raw_fragment': 'RawFragment',
        'raw_path': 'RawPath',
        'raw_query': 'RawQuery',
        'scheme': 'Scheme',
        'user': 'User'
    }

    def __init__(self, force_query=None, fragment=None, host=None, opaque=None, path=None, raw_fragment=None, raw_path=None, raw_query=None, scheme=None, user=None, _configuration=None):  # noqa: E501
        """URLModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._force_query = None
        self._fragment = None
        self._host = None
        self._opaque = None
        self._path = None
        self._raw_fragment = None
        self._raw_path = None
        self._raw_query = None
        self._scheme = None
        self._user = None
        self.discriminator = None

        if force_query is not None:
            self.force_query = force_query
        if fragment is not None:
            self.fragment = fragment
        if host is not None:
            self.host = host
        if opaque is not None:
            self.opaque = opaque
        if path is not None:
            self.path = path
        if raw_fragment is not None:
            self.raw_fragment = raw_fragment
        if raw_path is not None:
            self.raw_path = raw_path
        if raw_query is not None:
            self.raw_query = raw_query
        if scheme is not None:
            self.scheme = scheme
        if user is not None:
            self.user = user

    @property
    def force_query(self):
        """Gets the force_query of this URLModel.  # noqa: E501


        :return: The force_query of this URLModel.  # noqa: E501
        :rtype: bool
        """
        return self._force_query

    @force_query.setter
    def force_query(self, force_query):
        """Sets the force_query of this URLModel.


        :param force_query: The force_query of this URLModel.  # noqa: E501
        :type: bool
        """

        self._force_query = force_query

    @property
    def fragment(self):
        """Gets the fragment of this URLModel.  # noqa: E501


        :return: The fragment of this URLModel.  # noqa: E501
        :rtype: str
        """
        return self._fragment

    @fragment.setter
    def fragment(self, fragment):
        """Sets the fragment of this URLModel.


        :param fragment: The fragment of this URLModel.  # noqa: E501
        :type: str
        """

        self._fragment = fragment

    @property
    def host(self):
        """Gets the host of this URLModel.  # noqa: E501


        :return: The host of this URLModel.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this URLModel.


        :param host: The host of this URLModel.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def opaque(self):
        """Gets the opaque of this URLModel.  # noqa: E501


        :return: The opaque of this URLModel.  # noqa: E501
        :rtype: str
        """
        return self._opaque

    @opaque.setter
    def opaque(self, opaque):
        """Sets the opaque of this URLModel.


        :param opaque: The opaque of this URLModel.  # noqa: E501
        :type: str
        """

        self._opaque = opaque

    @property
    def path(self):
        """Gets the path of this URLModel.  # noqa: E501


        :return: The path of this URLModel.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this URLModel.


        :param path: The path of this URLModel.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def raw_fragment(self):
        """Gets the raw_fragment of this URLModel.  # noqa: E501


        :return: The raw_fragment of this URLModel.  # noqa: E501
        :rtype: str
        """
        return self._raw_fragment

    @raw_fragment.setter
    def raw_fragment(self, raw_fragment):
        """Sets the raw_fragment of this URLModel.


        :param raw_fragment: The raw_fragment of this URLModel.  # noqa: E501
        :type: str
        """

        self._raw_fragment = raw_fragment

    @property
    def raw_path(self):
        """Gets the raw_path of this URLModel.  # noqa: E501


        :return: The raw_path of this URLModel.  # noqa: E501
        :rtype: str
        """
        return self._raw_path

    @raw_path.setter
    def raw_path(self, raw_path):
        """Sets the raw_path of this URLModel.


        :param raw_path: The raw_path of this URLModel.  # noqa: E501
        :type: str
        """

        self._raw_path = raw_path

    @property
    def raw_query(self):
        """Gets the raw_query of this URLModel.  # noqa: E501


        :return: The raw_query of this URLModel.  # noqa: E501
        :rtype: str
        """
        return self._raw_query

    @raw_query.setter
    def raw_query(self, raw_query):
        """Sets the raw_query of this URLModel.


        :param raw_query: The raw_query of this URLModel.  # noqa: E501
        :type: str
        """

        self._raw_query = raw_query

    @property
    def scheme(self):
        """Gets the scheme of this URLModel.  # noqa: E501


        :return: The scheme of this URLModel.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this URLModel.


        :param scheme: The scheme of this URLModel.  # noqa: E501
        :type: str
        """

        self._scheme = scheme

    @property
    def user(self):
        """Gets the user of this URLModel.  # noqa: E501


        :return: The user of this URLModel.  # noqa: E501
        :rtype: UserinfoModel
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this URLModel.


        :param user: The user of this URLModel.  # noqa: E501
        :type: UserinfoModel
        """

        self._user = user

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
        if issubclass(URLModel, dict):
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
        if not isinstance(other, URLModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, URLModel):
            return True

        return self.to_dict() != other.to_dict()
