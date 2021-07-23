# coding: utf-8

"""
    syntropy-controller

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from syntropy_sdk.models.agent_object import AgentObject  # noqa: F401,E501


class AgentCreateAgentObject(AgentObject):
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
        "agent_created_at": "datetime",
        "agent_updated_at": "datetime",
        "agent_id": "float",
    }
    if hasattr(AgentObject, "swagger_types"):
        swagger_types.update(AgentObject.swagger_types)

    attribute_map = {
        "agent_created_at": "agent_created_at",
        "agent_updated_at": "agent_updated_at",
        "agent_id": "agent_id",
    }
    if hasattr(AgentObject, "attribute_map"):
        attribute_map.update(AgentObject.attribute_map)

    def __init__(
        self,
        agent_created_at=None,
        agent_updated_at=None,
        agent_id=None,
        *args,
        **kwargs
    ):  # noqa: E501
        """AgentCreateAgentObject - a model defined in Swagger"""  # noqa: E501
        self._agent_created_at = None
        self._agent_updated_at = None
        self._agent_id = None
        self.discriminator = None
        self.agent_created_at = agent_created_at
        self.agent_updated_at = agent_updated_at
        self.agent_id = agent_id
        AgentObject.__init__(self, *args, **kwargs)

    @property
    def agent_created_at(self):
        """Gets the agent_created_at of this AgentCreateAgentObject.  # noqa: E501


        :return: The agent_created_at of this AgentCreateAgentObject.  # noqa: E501
        :rtype: datetime
        """
        return self._agent_created_at

    @agent_created_at.setter
    def agent_created_at(self, agent_created_at):
        """Sets the agent_created_at of this AgentCreateAgentObject.


        :param agent_created_at: The agent_created_at of this AgentCreateAgentObject.  # noqa: E501
        :type: datetime
        """
        if agent_created_at is None:
            raise ValueError(
                "Invalid value for `agent_created_at`, must not be `None`"
            )  # noqa: E501

        self._agent_created_at = agent_created_at

    @property
    def agent_updated_at(self):
        """Gets the agent_updated_at of this AgentCreateAgentObject.  # noqa: E501


        :return: The agent_updated_at of this AgentCreateAgentObject.  # noqa: E501
        :rtype: datetime
        """
        return self._agent_updated_at

    @agent_updated_at.setter
    def agent_updated_at(self, agent_updated_at):
        """Sets the agent_updated_at of this AgentCreateAgentObject.


        :param agent_updated_at: The agent_updated_at of this AgentCreateAgentObject.  # noqa: E501
        :type: datetime
        """
        if agent_updated_at is None:
            raise ValueError(
                "Invalid value for `agent_updated_at`, must not be `None`"
            )  # noqa: E501

        self._agent_updated_at = agent_updated_at

    @property
    def agent_id(self):
        """Gets the agent_id of this AgentCreateAgentObject.  # noqa: E501


        :return: The agent_id of this AgentCreateAgentObject.  # noqa: E501
        :rtype: float
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this AgentCreateAgentObject.


        :param agent_id: The agent_id of this AgentCreateAgentObject.  # noqa: E501
        :type: float
        """
        if agent_id is None:
            raise ValueError(
                "Invalid value for `agent_id`, must not be `None`"
            )  # noqa: E501

        self._agent_id = agent_id

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
        if issubclass(AgentCreateAgentObject, dict):
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
        if not isinstance(other, AgentCreateAgentObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other