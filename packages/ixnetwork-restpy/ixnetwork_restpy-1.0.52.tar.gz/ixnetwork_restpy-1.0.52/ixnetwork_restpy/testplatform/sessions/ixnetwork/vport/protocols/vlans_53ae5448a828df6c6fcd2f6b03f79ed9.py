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


class Vlans(Base):
    """This object hold the VLAN configuration.
    The Vlans class encapsulates a list of vlans resources that are managed by the user.
    A list of resources can be retrieved from the server using the Vlans.find() method.
    The list can be managed by using the Vlans.add() and Vlans.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vlans'

    def __init__(self, parent):
        super(Vlans, self).__init__(parent)

    @property
    def MacRanges(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macranges_2548634f9fc45eaa0e934f6d2059db36.MacRanges): An instance of the MacRanges class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macranges_2548634f9fc45eaa0e934f6d2059db36 import MacRanges
        return MacRanges(self)

    @property
    def CVlanId(self):
        """
        Returns
        -------
        - number: The stacked VLAN identifier.
        """
        return self._get_attribute('cVlanId')
    @CVlanId.setter
    def CVlanId(self, value):
        self._set_attribute('cVlanId', value)

    @property
    def CVlanPriority(self):
        """
        Returns
        -------
        - number: The stacked VLAN priority.
        """
        return self._get_attribute('cVlanPriority')
    @CVlanPriority.setter
    def CVlanPriority(self, value):
        self._set_attribute('cVlanPriority', value)

    @property
    def CVlanTpId(self):
        """
        Returns
        -------
        - str: The stacked VLAN TPID. EtherTypes identify the protocol that follows the VLAN header. Select from: 0x8100, 0x9100, 0x9200, or 0x88A8.
        """
        return self._get_attribute('cVlanTpId')
    @CVlanTpId.setter
    def CVlanTpId(self, value):
        self._set_attribute('cVlanTpId', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the VLAN is enabled.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def SVlanId(self):
        """
        Returns
        -------
        - number: The single VLAN identifier.
        """
        return self._get_attribute('sVlanId')
    @SVlanId.setter
    def SVlanId(self, value):
        self._set_attribute('sVlanId', value)

    @property
    def SVlanPriority(self):
        """
        Returns
        -------
        - number: The single VLAN priority.
        """
        return self._get_attribute('sVlanPriority')
    @SVlanPriority.setter
    def SVlanPriority(self, value):
        self._set_attribute('sVlanPriority', value)

    @property
    def SVlanTpId(self):
        """
        Returns
        -------
        - str: The single VLAN TPID. EtherTypes identify the protocol that follows the VLAN header. Select from: 0x8100, 0x9100, 0x9200, or 0x88A8.
        """
        return self._get_attribute('sVlanTpId')
    @SVlanTpId.setter
    def SVlanTpId(self, value):
        self._set_attribute('sVlanTpId', value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(singleVlan | stackedVlan): Sets the VLAN type.
        """
        return self._get_attribute('type')
    @Type.setter
    def Type(self, value):
        self._set_attribute('type', value)

    def update(self, CVlanId=None, CVlanPriority=None, CVlanTpId=None, Enabled=None, SVlanId=None, SVlanPriority=None, SVlanTpId=None, Type=None):
        """Updates vlans resource on the server.

        Args
        ----
        - CVlanId (number): The stacked VLAN identifier.
        - CVlanPriority (number): The stacked VLAN priority.
        - CVlanTpId (str): The stacked VLAN TPID. EtherTypes identify the protocol that follows the VLAN header. Select from: 0x8100, 0x9100, 0x9200, or 0x88A8.
        - Enabled (bool): If true, the VLAN is enabled.
        - SVlanId (number): The single VLAN identifier.
        - SVlanPriority (number): The single VLAN priority.
        - SVlanTpId (str): The single VLAN TPID. EtherTypes identify the protocol that follows the VLAN header. Select from: 0x8100, 0x9100, 0x9200, or 0x88A8.
        - Type (str(singleVlan | stackedVlan)): Sets the VLAN type.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, CVlanId=None, CVlanPriority=None, CVlanTpId=None, Enabled=None, SVlanId=None, SVlanPriority=None, SVlanTpId=None, Type=None):
        """Adds a new vlans resource on the server and adds it to the container.

        Args
        ----
        - CVlanId (number): The stacked VLAN identifier.
        - CVlanPriority (number): The stacked VLAN priority.
        - CVlanTpId (str): The stacked VLAN TPID. EtherTypes identify the protocol that follows the VLAN header. Select from: 0x8100, 0x9100, 0x9200, or 0x88A8.
        - Enabled (bool): If true, the VLAN is enabled.
        - SVlanId (number): The single VLAN identifier.
        - SVlanPriority (number): The single VLAN priority.
        - SVlanTpId (str): The single VLAN TPID. EtherTypes identify the protocol that follows the VLAN header. Select from: 0x8100, 0x9100, 0x9200, or 0x88A8.
        - Type (str(singleVlan | stackedVlan)): Sets the VLAN type.

        Returns
        -------
        - self: This instance with all currently retrieved vlans resources using find and the newly added vlans resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained vlans resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CVlanId=None, CVlanPriority=None, CVlanTpId=None, Enabled=None, SVlanId=None, SVlanPriority=None, SVlanTpId=None, Type=None):
        """Finds and retrieves vlans resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vlans resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vlans resources from the server.

        Args
        ----
        - CVlanId (number): The stacked VLAN identifier.
        - CVlanPriority (number): The stacked VLAN priority.
        - CVlanTpId (str): The stacked VLAN TPID. EtherTypes identify the protocol that follows the VLAN header. Select from: 0x8100, 0x9100, 0x9200, or 0x88A8.
        - Enabled (bool): If true, the VLAN is enabled.
        - SVlanId (number): The single VLAN identifier.
        - SVlanPriority (number): The single VLAN priority.
        - SVlanTpId (str): The single VLAN TPID. EtherTypes identify the protocol that follows the VLAN header. Select from: 0x8100, 0x9100, 0x9200, or 0x88A8.
        - Type (str(singleVlan | stackedVlan)): Sets the VLAN type.

        Returns
        -------
        - self: This instance with matching vlans resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of vlans data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vlans resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
