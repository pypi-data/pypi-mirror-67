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


class MatchFields(Base):
    """NOT DEFINED
    The MatchFields class encapsulates a required matchFields resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'matchFields'

    def __init__(self, parent):
        super(MatchFields, self).__init__(parent)

    @property
    def ArpDestinationIpv4Address(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('arpDestinationIpv4Address')
    @ArpDestinationIpv4Address.setter
    def ArpDestinationIpv4Address(self, value):
        self._set_attribute('arpDestinationIpv4Address', value)

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('arpOpcode')
    @ArpOpcode.setter
    def ArpOpcode(self, value):
        self._set_attribute('arpOpcode', value)

    @property
    def ArpSourceHardwareAddress(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('arpSourceHardwareAddress')
    @ArpSourceHardwareAddress.setter
    def ArpSourceHardwareAddress(self, value):
        self._set_attribute('arpSourceHardwareAddress', value)

    @property
    def ArpSourceIpv4Address(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('arpSourceIpv4Address')
    @ArpSourceIpv4Address.setter
    def ArpSourceIpv4Address(self, value):
        self._set_attribute('arpSourceIpv4Address', value)

    @property
    def ArpTargetHardwareAddress(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('arpTargetHardwareAddress')
    @ArpTargetHardwareAddress.setter
    def ArpTargetHardwareAddress(self, value):
        self._set_attribute('arpTargetHardwareAddress', value)

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ethernetDestination')
    @EthernetDestination.setter
    def EthernetDestination(self, value):
        self._set_attribute('ethernetDestination', value)

    @property
    def EthernetSource(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ethernetSource')
    @EthernetSource.setter
    def EthernetSource(self, value):
        self._set_attribute('ethernetSource', value)

    @property
    def EthernetType(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ethernetType')
    @EthernetType.setter
    def EthernetType(self, value):
        self._set_attribute('ethernetType', value)

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('experimenter')
    @Experimenter.setter
    def Experimenter(self, value):
        self._set_attribute('experimenter', value)

    @property
    def IcmpCode(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('icmpCode')
    @IcmpCode.setter
    def IcmpCode(self, value):
        self._set_attribute('icmpCode', value)

    @property
    def IcmpType(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('icmpType')
    @IcmpType.setter
    def IcmpType(self, value):
        self._set_attribute('icmpType', value)

    @property
    def Icmpv6Code(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('icmpv6Code')
    @Icmpv6Code.setter
    def Icmpv6Code(self, value):
        self._set_attribute('icmpv6Code', value)

    @property
    def Icmpv6Type(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('icmpv6Type')
    @Icmpv6Type.setter
    def Icmpv6Type(self, value):
        self._set_attribute('icmpv6Type', value)

    @property
    def InPort(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('inPort')
    @InPort.setter
    def InPort(self, value):
        self._set_attribute('inPort', value)

    @property
    def IpDscp(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipDscp')
    @IpDscp.setter
    def IpDscp(self, value):
        self._set_attribute('ipDscp', value)

    @property
    def IpEcn(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipEcn')
    @IpEcn.setter
    def IpEcn(self, value):
        self._set_attribute('ipEcn', value)

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipProtocol')
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute('ipProtocol', value)

    @property
    def Ipv4Destination(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipv4Destination')
    @Ipv4Destination.setter
    def Ipv4Destination(self, value):
        self._set_attribute('ipv4Destination', value)

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipv4Source')
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute('ipv4Source', value)

    @property
    def Ipv6Destination(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipv6Destination')
    @Ipv6Destination.setter
    def Ipv6Destination(self, value):
        self._set_attribute('ipv6Destination', value)

    @property
    def Ipv6ExtHeader(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipv6ExtHeader')
    @Ipv6ExtHeader.setter
    def Ipv6ExtHeader(self, value):
        self._set_attribute('ipv6ExtHeader', value)

    @property
    def Ipv6FlowLabel(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipv6FlowLabel')
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute('ipv6FlowLabel', value)

    @property
    def Ipv6NdSll(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipv6NdSll')
    @Ipv6NdSll.setter
    def Ipv6NdSll(self, value):
        self._set_attribute('ipv6NdSll', value)

    @property
    def Ipv6NdTarget(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipv6NdTarget')
    @Ipv6NdTarget.setter
    def Ipv6NdTarget(self, value):
        self._set_attribute('ipv6NdTarget', value)

    @property
    def Ipv6NdTll(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipv6NdTll')
    @Ipv6NdTll.setter
    def Ipv6NdTll(self, value):
        self._set_attribute('ipv6NdTll', value)

    @property
    def Ipv6Source(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipv6Source')
    @Ipv6Source.setter
    def Ipv6Source(self, value):
        self._set_attribute('ipv6Source', value)

    @property
    def Metadata(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('metadata')
    @Metadata.setter
    def Metadata(self, value):
        self._set_attribute('metadata', value)

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('mplsBos')
    @MplsBos.setter
    def MplsBos(self, value):
        self._set_attribute('mplsBos', value)

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('mplsLabel')
    @MplsLabel.setter
    def MplsLabel(self, value):
        self._set_attribute('mplsLabel', value)

    @property
    def MplsTc(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('mplsTc')
    @MplsTc.setter
    def MplsTc(self, value):
        self._set_attribute('mplsTc', value)

    @property
    def PbbIsid(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('pbbIsid')
    @PbbIsid.setter
    def PbbIsid(self, value):
        self._set_attribute('pbbIsid', value)

    @property
    def PhysicalInPort(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('physicalInPort')
    @PhysicalInPort.setter
    def PhysicalInPort(self, value):
        self._set_attribute('physicalInPort', value)

    @property
    def SctpDestination(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('sctpDestination')
    @SctpDestination.setter
    def SctpDestination(self, value):
        self._set_attribute('sctpDestination', value)

    @property
    def SctpSource(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('sctpSource')
    @SctpSource.setter
    def SctpSource(self, value):
        self._set_attribute('sctpSource', value)

    @property
    def TcpDestination(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('tcpDestination')
    @TcpDestination.setter
    def TcpDestination(self, value):
        self._set_attribute('tcpDestination', value)

    @property
    def TcpSource(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('tcpSource')
    @TcpSource.setter
    def TcpSource(self, value):
        self._set_attribute('tcpSource', value)

    @property
    def TunnelId(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('tunnelId')
    @TunnelId.setter
    def TunnelId(self, value):
        self._set_attribute('tunnelId', value)

    @property
    def UdpDestination(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('udpDestination')
    @UdpDestination.setter
    def UdpDestination(self, value):
        self._set_attribute('udpDestination', value)

    @property
    def UdpSource(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('udpSource')
    @UdpSource.setter
    def UdpSource(self, value):
        self._set_attribute('udpSource', value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('vlanId')
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute('vlanId', value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('vlanPriority')
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute('vlanPriority', value)

    def update(self, ArpDestinationIpv4Address=None, ArpOpcode=None, ArpSourceHardwareAddress=None, ArpSourceIpv4Address=None, ArpTargetHardwareAddress=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, Experimenter=None, IcmpCode=None, IcmpType=None, Icmpv6Code=None, Icmpv6Type=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6NdTll=None, Ipv6Source=None, Metadata=None, MplsBos=None, MplsLabel=None, MplsTc=None, PbbIsid=None, PhysicalInPort=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
        """Updates matchFields resource on the server.

        Args
        ----
        - ArpDestinationIpv4Address (bool): NOT DEFINED
        - ArpOpcode (bool): NOT DEFINED
        - ArpSourceHardwareAddress (bool): NOT DEFINED
        - ArpSourceIpv4Address (bool): NOT DEFINED
        - ArpTargetHardwareAddress (bool): NOT DEFINED
        - EthernetDestination (bool): NOT DEFINED
        - EthernetSource (bool): NOT DEFINED
        - EthernetType (bool): NOT DEFINED
        - Experimenter (bool): NOT DEFINED
        - IcmpCode (bool): NOT DEFINED
        - IcmpType (bool): NOT DEFINED
        - Icmpv6Code (bool): NOT DEFINED
        - Icmpv6Type (bool): NOT DEFINED
        - InPort (bool): NOT DEFINED
        - IpDscp (bool): NOT DEFINED
        - IpEcn (bool): NOT DEFINED
        - IpProtocol (bool): NOT DEFINED
        - Ipv4Destination (bool): NOT DEFINED
        - Ipv4Source (bool): NOT DEFINED
        - Ipv6Destination (bool): NOT DEFINED
        - Ipv6ExtHeader (bool): NOT DEFINED
        - Ipv6FlowLabel (bool): NOT DEFINED
        - Ipv6NdSll (bool): NOT DEFINED
        - Ipv6NdTarget (bool): NOT DEFINED
        - Ipv6NdTll (bool): NOT DEFINED
        - Ipv6Source (bool): NOT DEFINED
        - Metadata (bool): NOT DEFINED
        - MplsBos (bool): NOT DEFINED
        - MplsLabel (bool): NOT DEFINED
        - MplsTc (bool): NOT DEFINED
        - PbbIsid (bool): NOT DEFINED
        - PhysicalInPort (bool): NOT DEFINED
        - SctpDestination (bool): NOT DEFINED
        - SctpSource (bool): NOT DEFINED
        - TcpDestination (bool): NOT DEFINED
        - TcpSource (bool): NOT DEFINED
        - TunnelId (bool): NOT DEFINED
        - UdpDestination (bool): NOT DEFINED
        - UdpSource (bool): NOT DEFINED
        - VlanId (bool): NOT DEFINED
        - VlanPriority (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
