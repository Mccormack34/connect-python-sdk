# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class CreateBreakTypeRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, idempotency_key=None, break_type=None):
        """
        CreateBreakTypeRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'idempotency_key': 'str',
            'break_type': 'BreakType'
        }

        self.attribute_map = {
            'idempotency_key': 'idempotency_key',
            'break_type': 'break_type'
        }

        self._idempotency_key = idempotency_key
        self._break_type = break_type

    @property
    def idempotency_key(self):
        """
        Gets the idempotency_key of this CreateBreakTypeRequest.
        Unique string value to insure idempotency of the operation

        :return: The idempotency_key of this CreateBreakTypeRequest.
        :rtype: str
        """
        return self._idempotency_key

    @idempotency_key.setter
    def idempotency_key(self, idempotency_key):
        """
        Sets the idempotency_key of this CreateBreakTypeRequest.
        Unique string value to insure idempotency of the operation

        :param idempotency_key: The idempotency_key of this CreateBreakTypeRequest.
        :type: str
        """

        if idempotency_key is None:
            raise ValueError("Invalid value for `idempotency_key`, must not be `None`")
        if len(idempotency_key) > 128:
            raise ValueError("Invalid value for `idempotency_key`, length must be less than `128`")

        self._idempotency_key = idempotency_key

    @property
    def break_type(self):
        """
        Gets the break_type of this CreateBreakTypeRequest.
        The `BreakType` to be created.

        :return: The break_type of this CreateBreakTypeRequest.
        :rtype: BreakType
        """
        return self._break_type

    @break_type.setter
    def break_type(self, break_type):
        """
        Sets the break_type of this CreateBreakTypeRequest.
        The `BreakType` to be created.

        :param break_type: The break_type of this CreateBreakTypeRequest.
        :type: BreakType
        """

        self._break_type = break_type

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
