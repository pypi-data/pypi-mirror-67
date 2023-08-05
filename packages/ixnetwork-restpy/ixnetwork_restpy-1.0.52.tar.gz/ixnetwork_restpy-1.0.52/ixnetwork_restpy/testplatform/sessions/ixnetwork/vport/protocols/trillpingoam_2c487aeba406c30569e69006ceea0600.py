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


class TrillPingOam(Base):
    """NOT DEFINED
    The TrillPingOam class encapsulates a required trillPingOam resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'trillPingOam'

    def __init__(self, parent):
        super(TrillPingOam, self).__init__(parent)

    @property
    def AlertFlag(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('alertFlag')
    @AlertFlag.setter
    def AlertFlag(self, value):
        self._set_attribute('alertFlag', value)

    @property
    def DestinationNickname(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('destinationNickname')
    @DestinationNickname.setter
    def DestinationNickname(self, value):
        self._set_attribute('destinationNickname', value)

    @property
    def EtherType(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('etherType')
    @EtherType.setter
    def EtherType(self, value):
        self._set_attribute('etherType', value)

    @property
    def HopCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('hopCount')
    @HopCount.setter
    def HopCount(self, value):
        self._set_attribute('hopCount', value)

    @property
    def NativeFlag(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('nativeFlag')
    @NativeFlag.setter
    def NativeFlag(self, value):
        self._set_attribute('nativeFlag', value)

    @property
    def NoOfPingRequests(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('noOfPingRequests')
    @NoOfPingRequests.setter
    def NoOfPingRequests(self, value):
        self._set_attribute('noOfPingRequests', value)

    @property
    def SilentFlag(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('silentFlag')
    @SilentFlag.setter
    def SilentFlag(self, value):
        self._set_attribute('silentFlag', value)

    @property
    def SourceNickname(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('sourceNickname')
    @SourceNickname.setter
    def SourceNickname(self, value):
        self._set_attribute('sourceNickname', value)

    @property
    def TimeOut(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('timeOut')
    @TimeOut.setter
    def TimeOut(self, value):
        self._set_attribute('timeOut', value)

    def update(self, AlertFlag=None, DestinationNickname=None, EtherType=None, HopCount=None, NativeFlag=None, NoOfPingRequests=None, SilentFlag=None, SourceNickname=None, TimeOut=None):
        """Updates trillPingOam resource on the server.

        Args
        ----
        - AlertFlag (bool): NOT DEFINED
        - DestinationNickname (number): NOT DEFINED
        - EtherType (number): NOT DEFINED
        - HopCount (number): NOT DEFINED
        - NativeFlag (bool): NOT DEFINED
        - NoOfPingRequests (number): NOT DEFINED
        - SilentFlag (bool): NOT DEFINED
        - SourceNickname (number): NOT DEFINED
        - TimeOut (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
