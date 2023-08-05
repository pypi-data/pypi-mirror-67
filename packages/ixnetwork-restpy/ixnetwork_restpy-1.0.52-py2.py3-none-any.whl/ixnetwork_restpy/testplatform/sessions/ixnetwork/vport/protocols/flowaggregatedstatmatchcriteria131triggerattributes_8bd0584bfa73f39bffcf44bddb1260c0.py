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


class FlowAggregatedStatMatchCriteria131TriggerAttributes(Base):
    """This object allows to configure the Flow stat trigger match criteria for controller version 1.3.1.
    The FlowAggregatedStatMatchCriteria131TriggerAttributes class encapsulates a required flowAggregatedStatMatchCriteria131TriggerAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'flowAggregatedStatMatchCriteria131TriggerAttributes'

    def __init__(self, parent):
        super(FlowAggregatedStatMatchCriteria131TriggerAttributes, self).__init__(parent)

    @property
    def ArpDstHwAddr(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): Value of the ARP destination hardware address.
        """
        return self._get_attribute('arpDstHwAddr')
    @ArpDstHwAddr.setter
    def ArpDstHwAddr(self, value):
        self._set_attribute('arpDstHwAddr', value)

    @property
    def ArpDstIpv4Addr(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): The ARP destination IPv4 address field value.
        """
        return self._get_attribute('arpDstIpv4Addr')
    @ArpDstIpv4Addr.setter
    def ArpDstIpv4Addr(self, value):
        self._set_attribute('arpDstIpv4Addr', value)

    @property
    def ArpOpcode(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): Value of the ARP opcode field.
        """
        return self._get_attribute('arpOpcode')
    @ArpOpcode.setter
    def ArpOpcode(self, value):
        self._set_attribute('arpOpcode', value)

    @property
    def ArpSrcHwAddr(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): Value of the ARP source hardware address.
        """
        return self._get_attribute('arpSrcHwAddr')
    @ArpSrcHwAddr.setter
    def ArpSrcHwAddr(self, value):
        self._set_attribute('arpSrcHwAddr', value)

    @property
    def ArpSrcIpv4Addr(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): The ARP source IPv4 address field value.
        """
        return self._get_attribute('arpSrcIpv4Addr')
    @ArpSrcIpv4Addr.setter
    def ArpSrcIpv4Addr(self, value):
        self._set_attribute('arpSrcIpv4Addr', value)

    @property
    def Cookie(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): The Cookie field value.
        """
        return self._get_attribute('cookie')
    @Cookie.setter
    def Cookie(self, value):
        self._set_attribute('cookie', value)

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): The Ethernet destination address.
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
        - dict(arg1:str,arg2:str): The Ethernet source address.
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
        - dict(arg1:str,arg2:str): The type of Ethernet port used.
        """
        return self._get_attribute('ethernetType')
    @EthernetType.setter
    def EthernetType(self, value):
        self._set_attribute('ethernetType', value)

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): The experimenter data field value.
        """
        return self._get_attribute('experimenterData')
    @ExperimenterData.setter
    def ExperimenterData(self, value):
        self._set_attribute('experimenterData', value)

    @property
    def ExperimenterDataLength(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:str): Value of the Experimenter data length field.
        """
        return self._get_attribute('experimenterDataLength')
    @ExperimenterDataLength.setter
    def ExperimenterDataLength(self, value):
        self._set_attribute('experimenterDataLength', value)

    @property
    def ExperimenterField(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:str): Value of the Experimenter Field field.
        """
        return self._get_attribute('experimenterField')
    @ExperimenterField.setter
    def ExperimenterField(self, value):
        self._set_attribute('experimenterField', value)

    @property
    def ExperimenterHashmask(self):
        """
        Returns
        -------
        - dict(arg1:bool,arg2:str): The experimented hasmask field value.
        """
        return self._get_attribute('experimenterHashmask')
    @ExperimenterHashmask.setter
    def ExperimenterHashmask(self, value):
        self._set_attribute('experimenterHashmask', value)

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): Value of the experimenter ID field.
        """
        return self._get_attribute('experimenterId')
    @ExperimenterId.setter
    def ExperimenterId(self, value):
        self._set_attribute('experimenterId', value)

    @property
    def Icmpv4Code(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): The code of ICMPv4 port used.
        """
        return self._get_attribute('icmpv4Code')
    @Icmpv4Code.setter
    def Icmpv4Code(self, value):
        self._set_attribute('icmpv4Code', value)

    @property
    def Icmpv4Type(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): The type of ICMPv4 port used.
        """
        return self._get_attribute('icmpv4Type')
    @Icmpv4Type.setter
    def Icmpv4Type(self, value):
        self._set_attribute('icmpv4Type', value)

    @property
    def Icmpv6Code(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): Value of the ICMPv6 code field.
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
        - dict(arg1:str,arg2:str): Value of the ICMPv6 type field.
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
        - dict(arg1:str,arg2:str): The input port used.
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
        - dict(arg1:str,arg2:str): The IP DSCP value for advertising.
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
        - dict(arg1:str,arg2:str): The IP ECN field value.
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
        - dict(arg1:str,arg2:str): The IP protocol used.
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
        - dict(arg1:str,arg2:str): The IPv4 destination address.
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
        - dict(arg1:str,arg2:str): The IPv4 source address.
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
        - dict(arg1:str,arg2:str): Value of the IPv6 destination field.
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
        - dict(arg1:str,arg2:str): The Ipv6 extension header field value.
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
        - dict(arg1:str,arg2:str): Value of the IPv6 flow label field.
        """
        return self._get_attribute('ipv6FlowLabel')
    @Ipv6FlowLabel.setter
    def Ipv6FlowLabel(self, value):
        self._set_attribute('ipv6FlowLabel', value)

    @property
    def Ipv6NdDll(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): The IPv6 ND DLL field value.
        """
        return self._get_attribute('ipv6NdDll')
    @Ipv6NdDll.setter
    def Ipv6NdDll(self, value):
        self._set_attribute('ipv6NdDll', value)

    @property
    def Ipv6NdSll(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): Value of the Ipv6 ND SLL field.
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
        - dict(arg1:str,arg2:str): Value of the IPv6 ND target field.
        """
        return self._get_attribute('ipv6NdTarget')
    @Ipv6NdTarget.setter
    def Ipv6NdTarget(self, value):
        self._set_attribute('ipv6NdTarget', value)

    @property
    def Ipv6Source(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): Value of the IPv6 source field.
        """
        return self._get_attribute('ipv6Source')
    @Ipv6Source.setter
    def Ipv6Source(self, value):
        self._set_attribute('ipv6Source', value)

    @property
    def MetaData(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): Value of the metadata field.
        """
        return self._get_attribute('metaData')
    @MetaData.setter
    def MetaData(self, value):
        self._set_attribute('metaData', value)

    @property
    def MplsBos(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): Value of the MPLS BoS field.
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
        - dict(arg1:str,arg2:str): Value of the MPLS label field.
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
        - dict(arg1:str,arg2:str): Value of the MPLS TC field.
        """
        return self._get_attribute('mplsTc')
    @MplsTc.setter
    def MplsTc(self, value):
        self._set_attribute('mplsTc', value)

    @property
    def PbbISid(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): Value of the PBB I-SID field.
        """
        return self._get_attribute('pbbISid')
    @PbbISid.setter
    def PbbISid(self, value):
        self._set_attribute('pbbISid', value)

    @property
    def PhysicalInPort(self):
        """
        Returns
        -------
        - dict(arg1:str,arg2:str): Value of the Physical IN port field.
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
        - dict(arg1:str,arg2:str): The SCTP destination field value.
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
        - dict(arg1:str,arg2:str): Value of the SCTP destination field.
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
        - dict(arg1:str,arg2:str): The Transport destination address.
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
        - dict(arg1:str,arg2:str): Value of the TCP source field.
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
        - dict(arg1:str,arg2:str): Value of the tunnel ID field.
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
        - dict(arg1:str,arg2:str): Value of the UDP destination field.
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
        - dict(arg1:str,arg2:str): Value of the UDP source field.
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
        - dict(arg1:str,arg2:str): The unique VLAN Identifier.
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
        - dict(arg1:str,arg2:str): The User Priority for this VLAN.
        """
        return self._get_attribute('vlanPriority')
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute('vlanPriority', value)

    def update(self, ArpDstHwAddr=None, ArpDstIpv4Addr=None, ArpOpcode=None, ArpSrcHwAddr=None, ArpSrcIpv4Addr=None, Cookie=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterField=None, ExperimenterHashmask=None, ExperimenterId=None, Icmpv4Code=None, Icmpv4Type=None, Icmpv6Code=None, Icmpv6Type=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdDll=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6Source=None, MetaData=None, MplsBos=None, MplsLabel=None, MplsTc=None, PbbISid=None, PhysicalInPort=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
        """Updates flowAggregatedStatMatchCriteria131TriggerAttributes resource on the server.

        Args
        ----
        - ArpDstHwAddr (dict(arg1:str,arg2:str)): Value of the ARP destination hardware address.
        - ArpDstIpv4Addr (dict(arg1:str,arg2:str)): The ARP destination IPv4 address field value.
        - ArpOpcode (dict(arg1:str,arg2:str)): Value of the ARP opcode field.
        - ArpSrcHwAddr (dict(arg1:str,arg2:str)): Value of the ARP source hardware address.
        - ArpSrcIpv4Addr (dict(arg1:str,arg2:str)): The ARP source IPv4 address field value.
        - Cookie (dict(arg1:str,arg2:str)): The Cookie field value.
        - EthernetDestination (dict(arg1:str,arg2:str)): The Ethernet destination address.
        - EthernetSource (dict(arg1:str,arg2:str)): The Ethernet source address.
        - EthernetType (dict(arg1:str,arg2:str)): The type of Ethernet port used.
        - ExperimenterData (dict(arg1:str,arg2:str)): The experimenter data field value.
        - ExperimenterDataLength (dict(arg1:number,arg2:str)): Value of the Experimenter data length field.
        - ExperimenterField (dict(arg1:number,arg2:str)): Value of the Experimenter Field field.
        - ExperimenterHashmask (dict(arg1:bool,arg2:str)): The experimented hasmask field value.
        - ExperimenterId (dict(arg1:str,arg2:str)): Value of the experimenter ID field.
        - Icmpv4Code (dict(arg1:str,arg2:str)): The code of ICMPv4 port used.
        - Icmpv4Type (dict(arg1:str,arg2:str)): The type of ICMPv4 port used.
        - Icmpv6Code (dict(arg1:str,arg2:str)): Value of the ICMPv6 code field.
        - Icmpv6Type (dict(arg1:str,arg2:str)): Value of the ICMPv6 type field.
        - InPort (dict(arg1:str,arg2:str)): The input port used.
        - IpDscp (dict(arg1:str,arg2:str)): The IP DSCP value for advertising.
        - IpEcn (dict(arg1:str,arg2:str)): The IP ECN field value.
        - IpProtocol (dict(arg1:str,arg2:str)): The IP protocol used.
        - Ipv4Destination (dict(arg1:str,arg2:str)): The IPv4 destination address.
        - Ipv4Source (dict(arg1:str,arg2:str)): The IPv4 source address.
        - Ipv6Destination (dict(arg1:str,arg2:str)): Value of the IPv6 destination field.
        - Ipv6ExtHeader (dict(arg1:str,arg2:str)): The Ipv6 extension header field value.
        - Ipv6FlowLabel (dict(arg1:str,arg2:str)): Value of the IPv6 flow label field.
        - Ipv6NdDll (dict(arg1:str,arg2:str)): The IPv6 ND DLL field value.
        - Ipv6NdSll (dict(arg1:str,arg2:str)): Value of the Ipv6 ND SLL field.
        - Ipv6NdTarget (dict(arg1:str,arg2:str)): Value of the IPv6 ND target field.
        - Ipv6Source (dict(arg1:str,arg2:str)): Value of the IPv6 source field.
        - MetaData (dict(arg1:str,arg2:str)): Value of the metadata field.
        - MplsBos (dict(arg1:str,arg2:str)): Value of the MPLS BoS field.
        - MplsLabel (dict(arg1:str,arg2:str)): Value of the MPLS label field.
        - MplsTc (dict(arg1:str,arg2:str)): Value of the MPLS TC field.
        - PbbISid (dict(arg1:str,arg2:str)): Value of the PBB I-SID field.
        - PhysicalInPort (dict(arg1:str,arg2:str)): Value of the Physical IN port field.
        - SctpDestination (dict(arg1:str,arg2:str)): The SCTP destination field value.
        - SctpSource (dict(arg1:str,arg2:str)): Value of the SCTP destination field.
        - TcpDestination (dict(arg1:str,arg2:str)): The Transport destination address.
        - TcpSource (dict(arg1:str,arg2:str)): Value of the TCP source field.
        - TunnelId (dict(arg1:str,arg2:str)): Value of the tunnel ID field.
        - UdpDestination (dict(arg1:str,arg2:str)): Value of the UDP destination field.
        - UdpSource (dict(arg1:str,arg2:str)): Value of the UDP source field.
        - VlanId (dict(arg1:str,arg2:str)): The unique VLAN Identifier.
        - VlanPriority (dict(arg1:str,arg2:str)): The User Priority for this VLAN.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
