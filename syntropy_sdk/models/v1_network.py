# coding: utf-8

"""
    Syntropy network API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@syntropynet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V1Network(object):
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
        'agent_connection_groups': 'list[V1NetworkConnectionGroup]',
        'agents': 'list[V1NetworkAgent]'
    }

    attribute_map = {
        'agent_connection_groups': 'agent_connection_groups',
        'agents': 'agents'
    }

    def __init__(self, agent_connection_groups=None, agents=None):  # noqa: E501
        """V1Network - a model defined in Swagger"""  # noqa: E501
        self._agent_connection_groups = None
        self._agents = None
        self.discriminator = None
        self.agent_connection_groups = agent_connection_groups
        self.agents = agents

    @property
    def agent_connection_groups(self):
        """Gets the agent_connection_groups of this V1Network.  # noqa: E501


        :return: The agent_connection_groups of this V1Network.  # noqa: E501
        :rtype: list[V1NetworkConnectionGroup]
        """
        return self._agent_connection_groups

    @agent_connection_groups.setter
    def agent_connection_groups(self, agent_connection_groups):
        """Sets the agent_connection_groups of this V1Network.


        :param agent_connection_groups: The agent_connection_groups of this V1Network.  # noqa: E501
        :type: list[V1NetworkConnectionGroup]
        """
        if agent_connection_groups is None:
            raise ValueError("Invalid value for `agent_connection_groups`, must not be `None`")  # noqa: E501

        self._agent_connection_groups = agent_connection_groups

    @property
    def agents(self):
        """Gets the agents of this V1Network.  # noqa: E501


        :return: The agents of this V1Network.  # noqa: E501
        :rtype: list[V1NetworkAgent]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this V1Network.


        :param agents: The agents of this V1Network.  # noqa: E501
        :type: list[V1NetworkAgent]
        """
        if agents is None:
            raise ValueError("Invalid value for `agents`, must not be `None`")  # noqa: E501

        self._agents = agents

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
        if issubclass(V1Network, dict):
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
        if not isinstance(other, V1Network):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other