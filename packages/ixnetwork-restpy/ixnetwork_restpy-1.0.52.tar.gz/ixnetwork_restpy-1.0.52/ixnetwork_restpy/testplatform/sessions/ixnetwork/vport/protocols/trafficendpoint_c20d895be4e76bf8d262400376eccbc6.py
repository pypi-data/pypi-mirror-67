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


class TrafficEndPoint(Base):
    """Specifies the Traffic Endpoints added to the grid.
    The TrafficEndPoint class encapsulates a list of trafficEndPoint resources that are managed by the user.
    A list of resources can be retrieved from the server using the TrafficEndPoint.find() method.
    The list can be managed by using the TrafficEndPoint.add() and TrafficEndPoint.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'trafficEndPoint'

    def __init__(self, parent):
        super(TrafficEndPoint, self).__init__(parent)

    @property
    def ArpViaInterface(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, ARP request is conveyed through an Interface.
        """
        return self._get_attribute('arpViaInterface')
    @ArpViaInterface.setter
    def ArpViaInterface(self, value):
        self._set_attribute('arpViaInterface', value)

    @property
    def CustomEtherHeaderLength(self):
        """DEPRECATED 
        Returns
        -------
        - number: Specifies the Custom Header length in bytes.
        """
        return self._get_attribute('customEtherHeaderLength')
    @CustomEtherHeaderLength.setter
    def CustomEtherHeaderLength(self, value):
        self._set_attribute('customEtherHeaderLength', value)

    @property
    def CustomEtherHeaderValue(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the Custom ether Header value.
        """
        return self._get_attribute('customEtherHeaderValue')
    @CustomEtherHeaderValue.setter
    def CustomEtherHeaderValue(self, value):
        self._set_attribute('customEtherHeaderValue', value)

    @property
    def CustomEtherType(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the custom Ether Type. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute('customEtherType')
    @CustomEtherType.setter
    def CustomEtherType(self, value):
        self._set_attribute('customEtherType', value)

    @property
    def CustomIpHeaderLength(self):
        """DEPRECATED 
        Returns
        -------
        - number: Specifies the custom Header length in bytes.
        """
        return self._get_attribute('customIpHeaderLength')
    @CustomIpHeaderLength.setter
    def CustomIpHeaderLength(self, value):
        self._set_attribute('customIpHeaderLength', value)

    @property
    def CustomIpHeaderValue(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the Custom Header value.
        """
        return self._get_attribute('customIpHeaderValue')
    @CustomIpHeaderValue.setter
    def CustomIpHeaderValue(self, value):
        self._set_attribute('customIpHeaderValue', value)

    @property
    def CustomIpProtocol(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the custom IP Protocol for the Source Traffic Endpoints. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute('customIpProtocol')
    @CustomIpProtocol.setter
    def CustomIpProtocol(self, value):
        self._set_attribute('customIpProtocol', value)

    @property
    def DestinationPort(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the transport destination port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute('destinationPort')
    @DestinationPort.setter
    def DestinationPort(self, value):
        self._set_attribute('destinationPort', value)

    @property
    def EnableMacInMac(self):
        """DEPRECATED 
        Returns
        -------
        - bool: Enables the PBB-specific fields.
        """
        return self._get_attribute('enableMacInMac')
    @EnableMacInMac.setter
    def EnableMacInMac(self, value):
        self._set_attribute('enableMacInMac', value)

    @property
    def EnableVlan(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If enabled, VLAN is available.
        """
        return self._get_attribute('enableVlan')
    @EnableVlan.setter
    def EnableVlan(self, value):
        self._set_attribute('enableVlan', value)

    @property
    def EtherType(self):
        """DEPRECATED 
        Returns
        -------
        - str(custom | ipv4 | ipv6 | mplsUnicast): Specifies the Ether Type to be used.
        """
        return self._get_attribute('etherType')
    @EtherType.setter
    def EtherType(self, value):
        self._set_attribute('etherType', value)

    @property
    def GatewayMac(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the Gateway MAC address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute('gatewayMac')
    @GatewayMac.setter
    def GatewayMac(self, value):
        self._set_attribute('gatewayMac', value)

    @property
    def IpAddress(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the IPv4 address of the Source Traffic Endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute('ipAddress')
    @IpAddress.setter
    def IpAddress(self, value):
        self._set_attribute('ipAddress', value)

    @property
    def IpMask(self):
        """DEPRECATED 
        Returns
        -------
        - number: Specifies the Mask value.
        """
        return self._get_attribute('ipMask')
    @IpMask.setter
    def IpMask(self, value):
        self._set_attribute('ipMask', value)

    @property
    def IpProtocol(self):
        """DEPRECATED 
        Returns
        -------
        - str(custom | tcp | udp): Specifies the IP Protocol to be used.
        """
        return self._get_attribute('ipProtocol')
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute('ipProtocol', value)

    @property
    def IpTos(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the Terms of Service of the IP Protocol. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute('ipTos')
    @IpTos.setter
    def IpTos(self, value):
        self._set_attribute('ipTos', value)

    @property
    def Ipv4Dscp(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies value of Ipv4 DSCP field.
        """
        return self._get_attribute('ipv4Dscp')
    @Ipv4Dscp.setter
    def Ipv4Dscp(self, value):
        self._set_attribute('ipv4Dscp', value)

    @property
    def Ipv4Ecn(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the IPv4 ECN field, which is actually the last 2 bits of ToS field.
        """
        return self._get_attribute('ipv4Ecn')
    @Ipv4Ecn.setter
    def Ipv4Ecn(self, value):
        self._set_attribute('ipv4Ecn', value)

    @property
    def Ipv6Address(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the IPv6 address to be used in the traffic endpoint.
        """
        return self._get_attribute('ipv6Address')
    @Ipv6Address.setter
    def Ipv6Address(self, value):
        self._set_attribute('ipv6Address', value)

    @property
    def Ipv6AddressMask(self):
        """DEPRECATED 
        Returns
        -------
        - number: Specifies the mask of IPv6 address
        """
        return self._get_attribute('ipv6AddressMask')
    @Ipv6AddressMask.setter
    def Ipv6AddressMask(self, value):
        self._set_attribute('ipv6AddressMask', value)

    @property
    def Ipv6CustomHeaderLength(self):
        """DEPRECATED 
        Returns
        -------
        - number: Specifies the IPv6 custom header length. This indicates the number of bytes in the field IPv6 custom header Value.
        """
        return self._get_attribute('ipv6CustomHeaderLength')
    @Ipv6CustomHeaderLength.setter
    def Ipv6CustomHeaderLength(self, value):
        self._set_attribute('ipv6CustomHeaderLength', value)

    @property
    def Ipv6CustomHeaderValue(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the IPv6 custom header value. This is populated with hexadecimal byte string containing the protocol header content.
        """
        return self._get_attribute('ipv6CustomHeaderValue')
    @Ipv6CustomHeaderValue.setter
    def Ipv6CustomHeaderValue(self, value):
        self._set_attribute('ipv6CustomHeaderValue', value)

    @property
    def Ipv6CustomNextHeader(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the custom IPv6 Next header. This has dependency on the field IPv6 Next Header which should be set to custom. It actually specifies the protocol type of header, the actual content and length of protocol header is specified in other fields. Using this custom header, user can send any other protocol header except TCP/UDP.
        """
        return self._get_attribute('ipv6CustomNextHeader')
    @Ipv6CustomNextHeader.setter
    def Ipv6CustomNextHeader(self, value):
        self._set_attribute('ipv6CustomNextHeader', value)

    @property
    def Ipv6Dscp(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the IPv6 DSCP field. This is the set of first 6 bits of the ToS field.
        """
        return self._get_attribute('ipv6Dscp')
    @Ipv6Dscp.setter
    def Ipv6Dscp(self, value):
        self._set_attribute('ipv6Dscp', value)

    @property
    def Ipv6Ecn(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the IPv6 ECN field, which is actually the last 2 bits of ToS field.
        """
        return self._get_attribute('ipv6Ecn')
    @Ipv6Ecn.setter
    def Ipv6Ecn(self, value):
        self._set_attribute('ipv6Ecn', value)

    @property
    def Ipv6FlowLabel(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the IPv6 flow label field.
        """
        return self._get_attribute('ipv6FlowLabel')
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute('ipv6FlowLabel', value)

    @property
    def Ipv6NextHeader(self):
        """DEPRECATED 
        Returns
        -------
        - str(custom | tcp | udp): Specifies the IPv6 Next header. It can be TCP, UDP or a custom header.
        """
        return self._get_attribute('ipv6NextHeader')
    @Ipv6NextHeader.setter
    def Ipv6NextHeader(self, value):
        self._set_attribute('ipv6NextHeader', value)

    @property
    def MacAddress(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the MAC Address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute('macAddress')
    @MacAddress.setter
    def MacAddress(self, value):
        self._set_attribute('macAddress', value)

    @property
    def MplsInnerMacSource(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the Inner MAC source of MPLS. Applicable when the MPLS payload type is ethernet.
        """
        return self._get_attribute('mplsInnerMacSource')
    @MplsInnerMacSource.setter
    def MplsInnerMacSource(self, value):
        self._set_attribute('mplsInnerMacSource', value)

    @property
    def MplsInnerVlanId(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the inner VLAN ID. Applicable when the MPLS payload type is ethernet.
        """
        return self._get_attribute('mplsInnerVlanId')
    @MplsInnerVlanId.setter
    def MplsInnerVlanId(self, value):
        self._set_attribute('mplsInnerVlanId', value)

    @property
    def MplsInnerVlanPriority(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the Inner VLAN priority. Applicable when the MPLS payload type is ethernet.
        """
        return self._get_attribute('mplsInnerVlanPriority')
    @MplsInnerVlanPriority.setter
    def MplsInnerVlanPriority(self, value):
        self._set_attribute('mplsInnerVlanPriority', value)

    @property
    def MplsLabel(self):
        """DEPRECATED 
        Returns
        -------
        - str: Value of the MPLS label field.
        """
        return self._get_attribute('mplsLabel')
    @MplsLabel.setter
    def MplsLabel(self, value):
        self._set_attribute('mplsLabel', value)

    @property
    def MplsLabelStackSize(self):
        """DEPRECATED 
        Returns
        -------
        - number: Specifies the MPLS label stack size. Indicates the number of MPLS tage that are appended. Can take a max of 3.
        """
        return self._get_attribute('mplsLabelStackSize')
    @MplsLabelStackSize.setter
    def MplsLabelStackSize(self, value):
        self._set_attribute('mplsLabelStackSize', value)

    @property
    def MplsPayloadType(self):
        """DEPRECATED 
        Returns
        -------
        - str(ethernet | ipv4 | ipv6): Specifies the payload type in MPLS. Can be IPv4/IPv6 (L3) or Ethernet (L2).
        """
        return self._get_attribute('mplsPayloadType')
    @MplsPayloadType.setter
    def MplsPayloadType(self, value):
        self._set_attribute('mplsPayloadType', value)

    @property
    def MplsTrafficClass(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the MPLS traffic class.
        """
        return self._get_attribute('mplsTrafficClass')
    @MplsTrafficClass.setter
    def MplsTrafficClass(self, value):
        self._set_attribute('mplsTrafficClass', value)

    @property
    def Name(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the name of the Traffic endpoint.
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def PbbDestinamtionMac(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the B-Destination MAC.
        """
        return self._get_attribute('pbbDestinamtionMac')
    @PbbDestinamtionMac.setter
    def PbbDestinamtionMac(self, value):
        self._set_attribute('pbbDestinamtionMac', value)

    @property
    def PbbEtherType(self):
        """DEPRECATED 
        Returns
        -------
        - str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200): Specifies the B-Ether Type.
        """
        return self._get_attribute('pbbEtherType')
    @PbbEtherType.setter
    def PbbEtherType(self, value):
        self._set_attribute('pbbEtherType', value)

    @property
    def PbbIsId(self):
        """DEPRECATED 
        Returns
        -------
        - str: Value of the PBB I-SID field.
        """
        return self._get_attribute('pbbIsId')
    @PbbIsId.setter
    def PbbIsId(self, value):
        self._set_attribute('pbbIsId', value)

    @property
    def PbbSourceMac(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the B-Source MAC.
        """
        return self._get_attribute('pbbSourceMac')
    @PbbSourceMac.setter
    def PbbSourceMac(self, value):
        self._set_attribute('pbbSourceMac', value)

    @property
    def PbbVlanId(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the B-VLAN ID.
        """
        return self._get_attribute('pbbVlanId')
    @PbbVlanId.setter
    def PbbVlanId(self, value):
        self._set_attribute('pbbVlanId', value)

    @property
    def PbbVlanPcp(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the B-VLAN priority.
        """
        return self._get_attribute('pbbVlanPcp')
    @PbbVlanPcp.setter
    def PbbVlanPcp(self, value):
        self._set_attribute('pbbVlanPcp', value)

    @property
    def ProtocolInterface(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): Specifies the name of the protocol interface being used for this OpenFlow configuration.
        """
        return self._get_attribute('protocolInterface')
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute('protocolInterface', value)

    @property
    def RangeSize(self):
        """DEPRECATED 
        Returns
        -------
        - number: Specifies the size of the traffic range.
        """
        return self._get_attribute('rangeSize')
    @RangeSize.setter
    def RangeSize(self, value):
        self._set_attribute('rangeSize', value)

    @property
    def SourcePort(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the transport source port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute('sourcePort')
    @SourcePort.setter
    def SourcePort(self, value):
        self._set_attribute('sourcePort', value)

    @property
    def UdpDestination(self):
        """DEPRECATED 
        Returns
        -------
        - str: Value of the UDP destination field.
        """
        return self._get_attribute('udpDestination')
    @UdpDestination.setter
    def UdpDestination(self, value):
        self._set_attribute('udpDestination', value)

    @property
    def UdpSource(self):
        """DEPRECATED 
        Returns
        -------
        - str: Value of the UDP source field.
        """
        return self._get_attribute('udpSource')
    @UdpSource.setter
    def UdpSource(self, value):
        self._set_attribute('udpSource', value)

    @property
    def VlanCount(self):
        """DEPRECATED 
        Returns
        -------
        - number: Specifies the VLAN Count.
        """
        return self._get_attribute('vlanCount')
    @VlanCount.setter
    def VlanCount(self, value):
        self._set_attribute('vlanCount', value)

    @property
    def VlanId(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the VLAN ID. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute('vlanId')
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute('vlanId', value)

    @property
    def VlanPriority(self):
        """DEPRECATED 
        Returns
        -------
        - str: Specifies the VLAN Priority. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        """
        return self._get_attribute('vlanPriority')
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute('vlanPriority', value)

    def update(self, ArpViaInterface=None, CustomEtherHeaderLength=None, CustomEtherHeaderValue=None, CustomEtherType=None, CustomIpHeaderLength=None, CustomIpHeaderValue=None, CustomIpProtocol=None, DestinationPort=None, EnableMacInMac=None, EnableVlan=None, EtherType=None, GatewayMac=None, IpAddress=None, IpMask=None, IpProtocol=None, IpTos=None, Ipv4Dscp=None, Ipv4Ecn=None, Ipv6Address=None, Ipv6AddressMask=None, Ipv6CustomHeaderLength=None, Ipv6CustomHeaderValue=None, Ipv6CustomNextHeader=None, Ipv6Dscp=None, Ipv6Ecn=None, Ipv6FlowLabel=None, Ipv6NextHeader=None, MacAddress=None, MplsInnerMacSource=None, MplsInnerVlanId=None, MplsInnerVlanPriority=None, MplsLabel=None, MplsLabelStackSize=None, MplsPayloadType=None, MplsTrafficClass=None, Name=None, PbbDestinamtionMac=None, PbbEtherType=None, PbbIsId=None, PbbSourceMac=None, PbbVlanId=None, PbbVlanPcp=None, ProtocolInterface=None, RangeSize=None, SourcePort=None, UdpDestination=None, UdpSource=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Updates trafficEndPoint resource on the server.

        Args
        ----
        - ArpViaInterface (bool): If true, ARP request is conveyed through an Interface.
        - CustomEtherHeaderLength (number): Specifies the Custom Header length in bytes.
        - CustomEtherHeaderValue (str): Specifies the Custom ether Header value.
        - CustomEtherType (str): Specifies the custom Ether Type. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - CustomIpHeaderLength (number): Specifies the custom Header length in bytes.
        - CustomIpHeaderValue (str): Specifies the Custom Header value.
        - CustomIpProtocol (str): Specifies the custom IP Protocol for the Source Traffic Endpoints. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - DestinationPort (str): Specifies the transport destination port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EnableMacInMac (bool): Enables the PBB-specific fields.
        - EnableVlan (bool): If enabled, VLAN is available.
        - EtherType (str(custom | ipv4 | ipv6 | mplsUnicast)): Specifies the Ether Type to be used.
        - GatewayMac (str): Specifies the Gateway MAC address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpAddress (str): Specifies the IPv4 address of the Source Traffic Endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpMask (number): Specifies the Mask value.
        - IpProtocol (str(custom | tcp | udp)): Specifies the IP Protocol to be used.
        - IpTos (str): Specifies the Terms of Service of the IP Protocol. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Dscp (str): Specifies value of Ipv4 DSCP field.
        - Ipv4Ecn (str): Specifies the IPv4 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6Address (str): Specifies the IPv6 address to be used in the traffic endpoint.
        - Ipv6AddressMask (number): Specifies the mask of IPv6 address
        - Ipv6CustomHeaderLength (number): Specifies the IPv6 custom header length. This indicates the number of bytes in the field IPv6 custom header Value.
        - Ipv6CustomHeaderValue (str): Specifies the IPv6 custom header value. This is populated with hexadecimal byte string containing the protocol header content.
        - Ipv6CustomNextHeader (str): Specifies the custom IPv6 Next header. This has dependency on the field IPv6 Next Header which should be set to custom. It actually specifies the protocol type of header, the actual content and length of protocol header is specified in other fields. Using this custom header, user can send any other protocol header except TCP/UDP.
        - Ipv6Dscp (str): Specifies the IPv6 DSCP field. This is the set of first 6 bits of the ToS field.
        - Ipv6Ecn (str): Specifies the IPv6 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6FlowLabel (str): Specifies the IPv6 flow label field.
        - Ipv6NextHeader (str(custom | tcp | udp)): Specifies the IPv6 Next header. It can be TCP, UDP or a custom header.
        - MacAddress (str): Specifies the MAC Address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - MplsInnerMacSource (str): Specifies the Inner MAC source of MPLS. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanId (str): Specifies the inner VLAN ID. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanPriority (str): Specifies the Inner VLAN priority. Applicable when the MPLS payload type is ethernet.
        - MplsLabel (str): Value of the MPLS label field.
        - MplsLabelStackSize (number): Specifies the MPLS label stack size. Indicates the number of MPLS tage that are appended. Can take a max of 3.
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): Specifies the payload type in MPLS. Can be IPv4/IPv6 (L3) or Ethernet (L2).
        - MplsTrafficClass (str): Specifies the MPLS traffic class.
        - Name (str): Specifies the name of the Traffic endpoint.
        - PbbDestinamtionMac (str): Specifies the B-Destination MAC.
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): Specifies the B-Ether Type.
        - PbbIsId (str): Value of the PBB I-SID field.
        - PbbSourceMac (str): Specifies the B-Source MAC.
        - PbbVlanId (str): Specifies the B-VLAN ID.
        - PbbVlanPcp (str): Specifies the B-VLAN priority.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): Specifies the name of the protocol interface being used for this OpenFlow configuration.
        - RangeSize (number): Specifies the size of the traffic range.
        - SourcePort (str): Specifies the transport source port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - UdpDestination (str): Value of the UDP destination field.
        - UdpSource (str): Value of the UDP source field.
        - VlanCount (number): Specifies the VLAN Count.
        - VlanId (str): Specifies the VLAN ID. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanPriority (str): Specifies the VLAN Priority. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, ArpViaInterface=None, CustomEtherHeaderLength=None, CustomEtherHeaderValue=None, CustomEtherType=None, CustomIpHeaderLength=None, CustomIpHeaderValue=None, CustomIpProtocol=None, DestinationPort=None, EnableMacInMac=None, EnableVlan=None, EtherType=None, GatewayMac=None, IpAddress=None, IpMask=None, IpProtocol=None, IpTos=None, Ipv4Dscp=None, Ipv4Ecn=None, Ipv6Address=None, Ipv6AddressMask=None, Ipv6CustomHeaderLength=None, Ipv6CustomHeaderValue=None, Ipv6CustomNextHeader=None, Ipv6Dscp=None, Ipv6Ecn=None, Ipv6FlowLabel=None, Ipv6NextHeader=None, MacAddress=None, MplsInnerMacSource=None, MplsInnerVlanId=None, MplsInnerVlanPriority=None, MplsLabel=None, MplsLabelStackSize=None, MplsPayloadType=None, MplsTrafficClass=None, Name=None, PbbDestinamtionMac=None, PbbEtherType=None, PbbIsId=None, PbbSourceMac=None, PbbVlanId=None, PbbVlanPcp=None, ProtocolInterface=None, RangeSize=None, SourcePort=None, UdpDestination=None, UdpSource=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Adds a new trafficEndPoint resource on the server and adds it to the container.

        Args
        ----
        - ArpViaInterface (bool): If true, ARP request is conveyed through an Interface.
        - CustomEtherHeaderLength (number): Specifies the Custom Header length in bytes.
        - CustomEtherHeaderValue (str): Specifies the Custom ether Header value.
        - CustomEtherType (str): Specifies the custom Ether Type. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - CustomIpHeaderLength (number): Specifies the custom Header length in bytes.
        - CustomIpHeaderValue (str): Specifies the Custom Header value.
        - CustomIpProtocol (str): Specifies the custom IP Protocol for the Source Traffic Endpoints. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - DestinationPort (str): Specifies the transport destination port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EnableMacInMac (bool): Enables the PBB-specific fields.
        - EnableVlan (bool): If enabled, VLAN is available.
        - EtherType (str(custom | ipv4 | ipv6 | mplsUnicast)): Specifies the Ether Type to be used.
        - GatewayMac (str): Specifies the Gateway MAC address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpAddress (str): Specifies the IPv4 address of the Source Traffic Endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpMask (number): Specifies the Mask value.
        - IpProtocol (str(custom | tcp | udp)): Specifies the IP Protocol to be used.
        - IpTos (str): Specifies the Terms of Service of the IP Protocol. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Dscp (str): Specifies value of Ipv4 DSCP field.
        - Ipv4Ecn (str): Specifies the IPv4 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6Address (str): Specifies the IPv6 address to be used in the traffic endpoint.
        - Ipv6AddressMask (number): Specifies the mask of IPv6 address
        - Ipv6CustomHeaderLength (number): Specifies the IPv6 custom header length. This indicates the number of bytes in the field IPv6 custom header Value.
        - Ipv6CustomHeaderValue (str): Specifies the IPv6 custom header value. This is populated with hexadecimal byte string containing the protocol header content.
        - Ipv6CustomNextHeader (str): Specifies the custom IPv6 Next header. This has dependency on the field IPv6 Next Header which should be set to custom. It actually specifies the protocol type of header, the actual content and length of protocol header is specified in other fields. Using this custom header, user can send any other protocol header except TCP/UDP.
        - Ipv6Dscp (str): Specifies the IPv6 DSCP field. This is the set of first 6 bits of the ToS field.
        - Ipv6Ecn (str): Specifies the IPv6 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6FlowLabel (str): Specifies the IPv6 flow label field.
        - Ipv6NextHeader (str(custom | tcp | udp)): Specifies the IPv6 Next header. It can be TCP, UDP or a custom header.
        - MacAddress (str): Specifies the MAC Address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - MplsInnerMacSource (str): Specifies the Inner MAC source of MPLS. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanId (str): Specifies the inner VLAN ID. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanPriority (str): Specifies the Inner VLAN priority. Applicable when the MPLS payload type is ethernet.
        - MplsLabel (str): Value of the MPLS label field.
        - MplsLabelStackSize (number): Specifies the MPLS label stack size. Indicates the number of MPLS tage that are appended. Can take a max of 3.
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): Specifies the payload type in MPLS. Can be IPv4/IPv6 (L3) or Ethernet (L2).
        - MplsTrafficClass (str): Specifies the MPLS traffic class.
        - Name (str): Specifies the name of the Traffic endpoint.
        - PbbDestinamtionMac (str): Specifies the B-Destination MAC.
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): Specifies the B-Ether Type.
        - PbbIsId (str): Value of the PBB I-SID field.
        - PbbSourceMac (str): Specifies the B-Source MAC.
        - PbbVlanId (str): Specifies the B-VLAN ID.
        - PbbVlanPcp (str): Specifies the B-VLAN priority.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): Specifies the name of the protocol interface being used for this OpenFlow configuration.
        - RangeSize (number): Specifies the size of the traffic range.
        - SourcePort (str): Specifies the transport source port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - UdpDestination (str): Value of the UDP destination field.
        - UdpSource (str): Value of the UDP source field.
        - VlanCount (number): Specifies the VLAN Count.
        - VlanId (str): Specifies the VLAN ID. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanPriority (str): Specifies the VLAN Priority. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.

        Returns
        -------
        - self: This instance with all currently retrieved trafficEndPoint resources using find and the newly added trafficEndPoint resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained trafficEndPoint resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ArpViaInterface=None, CustomEtherHeaderLength=None, CustomEtherHeaderValue=None, CustomEtherType=None, CustomIpHeaderLength=None, CustomIpHeaderValue=None, CustomIpProtocol=None, DestinationPort=None, EnableMacInMac=None, EnableVlan=None, EtherType=None, GatewayMac=None, IpAddress=None, IpMask=None, IpProtocol=None, IpTos=None, Ipv4Dscp=None, Ipv4Ecn=None, Ipv6Address=None, Ipv6AddressMask=None, Ipv6CustomHeaderLength=None, Ipv6CustomHeaderValue=None, Ipv6CustomNextHeader=None, Ipv6Dscp=None, Ipv6Ecn=None, Ipv6FlowLabel=None, Ipv6NextHeader=None, MacAddress=None, MplsInnerMacSource=None, MplsInnerVlanId=None, MplsInnerVlanPriority=None, MplsLabel=None, MplsLabelStackSize=None, MplsPayloadType=None, MplsTrafficClass=None, Name=None, PbbDestinamtionMac=None, PbbEtherType=None, PbbIsId=None, PbbSourceMac=None, PbbVlanId=None, PbbVlanPcp=None, ProtocolInterface=None, RangeSize=None, SourcePort=None, UdpDestination=None, UdpSource=None, VlanCount=None, VlanId=None, VlanPriority=None):
        """Finds and retrieves trafficEndPoint resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trafficEndPoint resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trafficEndPoint resources from the server.

        Args
        ----
        - ArpViaInterface (bool): If true, ARP request is conveyed through an Interface.
        - CustomEtherHeaderLength (number): Specifies the Custom Header length in bytes.
        - CustomEtherHeaderValue (str): Specifies the Custom ether Header value.
        - CustomEtherType (str): Specifies the custom Ether Type. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - CustomIpHeaderLength (number): Specifies the custom Header length in bytes.
        - CustomIpHeaderValue (str): Specifies the Custom Header value.
        - CustomIpProtocol (str): Specifies the custom IP Protocol for the Source Traffic Endpoints. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - DestinationPort (str): Specifies the transport destination port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - EnableMacInMac (bool): Enables the PBB-specific fields.
        - EnableVlan (bool): If enabled, VLAN is available.
        - EtherType (str(custom | ipv4 | ipv6 | mplsUnicast)): Specifies the Ether Type to be used.
        - GatewayMac (str): Specifies the Gateway MAC address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpAddress (str): Specifies the IPv4 address of the Source Traffic Endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - IpMask (number): Specifies the Mask value.
        - IpProtocol (str(custom | tcp | udp)): Specifies the IP Protocol to be used.
        - IpTos (str): Specifies the Terms of Service of the IP Protocol. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - Ipv4Dscp (str): Specifies value of Ipv4 DSCP field.
        - Ipv4Ecn (str): Specifies the IPv4 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6Address (str): Specifies the IPv6 address to be used in the traffic endpoint.
        - Ipv6AddressMask (number): Specifies the mask of IPv6 address
        - Ipv6CustomHeaderLength (number): Specifies the IPv6 custom header length. This indicates the number of bytes in the field IPv6 custom header Value.
        - Ipv6CustomHeaderValue (str): Specifies the IPv6 custom header value. This is populated with hexadecimal byte string containing the protocol header content.
        - Ipv6CustomNextHeader (str): Specifies the custom IPv6 Next header. This has dependency on the field IPv6 Next Header which should be set to custom. It actually specifies the protocol type of header, the actual content and length of protocol header is specified in other fields. Using this custom header, user can send any other protocol header except TCP/UDP.
        - Ipv6Dscp (str): Specifies the IPv6 DSCP field. This is the set of first 6 bits of the ToS field.
        - Ipv6Ecn (str): Specifies the IPv6 ECN field, which is actually the last 2 bits of ToS field.
        - Ipv6FlowLabel (str): Specifies the IPv6 flow label field.
        - Ipv6NextHeader (str(custom | tcp | udp)): Specifies the IPv6 Next header. It can be TCP, UDP or a custom header.
        - MacAddress (str): Specifies the MAC Address of the source traffic endpoint. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - MplsInnerMacSource (str): Specifies the Inner MAC source of MPLS. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanId (str): Specifies the inner VLAN ID. Applicable when the MPLS payload type is ethernet.
        - MplsInnerVlanPriority (str): Specifies the Inner VLAN priority. Applicable when the MPLS payload type is ethernet.
        - MplsLabel (str): Value of the MPLS label field.
        - MplsLabelStackSize (number): Specifies the MPLS label stack size. Indicates the number of MPLS tage that are appended. Can take a max of 3.
        - MplsPayloadType (str(ethernet | ipv4 | ipv6)): Specifies the payload type in MPLS. Can be IPv4/IPv6 (L3) or Ethernet (L2).
        - MplsTrafficClass (str): Specifies the MPLS traffic class.
        - Name (str): Specifies the name of the Traffic endpoint.
        - PbbDestinamtionMac (str): Specifies the B-Destination MAC.
        - PbbEtherType (str(bEtherType8100 | bEtherType88A8 | bEtherType88E7 | bEtherType9100 | bEtherType9200)): Specifies the B-Ether Type.
        - PbbIsId (str): Value of the PBB I-SID field.
        - PbbSourceMac (str): Specifies the B-Source MAC.
        - PbbVlanId (str): Specifies the B-VLAN ID.
        - PbbVlanPcp (str): Specifies the B-VLAN priority.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): Specifies the name of the protocol interface being used for this OpenFlow configuration.
        - RangeSize (number): Specifies the size of the traffic range.
        - SourcePort (str): Specifies the transport source port. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - UdpDestination (str): Value of the UDP destination field.
        - UdpSource (str): Value of the UDP source field.
        - VlanCount (number): Specifies the VLAN Count.
        - VlanId (str): Specifies the VLAN ID. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.
        - VlanPriority (str): Specifies the VLAN Priority. This attribute is of range kind and can take wildcard as input. It is composed of sub-attributes like, startValue, stepValue, repeatCount, wrapCount, and incrementMode.

        Returns
        -------
        - self: This instance with matching trafficEndPoint resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of trafficEndPoint data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trafficEndPoint resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
