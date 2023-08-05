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


class ScalarValueOutputV1(object):
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
        'is_uncertain': 'bool',
        'status_message': 'str',
        'uom': 'str',
        'value': 'object',
        'warning_count': 'int',
        'warning_logs': 'list[FormulaLogV1]'
    }

    attribute_map = {
        'is_uncertain': 'isUncertain',
        'status_message': 'statusMessage',
        'uom': 'uom',
        'value': 'value',
        'warning_count': 'warningCount',
        'warning_logs': 'warningLogs'
    }

    def __init__(self, is_uncertain=False, status_message=None, uom=None, value=None, warning_count=None, warning_logs=None):
        """
        ScalarValueOutputV1 - a model defined in Swagger
        """

        self._is_uncertain = None
        self._status_message = None
        self._uom = None
        self._value = None
        self._warning_count = None
        self._warning_logs = None

        if is_uncertain is not None:
          self.is_uncertain = is_uncertain
        if status_message is not None:
          self.status_message = status_message
        if uom is not None:
          self.uom = uom
        if value is not None:
          self.value = value
        if warning_count is not None:
          self.warning_count = warning_count
        if warning_logs is not None:
          self.warning_logs = warning_logs

    @property
    def is_uncertain(self):
        """
        Gets the is_uncertain of this ScalarValueOutputV1.
        True if this scalar is uncertain

        :return: The is_uncertain of this ScalarValueOutputV1.
        :rtype: bool
        """
        return self._is_uncertain

    @is_uncertain.setter
    def is_uncertain(self, is_uncertain):
        """
        Sets the is_uncertain of this ScalarValueOutputV1.
        True if this scalar is uncertain

        :param is_uncertain: The is_uncertain of this ScalarValueOutputV1.
        :type: bool
        """

        self._is_uncertain = is_uncertain

    @property
    def status_message(self):
        """
        Gets the status_message of this ScalarValueOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this ScalarValueOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ScalarValueOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this ScalarValueOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def uom(self):
        """
        Gets the uom of this ScalarValueOutputV1.
        The unit of measure of the scalar

        :return: The uom of this ScalarValueOutputV1.
        :rtype: str
        """
        return self._uom

    @uom.setter
    def uom(self, uom):
        """
        Sets the uom of this ScalarValueOutputV1.
        The unit of measure of the scalar

        :param uom: The uom of this ScalarValueOutputV1.
        :type: str
        """
        if uom is None:
            raise ValueError("Invalid value for `uom`, must not be `None`")

        self._uom = uom

    @property
    def value(self):
        """
        Gets the value of this ScalarValueOutputV1.
        The value of the scalar

        :return: The value of this ScalarValueOutputV1.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ScalarValueOutputV1.
        The value of the scalar

        :param value: The value of this ScalarValueOutputV1.
        :type: object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

    @property
    def warning_count(self):
        """
        Gets the warning_count of this ScalarValueOutputV1.
        The total number of warnings that have occurred

        :return: The warning_count of this ScalarValueOutputV1.
        :rtype: int
        """
        return self._warning_count

    @warning_count.setter
    def warning_count(self, warning_count):
        """
        Sets the warning_count of this ScalarValueOutputV1.
        The total number of warnings that have occurred

        :param warning_count: The warning_count of this ScalarValueOutputV1.
        :type: int
        """

        self._warning_count = warning_count

    @property
    def warning_logs(self):
        """
        Gets the warning_logs of this ScalarValueOutputV1.
        The Formula warning logs, which includes the text, line number, and column number where the warning occurred in addition to the warning details

        :return: The warning_logs of this ScalarValueOutputV1.
        :rtype: list[FormulaLogV1]
        """
        return self._warning_logs

    @warning_logs.setter
    def warning_logs(self, warning_logs):
        """
        Sets the warning_logs of this ScalarValueOutputV1.
        The Formula warning logs, which includes the text, line number, and column number where the warning occurred in addition to the warning details

        :param warning_logs: The warning_logs of this ScalarValueOutputV1.
        :type: list[FormulaLogV1]
        """

        self._warning_logs = warning_logs

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
        if not isinstance(other, ScalarValueOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
