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


class Dhcpv4client(Base):
    """IPv4 global and per-port settings
    The Dhcpv4client class encapsulates a required dhcpv4client resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dhcpv4client'

    def __init__(self, parent):
        super(Dhcpv4client, self).__init__(parent)

    @property
    def SessionLifetime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.sessionlifetime.sessionlifetime.SessionLifetime): An instance of the SessionLifetime class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.sessionlifetime.sessionlifetime import SessionLifetime
        return SessionLifetime(self)._select()

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.startrate.startrate.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.startrate.startrate import StartRate
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.stoprate.stoprate.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.dhcpv4client.stoprate.stoprate import StopRate
        return StopRate(self)._select()

    @property
    def TlvEditor(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlveditor.TlvEditor): An instance of the TlvEditor class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlveditor import TlvEditor
        return TlvEditor(self)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute('descriptiveName')

    @property
    def Dhcp4ArpGw(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, DHCP clients ARP to find their Gateway MAC Addresses.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('dhcp4ArpGw'))

    @property
    def Dhcp4ClientPort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): UDP port that the client listens on for DHCP and BOOTP responses.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('dhcp4ClientPort'))

    @property
    def Dhcp4MaxDiscoverTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The max value, in seconds, that the discover timeout can reach though Discover Timeout Factor.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('dhcp4MaxDiscoverTimeout'))

    @property
    def Dhcp4NumRetry(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of times that the client will retransmit a request for which it has not received a response. When the maximum number of retransmitions is reached, the port will increment the failure counter (DHCPSetupFail).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('dhcp4NumRetry'))

    @property
    def Dhcp4ResponseTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The initial time, in seconds, that the subnet waits to receive a response from a DHCP server.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('dhcp4ResponseTimeout'))

    @property
    def Dhcp4ResponseTimeoutFactor(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The factor by which the timeout will be multiplied each time the response timeout has been reached.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('dhcp4ResponseTimeoutFactor'))

    @property
    def Dhcp4ServerPort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): UDP port that the client addresses server requests to.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('dhcp4ServerPort'))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def RenewOnLinkUp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicate to renew the active DHCP sessions after link status goes down and up.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('renewOnLinkUp'))

    @property
    def RowNames(self):
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute('rowNames')

    @property
    def SkipReleaseOnStop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, the client does not send a DHCPRELEASE packet when the Stop command is given.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('skipReleaseOnStop'))

    def update(self, Name=None):
        """Updates dhcpv4client resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def get_device_ids(self, PortNames=None, Dhcp4ArpGw=None, Dhcp4ClientPort=None, Dhcp4MaxDiscoverTimeout=None, Dhcp4NumRetry=None, Dhcp4ResponseTimeout=None, Dhcp4ResponseTimeoutFactor=None, Dhcp4ServerPort=None, RenewOnLinkUp=None, SkipReleaseOnStop=None):
        """Base class infrastructure that gets a list of dhcpv4client device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Dhcp4ArpGw (str): optional regex of dhcp4ArpGw
        - Dhcp4ClientPort (str): optional regex of dhcp4ClientPort
        - Dhcp4MaxDiscoverTimeout (str): optional regex of dhcp4MaxDiscoverTimeout
        - Dhcp4NumRetry (str): optional regex of dhcp4NumRetry
        - Dhcp4ResponseTimeout (str): optional regex of dhcp4ResponseTimeout
        - Dhcp4ResponseTimeoutFactor (str): optional regex of dhcp4ResponseTimeoutFactor
        - Dhcp4ServerPort (str): optional regex of dhcp4ServerPort
        - RenewOnLinkUp (str): optional regex of renewOnLinkUp
        - SkipReleaseOnStop (str): optional regex of skipReleaseOnStop

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
