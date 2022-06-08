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


class TokenModel(object):
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
        'account': 'str',
        'company': 'str',
        'details_url': 'str',
        'exp': 'int',
        'iat': 'int',
        'included_users': 'int',
        'iss': 'str',
        'jti': 'str',
        'lexp': 'int',
        'lic_exp_warn_days': 'int',
        'lid': 'str',
        'limit_by': 'str',
        'max_concurrent_user_sessions': 'int',
        'nbf': 'int',
        'prod': 'list[str]',
        'slug': 'str',
        'status': 'TokenStatusModel',
        'sub': 'str',
        'tok_exp_warn_days': 'int',
        'trial': 'bool',
        'trial_exp': 'int',
        'update_days': 'int',
        'usage_billing': 'bool'
    }

    attribute_map = {
        'account': 'account',
        'company': 'company',
        'details_url': 'details_url',
        'exp': 'exp',
        'iat': 'iat',
        'included_users': 'included_users',
        'iss': 'iss',
        'jti': 'jti',
        'lexp': 'lexp',
        'lic_exp_warn_days': 'lic_exp_warn_days',
        'lid': 'lid',
        'limit_by': 'limit_by',
        'max_concurrent_user_sessions': 'max_concurrent_user_sessions',
        'nbf': 'nbf',
        'prod': 'prod',
        'slug': 'slug',
        'status': 'status',
        'sub': 'sub',
        'tok_exp_warn_days': 'tok_exp_warn_days',
        'trial': 'trial',
        'trial_exp': 'trial_exp',
        'update_days': 'update_days',
        'usage_billing': 'usage_billing'
    }

    def __init__(self, account=None, company=None, details_url=None, exp=None, iat=None, included_users=None, iss=None, jti=None, lexp=None, lic_exp_warn_days=None, lid=None, limit_by=None, max_concurrent_user_sessions=None, nbf=None, prod=None, slug=None, status=None, sub=None, tok_exp_warn_days=None, trial=None, trial_exp=None, update_days=None, usage_billing=None, _configuration=None):  # noqa: E501
        """TokenModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account = None
        self._company = None
        self._details_url = None
        self._exp = None
        self._iat = None
        self._included_users = None
        self._iss = None
        self._jti = None
        self._lexp = None
        self._lic_exp_warn_days = None
        self._lid = None
        self._limit_by = None
        self._max_concurrent_user_sessions = None
        self._nbf = None
        self._prod = None
        self._slug = None
        self._status = None
        self._sub = None
        self._tok_exp_warn_days = None
        self._trial = None
        self._trial_exp = None
        self._update_days = None
        self._usage_billing = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if company is not None:
            self.company = company
        if details_url is not None:
            self.details_url = details_url
        if exp is not None:
            self.exp = exp
        if iat is not None:
            self.iat = iat
        if included_users is not None:
            self.included_users = included_users
        if iss is not None:
            self.iss = iss
        if jti is not None:
            self.jti = jti
        if lexp is not None:
            self.lexp = lexp
        if lic_exp_warn_days is not None:
            self.lic_exp_warn_days = lic_exp_warn_days
        if lid is not None:
            self.lid = lid
        if limit_by is not None:
            self.limit_by = limit_by
        if max_concurrent_user_sessions is not None:
            self.max_concurrent_user_sessions = max_concurrent_user_sessions
        if nbf is not None:
            self.nbf = nbf
        if prod is not None:
            self.prod = prod
        if slug is not None:
            self.slug = slug
        if status is not None:
            self.status = status
        if sub is not None:
            self.sub = sub
        if tok_exp_warn_days is not None:
            self.tok_exp_warn_days = tok_exp_warn_days
        if trial is not None:
            self.trial = trial
        if trial_exp is not None:
            self.trial_exp = trial_exp
        if update_days is not None:
            self.update_days = update_days
        if usage_billing is not None:
            self.usage_billing = usage_billing

    @property
    def account(self):
        """Gets the account of this TokenModel.  # noqa: E501


        :return: The account of this TokenModel.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this TokenModel.


        :param account: The account of this TokenModel.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def company(self):
        """Gets the company of this TokenModel.  # noqa: E501


        :return: The company of this TokenModel.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this TokenModel.


        :param company: The company of this TokenModel.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def details_url(self):
        """Gets the details_url of this TokenModel.  # noqa: E501


        :return: The details_url of this TokenModel.  # noqa: E501
        :rtype: str
        """
        return self._details_url

    @details_url.setter
    def details_url(self, details_url):
        """Sets the details_url of this TokenModel.


        :param details_url: The details_url of this TokenModel.  # noqa: E501
        :type: str
        """

        self._details_url = details_url

    @property
    def exp(self):
        """Gets the exp of this TokenModel.  # noqa: E501


        :return: The exp of this TokenModel.  # noqa: E501
        :rtype: int
        """
        return self._exp

    @exp.setter
    def exp(self, exp):
        """Sets the exp of this TokenModel.


        :param exp: The exp of this TokenModel.  # noqa: E501
        :type: int
        """

        self._exp = exp

    @property
    def iat(self):
        """Gets the iat of this TokenModel.  # noqa: E501


        :return: The iat of this TokenModel.  # noqa: E501
        :rtype: int
        """
        return self._iat

    @iat.setter
    def iat(self, iat):
        """Sets the iat of this TokenModel.


        :param iat: The iat of this TokenModel.  # noqa: E501
        :type: int
        """

        self._iat = iat

    @property
    def included_users(self):
        """Gets the included_users of this TokenModel.  # noqa: E501


        :return: The included_users of this TokenModel.  # noqa: E501
        :rtype: int
        """
        return self._included_users

    @included_users.setter
    def included_users(self, included_users):
        """Sets the included_users of this TokenModel.


        :param included_users: The included_users of this TokenModel.  # noqa: E501
        :type: int
        """

        self._included_users = included_users

    @property
    def iss(self):
        """Gets the iss of this TokenModel.  # noqa: E501


        :return: The iss of this TokenModel.  # noqa: E501
        :rtype: str
        """
        return self._iss

    @iss.setter
    def iss(self, iss):
        """Sets the iss of this TokenModel.


        :param iss: The iss of this TokenModel.  # noqa: E501
        :type: str
        """

        self._iss = iss

    @property
    def jti(self):
        """Gets the jti of this TokenModel.  # noqa: E501


        :return: The jti of this TokenModel.  # noqa: E501
        :rtype: str
        """
        return self._jti

    @jti.setter
    def jti(self, jti):
        """Sets the jti of this TokenModel.


        :param jti: The jti of this TokenModel.  # noqa: E501
        :type: str
        """

        self._jti = jti

    @property
    def lexp(self):
        """Gets the lexp of this TokenModel.  # noqa: E501


        :return: The lexp of this TokenModel.  # noqa: E501
        :rtype: int
        """
        return self._lexp

    @lexp.setter
    def lexp(self, lexp):
        """Sets the lexp of this TokenModel.


        :param lexp: The lexp of this TokenModel.  # noqa: E501
        :type: int
        """

        self._lexp = lexp

    @property
    def lic_exp_warn_days(self):
        """Gets the lic_exp_warn_days of this TokenModel.  # noqa: E501


        :return: The lic_exp_warn_days of this TokenModel.  # noqa: E501
        :rtype: int
        """
        return self._lic_exp_warn_days

    @lic_exp_warn_days.setter
    def lic_exp_warn_days(self, lic_exp_warn_days):
        """Sets the lic_exp_warn_days of this TokenModel.


        :param lic_exp_warn_days: The lic_exp_warn_days of this TokenModel.  # noqa: E501
        :type: int
        """

        self._lic_exp_warn_days = lic_exp_warn_days

    @property
    def lid(self):
        """Gets the lid of this TokenModel.  # noqa: E501


        :return: The lid of this TokenModel.  # noqa: E501
        :rtype: str
        """
        return self._lid

    @lid.setter
    def lid(self, lid):
        """Sets the lid of this TokenModel.


        :param lid: The lid of this TokenModel.  # noqa: E501
        :type: str
        """

        self._lid = lid

    @property
    def limit_by(self):
        """Gets the limit_by of this TokenModel.  # noqa: E501


        :return: The limit_by of this TokenModel.  # noqa: E501
        :rtype: str
        """
        return self._limit_by

    @limit_by.setter
    def limit_by(self, limit_by):
        """Sets the limit_by of this TokenModel.


        :param limit_by: The limit_by of this TokenModel.  # noqa: E501
        :type: str
        """

        self._limit_by = limit_by

    @property
    def max_concurrent_user_sessions(self):
        """Gets the max_concurrent_user_sessions of this TokenModel.  # noqa: E501


        :return: The max_concurrent_user_sessions of this TokenModel.  # noqa: E501
        :rtype: int
        """
        return self._max_concurrent_user_sessions

    @max_concurrent_user_sessions.setter
    def max_concurrent_user_sessions(self, max_concurrent_user_sessions):
        """Sets the max_concurrent_user_sessions of this TokenModel.


        :param max_concurrent_user_sessions: The max_concurrent_user_sessions of this TokenModel.  # noqa: E501
        :type: int
        """

        self._max_concurrent_user_sessions = max_concurrent_user_sessions

    @property
    def nbf(self):
        """Gets the nbf of this TokenModel.  # noqa: E501


        :return: The nbf of this TokenModel.  # noqa: E501
        :rtype: int
        """
        return self._nbf

    @nbf.setter
    def nbf(self, nbf):
        """Sets the nbf of this TokenModel.


        :param nbf: The nbf of this TokenModel.  # noqa: E501
        :type: int
        """

        self._nbf = nbf

    @property
    def prod(self):
        """Gets the prod of this TokenModel.  # noqa: E501


        :return: The prod of this TokenModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._prod

    @prod.setter
    def prod(self, prod):
        """Sets the prod of this TokenModel.


        :param prod: The prod of this TokenModel.  # noqa: E501
        :type: list[str]
        """

        self._prod = prod

    @property
    def slug(self):
        """Gets the slug of this TokenModel.  # noqa: E501


        :return: The slug of this TokenModel.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this TokenModel.


        :param slug: The slug of this TokenModel.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def status(self):
        """Gets the status of this TokenModel.  # noqa: E501


        :return: The status of this TokenModel.  # noqa: E501
        :rtype: TokenStatusModel
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TokenModel.


        :param status: The status of this TokenModel.  # noqa: E501
        :type: TokenStatusModel
        """

        self._status = status

    @property
    def sub(self):
        """Gets the sub of this TokenModel.  # noqa: E501


        :return: The sub of this TokenModel.  # noqa: E501
        :rtype: str
        """
        return self._sub

    @sub.setter
    def sub(self, sub):
        """Sets the sub of this TokenModel.


        :param sub: The sub of this TokenModel.  # noqa: E501
        :type: str
        """

        self._sub = sub

    @property
    def tok_exp_warn_days(self):
        """Gets the tok_exp_warn_days of this TokenModel.  # noqa: E501


        :return: The tok_exp_warn_days of this TokenModel.  # noqa: E501
        :rtype: int
        """
        return self._tok_exp_warn_days

    @tok_exp_warn_days.setter
    def tok_exp_warn_days(self, tok_exp_warn_days):
        """Sets the tok_exp_warn_days of this TokenModel.


        :param tok_exp_warn_days: The tok_exp_warn_days of this TokenModel.  # noqa: E501
        :type: int
        """

        self._tok_exp_warn_days = tok_exp_warn_days

    @property
    def trial(self):
        """Gets the trial of this TokenModel.  # noqa: E501


        :return: The trial of this TokenModel.  # noqa: E501
        :rtype: bool
        """
        return self._trial

    @trial.setter
    def trial(self, trial):
        """Sets the trial of this TokenModel.


        :param trial: The trial of this TokenModel.  # noqa: E501
        :type: bool
        """

        self._trial = trial

    @property
    def trial_exp(self):
        """Gets the trial_exp of this TokenModel.  # noqa: E501


        :return: The trial_exp of this TokenModel.  # noqa: E501
        :rtype: int
        """
        return self._trial_exp

    @trial_exp.setter
    def trial_exp(self, trial_exp):
        """Sets the trial_exp of this TokenModel.


        :param trial_exp: The trial_exp of this TokenModel.  # noqa: E501
        :type: int
        """

        self._trial_exp = trial_exp

    @property
    def update_days(self):
        """Gets the update_days of this TokenModel.  # noqa: E501


        :return: The update_days of this TokenModel.  # noqa: E501
        :rtype: int
        """
        return self._update_days

    @update_days.setter
    def update_days(self, update_days):
        """Sets the update_days of this TokenModel.


        :param update_days: The update_days of this TokenModel.  # noqa: E501
        :type: int
        """

        self._update_days = update_days

    @property
    def usage_billing(self):
        """Gets the usage_billing of this TokenModel.  # noqa: E501


        :return: The usage_billing of this TokenModel.  # noqa: E501
        :rtype: bool
        """
        return self._usage_billing

    @usage_billing.setter
    def usage_billing(self, usage_billing):
        """Sets the usage_billing of this TokenModel.


        :param usage_billing: The usage_billing of this TokenModel.  # noqa: E501
        :type: bool
        """

        self._usage_billing = usage_billing

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
        if issubclass(TokenModel, dict):
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
        if not isinstance(other, TokenModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenModel):
            return True

        return self.to_dict() != other.to_dict()
