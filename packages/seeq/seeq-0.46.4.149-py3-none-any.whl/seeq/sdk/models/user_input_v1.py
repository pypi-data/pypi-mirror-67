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


class UserInputV1(object):
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
        'data_id': 'str',
        'datasource_class': 'str',
        'datasource_id': 'str',
        'description': 'str',
        'email': 'str',
        'first_name': 'str',
        'is_admin': 'bool',
        'is_enabled': 'bool',
        'last_name': 'str',
        'name': 'str',
        'password': 'str',
        'session_duration': 'int',
        'username': 'str',
        'workbench': 'str'
    }

    attribute_map = {
        'data_id': 'dataId',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'description': 'description',
        'email': 'email',
        'first_name': 'firstName',
        'is_admin': 'isAdmin',
        'is_enabled': 'isEnabled',
        'last_name': 'lastName',
        'name': 'name',
        'password': 'password',
        'session_duration': 'sessionDuration',
        'username': 'username',
        'workbench': 'workbench'
    }

    def __init__(self, data_id=None, datasource_class=None, datasource_id=None, description=None, email=None, first_name=None, is_admin=None, is_enabled=None, last_name=None, name=None, password=None, session_duration=None, username=None, workbench=None):
        """
        UserInputV1 - a model defined in Swagger
        """

        self._data_id = None
        self._datasource_class = None
        self._datasource_id = None
        self._description = None
        self._email = None
        self._first_name = None
        self._is_admin = None
        self._is_enabled = None
        self._last_name = None
        self._name = None
        self._password = None
        self._session_duration = None
        self._username = None
        self._workbench = None

        if data_id is not None:
          self.data_id = data_id
        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if description is not None:
          self.description = description
        if email is not None:
          self.email = email
        if first_name is not None:
          self.first_name = first_name
        if is_admin is not None:
          self.is_admin = is_admin
        if is_enabled is not None:
          self.is_enabled = is_enabled
        if last_name is not None:
          self.last_name = last_name
        if name is not None:
          self.name = name
        if password is not None:
          self.password = password
        if session_duration is not None:
          self.session_duration = session_duration
        if username is not None:
          self.username = username
        if workbench is not None:
          self.workbench = workbench

    @property
    def data_id(self):
        """
        Gets the data_id of this UserInputV1.
        The unique identifier of this user within the datasource. Leave null to use the username as the Data ID.

        :return: The data_id of this UserInputV1.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """
        Sets the data_id of this UserInputV1.
        The unique identifier of this user within the datasource. Leave null to use the username as the Data ID.

        :param data_id: The data_id of this UserInputV1.
        :type: str
        """

        self._data_id = data_id

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this UserInputV1.
        The class of the auth provider for this user. Leave null to use the Seeq datasource.

        :return: The datasource_class of this UserInputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this UserInputV1.
        The class of the auth provider for this user. Leave null to use the Seeq datasource.

        :param datasource_class: The datasource_class of this UserInputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this UserInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource. For example, a datasource may be a particular instance of an Active Directory. Leave null to use the Seeq datasource.

        :return: The datasource_id of this UserInputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this UserInputV1.
        Along with the Datasource Class, the Datasource ID uniquely identifies a datasource. For example, a datasource may be a particular instance of an Active Directory. Leave null to use the Seeq datasource.

        :param datasource_id: The datasource_id of this UserInputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def description(self):
        """
        Gets the description of this UserInputV1.
        Clarifying information or other plain language description of this asset. An input of just whitespace is equivalent to a null input.

        :return: The description of this UserInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UserInputV1.
        Clarifying information or other plain language description of this asset. An input of just whitespace is equivalent to a null input.

        :param description: The description of this UserInputV1.
        :type: str
        """

        self._description = description

    @property
    def email(self):
        """
        Gets the email of this UserInputV1.
        The email address of the user

        :return: The email of this UserInputV1.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserInputV1.
        The email address of the user

        :param email: The email of this UserInputV1.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this UserInputV1.
        The first name of the user

        :return: The first_name of this UserInputV1.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UserInputV1.
        The first name of the user

        :param first_name: The first_name of this UserInputV1.
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")

        self._first_name = first_name

    @property
    def is_admin(self):
        """
        Gets the is_admin of this UserInputV1.
        Whether or not the user is an administrator.

        :return: The is_admin of this UserInputV1.
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """
        Sets the is_admin of this UserInputV1.
        Whether or not the user is an administrator.

        :param is_admin: The is_admin of this UserInputV1.
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UserInputV1.
        Whether the user is enabled or disabled.

        :return: The is_enabled of this UserInputV1.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UserInputV1.
        Whether the user is enabled or disabled.

        :param is_enabled: The is_enabled of this UserInputV1.
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def last_name(self):
        """
        Gets the last_name of this UserInputV1.
        The last name of the user

        :return: The last_name of this UserInputV1.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UserInputV1.
        The last name of the user

        :param last_name: The last_name of this UserInputV1.
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")

        self._last_name = last_name

    @property
    def name(self):
        """
        Gets the name of this UserInputV1.
        Human readable name. Null or whitespace names are not permitted. Defaults to a concatenation of the first and last name

        :return: The name of this UserInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserInputV1.
        Human readable name. Null or whitespace names are not permitted. Defaults to a concatenation of the first and last name

        :param name: The name of this UserInputV1.
        :type: str
        """

        self._name = name

    @property
    def password(self):
        """
        Gets the password of this UserInputV1.
        The password of the user. Required for users in the Seeq datasource.

        :return: The password of this UserInputV1.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UserInputV1.
        The password of the user. Required for users in the Seeq datasource.

        :param password: The password of this UserInputV1.
        :type: str
        """

        self._password = password

    @property
    def session_duration(self):
        """
        Gets the session_duration of this UserInputV1.
        The session duration, in minutes, for the user. Defaults to 1 day. This controls the maximum period of inactivity before the user must authenticate again. A value of 0 indicates the user does not have a session duration.

        :return: The session_duration of this UserInputV1.
        :rtype: int
        """
        return self._session_duration

    @session_duration.setter
    def session_duration(self, session_duration):
        """
        Sets the session_duration of this UserInputV1.
        The session duration, in minutes, for the user. Defaults to 1 day. This controls the maximum period of inactivity before the user must authenticate again. A value of 0 indicates the user does not have a session duration.

        :param session_duration: The session_duration of this UserInputV1.
        :type: int
        """

        self._session_duration = session_duration

    @property
    def username(self):
        """
        Gets the username of this UserInputV1.
        The username of the user. Required for users from an external directory such as LDAP or Windows Authentication.

        :return: The username of this UserInputV1.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserInputV1.
        The username of the user. Required for users from an external directory such as LDAP or Windows Authentication.

        :param username: The username of this UserInputV1.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

    @property
    def workbench(self):
        """
        Gets the workbench of this UserInputV1.
        The workbench configuration of this user.

        :return: The workbench of this UserInputV1.
        :rtype: str
        """
        return self._workbench

    @workbench.setter
    def workbench(self, workbench):
        """
        Sets the workbench of this UserInputV1.
        The workbench configuration of this user.

        :param workbench: The workbench of this UserInputV1.
        :type: str
        """

        self._workbench = workbench

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
        if not isinstance(other, UserInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
