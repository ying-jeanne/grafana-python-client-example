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


class PatchLibraryElementCommandModel(object):
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
        'folder_id': 'int',
        'folder_uid': 'str',
        'kind': 'int',
        'model': 'object',
        'name': 'str',
        'uid': 'str',
        'version': 'int'
    }

    attribute_map = {
        'folder_id': 'folderId',
        'folder_uid': 'folderUid',
        'kind': 'kind',
        'model': 'model',
        'name': 'name',
        'uid': 'uid',
        'version': 'version'
    }

    def __init__(self, folder_id=None, folder_uid=None, kind=None, model=None, name=None, uid=None, version=None, _configuration=None):  # noqa: E501
        """PatchLibraryElementCommandModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._folder_id = None
        self._folder_uid = None
        self._kind = None
        self._model = None
        self._name = None
        self._uid = None
        self._version = None
        self.discriminator = None

        if folder_id is not None:
            self.folder_id = folder_id
        if folder_uid is not None:
            self.folder_uid = folder_uid
        if kind is not None:
            self.kind = kind
        if model is not None:
            self.model = model
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if version is not None:
            self.version = version

    @property
    def folder_id(self):
        """Gets the folder_id of this PatchLibraryElementCommandModel.  # noqa: E501

        ID of the folder where the library element is stored.  # noqa: E501

        :return: The folder_id of this PatchLibraryElementCommandModel.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this PatchLibraryElementCommandModel.

        ID of the folder where the library element is stored.  # noqa: E501

        :param folder_id: The folder_id of this PatchLibraryElementCommandModel.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def folder_uid(self):
        """Gets the folder_uid of this PatchLibraryElementCommandModel.  # noqa: E501

        UID of the folder where the library element is stored.  # noqa: E501

        :return: The folder_uid of this PatchLibraryElementCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._folder_uid

    @folder_uid.setter
    def folder_uid(self, folder_uid):
        """Sets the folder_uid of this PatchLibraryElementCommandModel.

        UID of the folder where the library element is stored.  # noqa: E501

        :param folder_uid: The folder_uid of this PatchLibraryElementCommandModel.  # noqa: E501
        :type: str
        """

        self._folder_uid = folder_uid

    @property
    def kind(self):
        """Gets the kind of this PatchLibraryElementCommandModel.  # noqa: E501

        Kind of element to create, Use 1 for library panels or 2 for c. Description: 1 - library panels 2 - library variables  # noqa: E501

        :return: The kind of this PatchLibraryElementCommandModel.  # noqa: E501
        :rtype: int
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PatchLibraryElementCommandModel.

        Kind of element to create, Use 1 for library panels or 2 for c. Description: 1 - library panels 2 - library variables  # noqa: E501

        :param kind: The kind of this PatchLibraryElementCommandModel.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if (self._configuration.client_side_validation and
                kind not in allowed_values):
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def model(self):
        """Gets the model of this PatchLibraryElementCommandModel.  # noqa: E501

        The JSON model for the library element.  # noqa: E501

        :return: The model of this PatchLibraryElementCommandModel.  # noqa: E501
        :rtype: object
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PatchLibraryElementCommandModel.

        The JSON model for the library element.  # noqa: E501

        :param model: The model of this PatchLibraryElementCommandModel.  # noqa: E501
        :type: object
        """

        self._model = model

    @property
    def name(self):
        """Gets the name of this PatchLibraryElementCommandModel.  # noqa: E501

        Name of the library element.  # noqa: E501

        :return: The name of this PatchLibraryElementCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchLibraryElementCommandModel.

        Name of the library element.  # noqa: E501

        :param name: The name of this PatchLibraryElementCommandModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uid(self):
        """Gets the uid of this PatchLibraryElementCommandModel.  # noqa: E501


        :return: The uid of this PatchLibraryElementCommandModel.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this PatchLibraryElementCommandModel.


        :param uid: The uid of this PatchLibraryElementCommandModel.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def version(self):
        """Gets the version of this PatchLibraryElementCommandModel.  # noqa: E501

        Version of the library element you are updating.  # noqa: E501

        :return: The version of this PatchLibraryElementCommandModel.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PatchLibraryElementCommandModel.

        Version of the library element you are updating.  # noqa: E501

        :param version: The version of this PatchLibraryElementCommandModel.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(PatchLibraryElementCommandModel, dict):
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
        if not isinstance(other, PatchLibraryElementCommandModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchLibraryElementCommandModel):
            return True

        return self.to_dict() != other.to_dict()
