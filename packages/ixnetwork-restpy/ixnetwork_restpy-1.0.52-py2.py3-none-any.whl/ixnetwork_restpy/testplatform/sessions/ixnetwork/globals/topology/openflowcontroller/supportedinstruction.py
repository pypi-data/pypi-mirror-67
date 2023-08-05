# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SupportedInstruction(Base):
    """Instruction prototype.
    The SupportedInstruction class encapsulates a list of supportedInstruction resources that are managed by the user.
    A list of resources can be retrieved from the server using the SupportedInstruction.find() method.
    The list can be managed by using the SupportedInstruction.add() and SupportedInstruction.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'supportedInstruction'

    def __init__(self, parent):
        super(SupportedInstruction, self).__init__(parent)

    @property
    def ActionSet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.actionset.ActionSet): An instance of the ActionSet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.actionset import ActionSet
        return ActionSet(self)

    @property
    def Field(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.field.Field): An instance of the Field class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.field import Field
        return Field(self)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute('count')

    @property
    def Description(self):
        """
        Returns
        -------
        - str: Description of the TLV prototype.
        """
        return self._get_attribute('description')
    @Description.setter
    def Description(self, value):
        self._set_attribute('description', value)

    @property
    def IsEditable(self):
        """
        Returns
        -------
        - bool: Information on the requirement of the field.
        """
        return self._get_attribute('isEditable')
    @IsEditable.setter
    def IsEditable(self, value):
        self._set_attribute('isEditable', value)

    @property
    def IsRepeatable(self):
        """
        Returns
        -------
        - bool: Information if the field can be multiplied in the tlv definition.
        """
        return self._get_attribute('isRepeatable')
    @IsRepeatable.setter
    def IsRepeatable(self, value):
        self._set_attribute('isRepeatable', value)

    @property
    def IsRequired(self):
        """
        Returns
        -------
        - bool: Information on the requirement of the field.
        """
        return self._get_attribute('isRequired')
    @IsRequired.setter
    def IsRequired(self, value):
        self._set_attribute('isRequired', value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of the TLV field.
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    def update(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        """Updates supportedInstruction resource on the server.

        Args
        ----
        - Description (str): Description of the TLV prototype.
        - IsEditable (bool): Information on the requirement of the field.
        - IsRepeatable (bool): Information if the field can be multiplied in the tlv definition.
        - IsRequired (bool): Information on the requirement of the field.
        - Name (str): Name of the TLV field.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        """Adds a new supportedInstruction resource on the server and adds it to the container.

        Args
        ----
        - Description (str): Description of the TLV prototype.
        - IsEditable (bool): Information on the requirement of the field.
        - IsRepeatable (bool): Information if the field can be multiplied in the tlv definition.
        - IsRequired (bool): Information on the requirement of the field.
        - Name (str): Name of the TLV field.

        Returns
        -------
        - self: This instance with all currently retrieved supportedInstruction resources using find and the newly added supportedInstruction resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained supportedInstruction resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
        """Finds and retrieves supportedInstruction resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve supportedInstruction resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all supportedInstruction resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - Description (str): Description of the TLV prototype.
        - IsEditable (bool): Information on the requirement of the field.
        - IsRepeatable (bool): Information if the field can be multiplied in the tlv definition.
        - IsRequired (bool): Information on the requirement of the field.
        - Name (str): Name of the TLV field.

        Returns
        -------
        - self: This instance with matching supportedInstruction resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of supportedInstruction data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the supportedInstruction resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
