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


class PostableSilenceModel(object):
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
        'comment': 'str',
        'created_by': 'str',
        'ends_at': 'datetime',
        'id': 'str',
        'matchers': 'MatchersModel',
        'starts_at': 'datetime'
    }

    attribute_map = {
        'comment': 'comment',
        'created_by': 'createdBy',
        'ends_at': 'endsAt',
        'id': 'id',
        'matchers': 'matchers',
        'starts_at': 'startsAt'
    }

    def __init__(self, comment=None, created_by=None, ends_at=None, id=None, matchers=None, starts_at=None, _configuration=None):  # noqa: E501
        """PostableSilenceModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._comment = None
        self._created_by = None
        self._ends_at = None
        self._id = None
        self._matchers = None
        self._starts_at = None
        self.discriminator = None

        self.comment = comment
        self.created_by = created_by
        self.ends_at = ends_at
        if id is not None:
            self.id = id
        self.matchers = matchers
        self.starts_at = starts_at

    @property
    def comment(self):
        """Gets the comment of this PostableSilenceModel.  # noqa: E501

        comment  # noqa: E501

        :return: The comment of this PostableSilenceModel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PostableSilenceModel.

        comment  # noqa: E501

        :param comment: The comment of this PostableSilenceModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

    @property
    def created_by(self):
        """Gets the created_by of this PostableSilenceModel.  # noqa: E501

        created by  # noqa: E501

        :return: The created_by of this PostableSilenceModel.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this PostableSilenceModel.

        created by  # noqa: E501

        :param created_by: The created_by of this PostableSilenceModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def ends_at(self):
        """Gets the ends_at of this PostableSilenceModel.  # noqa: E501

        ends at  # noqa: E501

        :return: The ends_at of this PostableSilenceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this PostableSilenceModel.

        ends at  # noqa: E501

        :param ends_at: The ends_at of this PostableSilenceModel.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and ends_at is None:
            raise ValueError("Invalid value for `ends_at`, must not be `None`")  # noqa: E501

        self._ends_at = ends_at

    @property
    def id(self):
        """Gets the id of this PostableSilenceModel.  # noqa: E501

        id  # noqa: E501

        :return: The id of this PostableSilenceModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PostableSilenceModel.

        id  # noqa: E501

        :param id: The id of this PostableSilenceModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def matchers(self):
        """Gets the matchers of this PostableSilenceModel.  # noqa: E501


        :return: The matchers of this PostableSilenceModel.  # noqa: E501
        :rtype: MatchersModel
        """
        return self._matchers

    @matchers.setter
    def matchers(self, matchers):
        """Sets the matchers of this PostableSilenceModel.


        :param matchers: The matchers of this PostableSilenceModel.  # noqa: E501
        :type: MatchersModel
        """
        if self._configuration.client_side_validation and matchers is None:
            raise ValueError("Invalid value for `matchers`, must not be `None`")  # noqa: E501

        self._matchers = matchers

    @property
    def starts_at(self):
        """Gets the starts_at of this PostableSilenceModel.  # noqa: E501

        starts at  # noqa: E501

        :return: The starts_at of this PostableSilenceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """Sets the starts_at of this PostableSilenceModel.

        starts at  # noqa: E501

        :param starts_at: The starts_at of this PostableSilenceModel.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and starts_at is None:
            raise ValueError("Invalid value for `starts_at`, must not be `None`")  # noqa: E501

        self._starts_at = starts_at

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
        if issubclass(PostableSilenceModel, dict):
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
        if not isinstance(other, PostableSilenceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostableSilenceModel):
            return True

        return self.to_dict() != other.to_dict()
