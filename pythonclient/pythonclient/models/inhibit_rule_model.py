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


class InhibitRuleModel(object):
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
        'equal': 'LabelNamesModel',
        'source_match': 'dict(str, str)',
        'source_match_re': 'MatchRegexpsModel',
        'source_matchers': 'MatchersModel',
        'target_match': 'dict(str, str)',
        'target_match_re': 'MatchRegexpsModel',
        'target_matchers': 'MatchersModel'
    }

    attribute_map = {
        'equal': 'equal',
        'source_match': 'source_match',
        'source_match_re': 'source_match_re',
        'source_matchers': 'source_matchers',
        'target_match': 'target_match',
        'target_match_re': 'target_match_re',
        'target_matchers': 'target_matchers'
    }

    def __init__(self, equal=None, source_match=None, source_match_re=None, source_matchers=None, target_match=None, target_match_re=None, target_matchers=None, _configuration=None):  # noqa: E501
        """InhibitRuleModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._equal = None
        self._source_match = None
        self._source_match_re = None
        self._source_matchers = None
        self._target_match = None
        self._target_match_re = None
        self._target_matchers = None
        self.discriminator = None

        if equal is not None:
            self.equal = equal
        if source_match is not None:
            self.source_match = source_match
        if source_match_re is not None:
            self.source_match_re = source_match_re
        if source_matchers is not None:
            self.source_matchers = source_matchers
        if target_match is not None:
            self.target_match = target_match
        if target_match_re is not None:
            self.target_match_re = target_match_re
        if target_matchers is not None:
            self.target_matchers = target_matchers

    @property
    def equal(self):
        """Gets the equal of this InhibitRuleModel.  # noqa: E501


        :return: The equal of this InhibitRuleModel.  # noqa: E501
        :rtype: LabelNamesModel
        """
        return self._equal

    @equal.setter
    def equal(self, equal):
        """Sets the equal of this InhibitRuleModel.


        :param equal: The equal of this InhibitRuleModel.  # noqa: E501
        :type: LabelNamesModel
        """

        self._equal = equal

    @property
    def source_match(self):
        """Gets the source_match of this InhibitRuleModel.  # noqa: E501

        SourceMatch defines a set of labels that have to equal the given value for source alerts. Deprecated. Remove before v1.0 release.  # noqa: E501

        :return: The source_match of this InhibitRuleModel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._source_match

    @source_match.setter
    def source_match(self, source_match):
        """Sets the source_match of this InhibitRuleModel.

        SourceMatch defines a set of labels that have to equal the given value for source alerts. Deprecated. Remove before v1.0 release.  # noqa: E501

        :param source_match: The source_match of this InhibitRuleModel.  # noqa: E501
        :type: dict(str, str)
        """

        self._source_match = source_match

    @property
    def source_match_re(self):
        """Gets the source_match_re of this InhibitRuleModel.  # noqa: E501


        :return: The source_match_re of this InhibitRuleModel.  # noqa: E501
        :rtype: MatchRegexpsModel
        """
        return self._source_match_re

    @source_match_re.setter
    def source_match_re(self, source_match_re):
        """Sets the source_match_re of this InhibitRuleModel.


        :param source_match_re: The source_match_re of this InhibitRuleModel.  # noqa: E501
        :type: MatchRegexpsModel
        """

        self._source_match_re = source_match_re

    @property
    def source_matchers(self):
        """Gets the source_matchers of this InhibitRuleModel.  # noqa: E501


        :return: The source_matchers of this InhibitRuleModel.  # noqa: E501
        :rtype: MatchersModel
        """
        return self._source_matchers

    @source_matchers.setter
    def source_matchers(self, source_matchers):
        """Sets the source_matchers of this InhibitRuleModel.


        :param source_matchers: The source_matchers of this InhibitRuleModel.  # noqa: E501
        :type: MatchersModel
        """

        self._source_matchers = source_matchers

    @property
    def target_match(self):
        """Gets the target_match of this InhibitRuleModel.  # noqa: E501

        TargetMatch defines a set of labels that have to equal the given value for target alerts. Deprecated. Remove before v1.0 release.  # noqa: E501

        :return: The target_match of this InhibitRuleModel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._target_match

    @target_match.setter
    def target_match(self, target_match):
        """Sets the target_match of this InhibitRuleModel.

        TargetMatch defines a set of labels that have to equal the given value for target alerts. Deprecated. Remove before v1.0 release.  # noqa: E501

        :param target_match: The target_match of this InhibitRuleModel.  # noqa: E501
        :type: dict(str, str)
        """

        self._target_match = target_match

    @property
    def target_match_re(self):
        """Gets the target_match_re of this InhibitRuleModel.  # noqa: E501


        :return: The target_match_re of this InhibitRuleModel.  # noqa: E501
        :rtype: MatchRegexpsModel
        """
        return self._target_match_re

    @target_match_re.setter
    def target_match_re(self, target_match_re):
        """Sets the target_match_re of this InhibitRuleModel.


        :param target_match_re: The target_match_re of this InhibitRuleModel.  # noqa: E501
        :type: MatchRegexpsModel
        """

        self._target_match_re = target_match_re

    @property
    def target_matchers(self):
        """Gets the target_matchers of this InhibitRuleModel.  # noqa: E501


        :return: The target_matchers of this InhibitRuleModel.  # noqa: E501
        :rtype: MatchersModel
        """
        return self._target_matchers

    @target_matchers.setter
    def target_matchers(self, target_matchers):
        """Sets the target_matchers of this InhibitRuleModel.


        :param target_matchers: The target_matchers of this InhibitRuleModel.  # noqa: E501
        :type: MatchersModel
        """

        self._target_matchers = target_matchers

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
        if issubclass(InhibitRuleModel, dict):
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
        if not isinstance(other, InhibitRuleModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InhibitRuleModel):
            return True

        return self.to_dict() != other.to_dict()