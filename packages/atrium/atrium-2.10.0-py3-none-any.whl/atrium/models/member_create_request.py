# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from atrium.models.credential_request import CredentialRequest  # noqa: F401,E501


class MemberCreateRequest(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'credentials': 'list[CredentialRequest]',
        'identifier': 'str',
        'institution_code': 'str',
        'metadata': 'str',
        'skip_aggregation': 'bool'
    }

    attribute_map = {
        'credentials': 'credentials',
        'identifier': 'identifier',
        'institution_code': 'institution_code',
        'metadata': 'metadata',
        'skip_aggregation': 'skip_aggregation'
    }

    def __init__(self, credentials=None, identifier=None, institution_code=None, metadata=None, skip_aggregation=None):  # noqa: E501

        self._credentials = None
        self._identifier = None
        self._institution_code = None
        self._metadata = None
        self._skip_aggregation = None
        self.discriminator = None

        self.credentials = credentials
        if identifier is not None:
            self.identifier = identifier
        self.institution_code = institution_code
        if metadata is not None:
            self.metadata = metadata
        if skip_aggregation is not None:
            self.skip_aggregation = skip_aggregation

    @property
    def credentials(self):
        """Gets the credentials of this MemberCreateRequest.  # noqa: E501


        :return: The credentials of this MemberCreateRequest.  # noqa: E501
        :rtype: list[CredentialRequest]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this MemberCreateRequest.


        :param credentials: The credentials of this MemberCreateRequest.  # noqa: E501
        :type: list[CredentialRequest]
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def identifier(self):
        """Gets the identifier of this MemberCreateRequest.  # noqa: E501


        :return: The identifier of this MemberCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this MemberCreateRequest.


        :param identifier: The identifier of this MemberCreateRequest.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def institution_code(self):
        """Gets the institution_code of this MemberCreateRequest.  # noqa: E501


        :return: The institution_code of this MemberCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._institution_code

    @institution_code.setter
    def institution_code(self, institution_code):
        """Sets the institution_code of this MemberCreateRequest.


        :param institution_code: The institution_code of this MemberCreateRequest.  # noqa: E501
        :type: str
        """
        if institution_code is None:
            raise ValueError("Invalid value for `institution_code`, must not be `None`")  # noqa: E501

        self._institution_code = institution_code

    @property
    def metadata(self):
        """Gets the metadata of this MemberCreateRequest.  # noqa: E501


        :return: The metadata of this MemberCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this MemberCreateRequest.


        :param metadata: The metadata of this MemberCreateRequest.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def skip_aggregation(self):
        """Gets the skip_aggregation of this MemberCreateRequest.  # noqa: E501


        :return: The skip_aggregation of this MemberCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._skip_aggregation

    @skip_aggregation.setter
    def skip_aggregation(self, skip_aggregation):
        """Sets the skip_aggregation of this MemberCreateRequest.


        :param skip_aggregation: The skip_aggregation of this MemberCreateRequest.  # noqa: E501
        :type: bool
        """

        self._skip_aggregation = skip_aggregation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.mx_types):
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
        if issubclass(MemberCreateRequest, dict):
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
        if not isinstance(other, MemberCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
