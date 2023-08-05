# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.46.04
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WorksheetInputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'branch_from': 'str',
        'name': 'str'
    }

    attribute_map = {
        'branch_from': 'branchFrom',
        'name': 'name'
    }

    def __init__(self, branch_from=None, name=None):
        """
        WorksheetInputV1 - a model defined in Swagger
        """

        self._branch_from = None
        self._name = None

        if branch_from is not None:
          self.branch_from = branch_from
        if name is not None:
          self.name = name

    @property
    def branch_from(self):
        """
        Gets the branch_from of this WorksheetInputV1.
        Create a new worksheet by duplicating the contents and history of the worksheet with the specified ID. When null, no branching will occur; resulting worksheet will be blank.

        :return: The branch_from of this WorksheetInputV1.
        :rtype: str
        """
        return self._branch_from

    @branch_from.setter
    def branch_from(self, branch_from):
        """
        Sets the branch_from of this WorksheetInputV1.
        Create a new worksheet by duplicating the contents and history of the worksheet with the specified ID. When null, no branching will occur; resulting worksheet will be blank.

        :param branch_from: The branch_from of this WorksheetInputV1.
        :type: str
        """

        self._branch_from = branch_from

    @property
    def name(self):
        """
        Gets the name of this WorksheetInputV1.
        Human readable name. Null or whitespace names are not permitted.

        :return: The name of this WorksheetInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorksheetInputV1.
        Human readable name. Null or whitespace names are not permitted.

        :param name: The name of this WorksheetInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, WorksheetInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
