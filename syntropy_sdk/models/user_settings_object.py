# coding: utf-8

"""
    noia-controller

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class UserSettingsObject(object):
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
        "show_onboarding": "bool",
        "user_timezone": "str",
        "auth_sources": "list[AuthSource]",
    }

    attribute_map = {
        "show_onboarding": "show_onboarding",
        "user_timezone": "user_timezone",
        "auth_sources": "auth_sources",
    }

    def __init__(
        self, show_onboarding=None, user_timezone=None, auth_sources=None
    ):  # noqa: E501
        """UserSettingsObject - a model defined in Swagger"""  # noqa: E501
        self._show_onboarding = None
        self._user_timezone = None
        self._auth_sources = None
        self.discriminator = None
        if show_onboarding is not None:
            self.show_onboarding = show_onboarding
        if user_timezone is not None:
            self.user_timezone = user_timezone
        if auth_sources is not None:
            self.auth_sources = auth_sources

    @property
    def show_onboarding(self):
        """Gets the show_onboarding of this UserSettingsObject.  # noqa: E501


        :return: The show_onboarding of this UserSettingsObject.  # noqa: E501
        :rtype: bool
        """
        return self._show_onboarding

    @show_onboarding.setter
    def show_onboarding(self, show_onboarding):
        """Sets the show_onboarding of this UserSettingsObject.


        :param show_onboarding: The show_onboarding of this UserSettingsObject.  # noqa: E501
        :type: bool
        """

        self._show_onboarding = show_onboarding

    @property
    def user_timezone(self):
        """Gets the user_timezone of this UserSettingsObject.  # noqa: E501


        :return: The user_timezone of this UserSettingsObject.  # noqa: E501
        :rtype: str
        """
        return self._user_timezone

    @user_timezone.setter
    def user_timezone(self, user_timezone):
        """Sets the user_timezone of this UserSettingsObject.


        :param user_timezone: The user_timezone of this UserSettingsObject.  # noqa: E501
        :type: str
        """

        self._user_timezone = user_timezone

    @property
    def auth_sources(self):
        """Gets the auth_sources of this UserSettingsObject.  # noqa: E501


        :return: The auth_sources of this UserSettingsObject.  # noqa: E501
        :rtype: list[AuthSource]
        """
        return self._auth_sources

    @auth_sources.setter
    def auth_sources(self, auth_sources):
        """Sets the auth_sources of this UserSettingsObject.


        :param auth_sources: The auth_sources of this UserSettingsObject.  # noqa: E501
        :type: list[AuthSource]
        """

        self._auth_sources = auth_sources

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(UserSettingsObject, dict):
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
        if not isinstance(other, UserSettingsObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other