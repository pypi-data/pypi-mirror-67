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


class L2VcIpRange(Base):
    """This object holds a list of Layer 2 VC IP address ranges.
    The L2VcIpRange class encapsulates a required l2VcIpRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'l2VcIpRange'

    def __init__(self, parent):
        super(L2VcIpRange, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the Layer 2 IP address range.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def IncrementBy(self):
        """
        Returns
        -------
        - number: The value to be added for creating each additional L2 VC IP route range.
        """
        return self._get_attribute('incrementBy')
    @IncrementBy.setter
    def IncrementBy(self, value):
        self._set_attribute('incrementBy', value)

    @property
    def Mask(self):
        """
        Returns
        -------
        - number: The number of bits in the mask applied to the network address. The masked bits in the first network address form the address prefix.
        """
        return self._get_attribute('mask')
    @Mask.setter
    def Mask(self, value):
        self._set_attribute('mask', value)

    @property
    def NumHosts(self):
        """
        Returns
        -------
        - number: The number of emulated LDP hosts to be created on this port.
        """
        return self._get_attribute('numHosts')
    @NumHosts.setter
    def NumHosts(self, value):
        self._set_attribute('numHosts', value)

    @property
    def PeerAddress(self):
        """
        Returns
        -------
        - str: The 32-bit IPv4 address of the LDP peer.
        """
        return self._get_attribute('peerAddress')

    @property
    def StartAddress(self):
        """
        Returns
        -------
        - str: The IP address that starts the L2 VC IP range.
        """
        return self._get_attribute('startAddress')
    @StartAddress.setter
    def StartAddress(self, value):
        self._set_attribute('startAddress', value)

    def update(self, Enabled=None, IncrementBy=None, Mask=None, NumHosts=None, StartAddress=None):
        """Updates l2VcIpRange resource on the server.

        Args
        ----
        - Enabled (bool): Enables the Layer 2 IP address range.
        - IncrementBy (number): The value to be added for creating each additional L2 VC IP route range.
        - Mask (number): The number of bits in the mask applied to the network address. The masked bits in the first network address form the address prefix.
        - NumHosts (number): The number of emulated LDP hosts to be created on this port.
        - StartAddress (str): The IP address that starts the L2 VC IP range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
