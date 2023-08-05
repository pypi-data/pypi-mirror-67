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


class GroupStatLearnedInformation(Base):
    """NOT DEFINED
    The GroupStatLearnedInformation class encapsulates a list of groupStatLearnedInformation resources that are managed by the system.
    A list of resources can be retrieved from the server using the GroupStatLearnedInformation.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'groupStatLearnedInformation'

    def __init__(self, parent):
        super(GroupStatLearnedInformation, self).__init__(parent)

    @property
    def GroupStatBucketLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatbucketlearnedinformation_7b24adbf4d231474c1a82b3fc095fc63.GroupStatBucketLearnedInformation): An instance of the GroupStatBucketLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatbucketlearnedinformation_7b24adbf4d231474c1a82b3fc095fc63 import GroupStatBucketLearnedInformation
        return GroupStatBucketLearnedInformation(self)

    @property
    def ByteCount(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('byteCount')

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('dataPathId')

    @property
    def DataPathIdAsHex(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('dataPathIdAsHex')

    @property
    def DurationInNSec(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('durationInNSec')

    @property
    def DurationInSec(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('durationInSec')

    @property
    def ErrorCode(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('errorCode')

    @property
    def ErrorType(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('errorType')

    @property
    def GroupId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('groupId')

    @property
    def Latency(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('latency')

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('localIp')

    @property
    def NegotiatedVersion(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('negotiatedVersion')

    @property
    def NumberOfBucketStats(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('numberOfBucketStats')

    @property
    def PacketCount(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('packetCount')

    @property
    def ReferenceCount(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('referenceCount')

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('remoteIp')

    @property
    def ReplyState(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('replyState')

    def find(self, ByteCount=None, DataPathId=None, DataPathIdAsHex=None, DurationInNSec=None, DurationInSec=None, ErrorCode=None, ErrorType=None, GroupId=None, Latency=None, LocalIp=None, NegotiatedVersion=None, NumberOfBucketStats=None, PacketCount=None, ReferenceCount=None, RemoteIp=None, ReplyState=None):
        """Finds and retrieves groupStatLearnedInformation resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve groupStatLearnedInformation resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all groupStatLearnedInformation resources from the server.

        Args
        ----
        - ByteCount (str): NOT DEFINED
        - DataPathId (str): NOT DEFINED
        - DataPathIdAsHex (str): NOT DEFINED
        - DurationInNSec (str): NOT DEFINED
        - DurationInSec (str): NOT DEFINED
        - ErrorCode (str): NOT DEFINED
        - ErrorType (str): NOT DEFINED
        - GroupId (str): NOT DEFINED
        - Latency (number): NOT DEFINED
        - LocalIp (str): NOT DEFINED
        - NegotiatedVersion (str): NOT DEFINED
        - NumberOfBucketStats (str): NOT DEFINED
        - PacketCount (str): NOT DEFINED
        - ReferenceCount (str): NOT DEFINED
        - RemoteIp (str): NOT DEFINED
        - ReplyState (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching groupStatLearnedInformation resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of groupStatLearnedInformation data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the groupStatLearnedInformation resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
