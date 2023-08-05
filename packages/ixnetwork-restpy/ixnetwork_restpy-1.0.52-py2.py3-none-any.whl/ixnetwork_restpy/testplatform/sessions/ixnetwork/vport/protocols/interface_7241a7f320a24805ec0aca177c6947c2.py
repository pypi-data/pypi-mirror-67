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


class Interface(Base):
    """This object holds three lists associated with the Router, Route ranges and Interfaces.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def BfdCvType(self):
        """
        Returns
        -------
        - str(bfdCvTypeIpUdp | bfdCvTypePwAch): This signifies the BFD Connectivity Verification type. Possible values include:
        """
        return self._get_attribute('bfdCvType')
    @BfdCvType.setter
    def BfdCvType(self, value):
        self._set_attribute('bfdCvType', value)

    @property
    def BfdDiscriminatorEnd(self):
        """
        Returns
        -------
        - number: This signifies the last BFD Discriminator value. This value should be greater than the BFD.
        """
        return self._get_attribute('bfdDiscriminatorEnd')
    @BfdDiscriminatorEnd.setter
    def BfdDiscriminatorEnd(self, value):
        self._set_attribute('bfdDiscriminatorEnd', value)

    @property
    def BfdDiscriminatorStart(self):
        """
        Returns
        -------
        - number: This signifies the first BFD Discriminator value. The default value is 5000.
        """
        return self._get_attribute('bfdDiscriminatorStart')
    @BfdDiscriminatorStart.setter
    def BfdDiscriminatorStart(self, value):
        self._set_attribute('bfdDiscriminatorStart', value)

    @property
    def ControlChannel(self):
        """
        Returns
        -------
        - str(controlChannelRouterAlert | controlChannelPwAch): This signifies the communication control channel. Possible values include
        """
        return self._get_attribute('controlChannel')
    @ControlChannel.setter
    def ControlChannel(self, value):
        self._set_attribute('controlChannel', value)

    @property
    def DestinationAddressIpv4(self):
        """
        Returns
        -------
        - str: This signifies the destination IPv4 address.
        """
        return self._get_attribute('destinationAddressIpv4')
    @DestinationAddressIpv4.setter
    def DestinationAddressIpv4(self, value):
        self._set_attribute('destinationAddressIpv4', value)

    @property
    def DownStreamAddressType(self):
        """
        Returns
        -------
        - str(ipv4Numbered | ipv4UnNumbered | ipv6Numbered | ipv6UnNumbered): This signifies the address type of the downstream traffic. Possible values include:
        """
        return self._get_attribute('downStreamAddressType')
    @DownStreamAddressType.setter
    def DownStreamAddressType(self, value):
        self._set_attribute('downStreamAddressType', value)

    @property
    def DownStreamInterfaceAddress(self):
        """
        Returns
        -------
        - number: This signifies the interface address of the downstream traffic.
        """
        return self._get_attribute('downStreamInterfaceAddress')
    @DownStreamInterfaceAddress.setter
    def DownStreamInterfaceAddress(self, value):
        self._set_attribute('downStreamInterfaceAddress', value)

    @property
    def DownStreamIpAddress(self):
        """
        Returns
        -------
        - str: This signifies the IPv4/IPv6 address of the downstream traffic.
        """
        return self._get_attribute('downStreamIpAddress')
    @DownStreamIpAddress.setter
    def DownStreamIpAddress(self, value):
        self._set_attribute('downStreamIpAddress', value)

    @property
    def EchoRequestInterval(self):
        """
        Returns
        -------
        - number: This signifies the minimum interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        """
        return self._get_attribute('echoRequestInterval')
    @EchoRequestInterval.setter
    def EchoRequestInterval(self, value):
        self._set_attribute('echoRequestInterval', value)

    @property
    def EchoResponseTimeout(self):
        """
        Returns
        -------
        - number: This signifies the minimum tiomeout interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        """
        return self._get_attribute('echoResponseTimeout')
    @EchoResponseTimeout.setter
    def EchoResponseTimeout(self, value):
        self._set_attribute('echoResponseTimeout', value)

    @property
    def EnableDownStreamMappingTlv(self):
        """
        Returns
        -------
        - bool: This signifies the enablement of downstream mapping TLV.
        """
        return self._get_attribute('enableDownStreamMappingTlv')
    @EnableDownStreamMappingTlv.setter
    def EnableDownStreamMappingTlv(self, value):
        self._set_attribute('enableDownStreamMappingTlv', value)

    @property
    def EnableDsIflag(self):
        """
        Returns
        -------
        - bool: This signifies the activation of the DS I Flag.
        """
        return self._get_attribute('enableDsIflag')
    @EnableDsIflag.setter
    def EnableDsIflag(self, value):
        self._set_attribute('enableDsIflag', value)

    @property
    def EnableDsNflag(self):
        """
        Returns
        -------
        - bool: This signifies the activation of the DS N Flag.
        """
        return self._get_attribute('enableDsNflag')
    @EnableDsNflag.setter
    def EnableDsNflag(self, value):
        self._set_attribute('enableDsNflag', value)

    @property
    def EnableFecValidation(self):
        """
        Returns
        -------
        - bool: This signifies the selection of the check box to enable FEC validation.
        """
        return self._get_attribute('enableFecValidation')
    @EnableFecValidation.setter
    def EnableFecValidation(self, value):
        self._set_attribute('enableFecValidation', value)

    @property
    def EnablePeriodicPing(self):
        """
        Returns
        -------
        - bool: If true, the router is pinged at regular intervals.
        """
        return self._get_attribute('enablePeriodicPing')
    @EnablePeriodicPing.setter
    def EnablePeriodicPing(self, value):
        self._set_attribute('enablePeriodicPing', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, it enables or disables the simulated router.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def FlapTxIntervals(self):
        """
        Returns
        -------
        - number: This signifies the number of seconds between route flaps for BFD. A value of zero means no flapping.
        """
        return self._get_attribute('flapTxIntervals')
    @FlapTxIntervals.setter
    def FlapTxIntervals(self, value):
        self._set_attribute('flapTxIntervals', value)

    @property
    def IncludePadTlv(self):
        """
        Returns
        -------
        - bool: If true, includes Pad TLV in triggered ping.
        """
        return self._get_attribute('includePadTlv')
    @IncludePadTlv.setter
    def IncludePadTlv(self, value):
        self._set_attribute('includePadTlv', value)

    @property
    def IncludeVendorEnterpriseNumberTlv(self):
        """
        Returns
        -------
        - bool: If true, includes the TLV number of the vendor, in triggered ping.
        """
        return self._get_attribute('includeVendorEnterpriseNumberTlv')
    @IncludeVendorEnterpriseNumberTlv.setter
    def IncludeVendorEnterpriseNumberTlv(self, value):
        self._set_attribute('includeVendorEnterpriseNumberTlv', value)

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): This signifies the interfaces that are associated with the selected interface type.Object references are:
        """
        return self._get_attribute('interfaces')
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute('interfaces', value)

    @property
    def MinRxInterval(self):
        """
        Returns
        -------
        - number: This signifies the minimum interval, in milliseconds, between received BFD Control packets that this interface is capable of supporting.
        """
        return self._get_attribute('minRxInterval')
    @MinRxInterval.setter
    def MinRxInterval(self, value):
        self._set_attribute('minRxInterval', value)

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: This signifies the negotiated transmit interval, multiplied by this value, provides the detection time for the interface.
        """
        return self._get_attribute('multiplier')
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute('multiplier', value)

    @property
    def PadTlvFirstOctet(self):
        """
        Returns
        -------
        - str(dropPadTlvFromReply | copyPadTlvToReply): This signifies the selection of the first octate of the Pad TLV. Possible values include:
        """
        return self._get_attribute('padTlvFirstOctet')
    @PadTlvFirstOctet.setter
    def PadTlvFirstOctet(self, value):
        self._set_attribute('padTlvFirstOctet', value)

    @property
    def PadTlvLength(self):
        """
        Returns
        -------
        - number: This signifies the specification of the length of the Pad TLV.
        """
        return self._get_attribute('padTlvLength')
    @PadTlvLength.setter
    def PadTlvLength(self, value):
        self._set_attribute('padTlvLength', value)

    @property
    def ReplyMode(self):
        """
        Returns
        -------
        - str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel): This signifies the selecion of the mode of reply.Possible values include DoNotReply, ReplyViaApplicationLevelControlChannel, ReplyViaIpv4Ipv6UdpPacket and ReplyViaIpv4Ipv6UdpPacketWithRouterAlert.
        """
        return self._get_attribute('replyMode')
    @ReplyMode.setter
    def ReplyMode(self, value):
        self._set_attribute('replyMode', value)

    @property
    def TxInterval(self):
        """
        Returns
        -------
        - number: This signifies the minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Control packets.
        """
        return self._get_attribute('txInterval')
    @TxInterval.setter
    def TxInterval(self, value):
        self._set_attribute('txInterval', value)

    @property
    def VendorEnterpriseNumber(self):
        """
        Returns
        -------
        - number: This signifies the specification of the enterprise number of the vendor.
        """
        return self._get_attribute('vendorEnterpriseNumber')
    @VendorEnterpriseNumber.setter
    def VendorEnterpriseNumber(self, value):
        self._set_attribute('vendorEnterpriseNumber', value)

    def update(self, BfdCvType=None, BfdDiscriminatorEnd=None, BfdDiscriminatorStart=None, ControlChannel=None, DestinationAddressIpv4=None, DownStreamAddressType=None, DownStreamInterfaceAddress=None, DownStreamIpAddress=None, EchoRequestInterval=None, EchoResponseTimeout=None, EnableDownStreamMappingTlv=None, EnableDsIflag=None, EnableDsNflag=None, EnableFecValidation=None, EnablePeriodicPing=None, Enabled=None, FlapTxIntervals=None, IncludePadTlv=None, IncludeVendorEnterpriseNumberTlv=None, Interfaces=None, MinRxInterval=None, Multiplier=None, PadTlvFirstOctet=None, PadTlvLength=None, ReplyMode=None, TxInterval=None, VendorEnterpriseNumber=None):
        """Updates interface resource on the server.

        Args
        ----
        - BfdCvType (str(bfdCvTypeIpUdp | bfdCvTypePwAch)): This signifies the BFD Connectivity Verification type. Possible values include:
        - BfdDiscriminatorEnd (number): This signifies the last BFD Discriminator value. This value should be greater than the BFD.
        - BfdDiscriminatorStart (number): This signifies the first BFD Discriminator value. The default value is 5000.
        - ControlChannel (str(controlChannelRouterAlert | controlChannelPwAch)): This signifies the communication control channel. Possible values include
        - DestinationAddressIpv4 (str): This signifies the destination IPv4 address.
        - DownStreamAddressType (str(ipv4Numbered | ipv4UnNumbered | ipv6Numbered | ipv6UnNumbered)): This signifies the address type of the downstream traffic. Possible values include:
        - DownStreamInterfaceAddress (number): This signifies the interface address of the downstream traffic.
        - DownStreamIpAddress (str): This signifies the IPv4/IPv6 address of the downstream traffic.
        - EchoRequestInterval (number): This signifies the minimum interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        - EchoResponseTimeout (number): This signifies the minimum tiomeout interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        - EnableDownStreamMappingTlv (bool): This signifies the enablement of downstream mapping TLV.
        - EnableDsIflag (bool): This signifies the activation of the DS I Flag.
        - EnableDsNflag (bool): This signifies the activation of the DS N Flag.
        - EnableFecValidation (bool): This signifies the selection of the check box to enable FEC validation.
        - EnablePeriodicPing (bool): If true, the router is pinged at regular intervals.
        - Enabled (bool): If true, it enables or disables the simulated router.
        - FlapTxIntervals (number): This signifies the number of seconds between route flaps for BFD. A value of zero means no flapping.
        - IncludePadTlv (bool): If true, includes Pad TLV in triggered ping.
        - IncludeVendorEnterpriseNumberTlv (bool): If true, includes the TLV number of the vendor, in triggered ping.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): This signifies the interfaces that are associated with the selected interface type.Object references are:
        - MinRxInterval (number): This signifies the minimum interval, in milliseconds, between received BFD Control packets that this interface is capable of supporting.
        - Multiplier (number): This signifies the negotiated transmit interval, multiplied by this value, provides the detection time for the interface.
        - PadTlvFirstOctet (str(dropPadTlvFromReply | copyPadTlvToReply)): This signifies the selection of the first octate of the Pad TLV. Possible values include:
        - PadTlvLength (number): This signifies the specification of the length of the Pad TLV.
        - ReplyMode (str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel)): This signifies the selecion of the mode of reply.Possible values include DoNotReply, ReplyViaApplicationLevelControlChannel, ReplyViaIpv4Ipv6UdpPacket and ReplyViaIpv4Ipv6UdpPacketWithRouterAlert.
        - TxInterval (number): This signifies the minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Control packets.
        - VendorEnterpriseNumber (number): This signifies the specification of the enterprise number of the vendor.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, BfdCvType=None, BfdDiscriminatorEnd=None, BfdDiscriminatorStart=None, ControlChannel=None, DestinationAddressIpv4=None, DownStreamAddressType=None, DownStreamInterfaceAddress=None, DownStreamIpAddress=None, EchoRequestInterval=None, EchoResponseTimeout=None, EnableDownStreamMappingTlv=None, EnableDsIflag=None, EnableDsNflag=None, EnableFecValidation=None, EnablePeriodicPing=None, Enabled=None, FlapTxIntervals=None, IncludePadTlv=None, IncludeVendorEnterpriseNumberTlv=None, Interfaces=None, MinRxInterval=None, Multiplier=None, PadTlvFirstOctet=None, PadTlvLength=None, ReplyMode=None, TxInterval=None, VendorEnterpriseNumber=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - BfdCvType (str(bfdCvTypeIpUdp | bfdCvTypePwAch)): This signifies the BFD Connectivity Verification type. Possible values include:
        - BfdDiscriminatorEnd (number): This signifies the last BFD Discriminator value. This value should be greater than the BFD.
        - BfdDiscriminatorStart (number): This signifies the first BFD Discriminator value. The default value is 5000.
        - ControlChannel (str(controlChannelRouterAlert | controlChannelPwAch)): This signifies the communication control channel. Possible values include
        - DestinationAddressIpv4 (str): This signifies the destination IPv4 address.
        - DownStreamAddressType (str(ipv4Numbered | ipv4UnNumbered | ipv6Numbered | ipv6UnNumbered)): This signifies the address type of the downstream traffic. Possible values include:
        - DownStreamInterfaceAddress (number): This signifies the interface address of the downstream traffic.
        - DownStreamIpAddress (str): This signifies the IPv4/IPv6 address of the downstream traffic.
        - EchoRequestInterval (number): This signifies the minimum interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        - EchoResponseTimeout (number): This signifies the minimum tiomeout interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        - EnableDownStreamMappingTlv (bool): This signifies the enablement of downstream mapping TLV.
        - EnableDsIflag (bool): This signifies the activation of the DS I Flag.
        - EnableDsNflag (bool): This signifies the activation of the DS N Flag.
        - EnableFecValidation (bool): This signifies the selection of the check box to enable FEC validation.
        - EnablePeriodicPing (bool): If true, the router is pinged at regular intervals.
        - Enabled (bool): If true, it enables or disables the simulated router.
        - FlapTxIntervals (number): This signifies the number of seconds between route flaps for BFD. A value of zero means no flapping.
        - IncludePadTlv (bool): If true, includes Pad TLV in triggered ping.
        - IncludeVendorEnterpriseNumberTlv (bool): If true, includes the TLV number of the vendor, in triggered ping.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): This signifies the interfaces that are associated with the selected interface type.Object references are:
        - MinRxInterval (number): This signifies the minimum interval, in milliseconds, between received BFD Control packets that this interface is capable of supporting.
        - Multiplier (number): This signifies the negotiated transmit interval, multiplied by this value, provides the detection time for the interface.
        - PadTlvFirstOctet (str(dropPadTlvFromReply | copyPadTlvToReply)): This signifies the selection of the first octate of the Pad TLV. Possible values include:
        - PadTlvLength (number): This signifies the specification of the length of the Pad TLV.
        - ReplyMode (str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel)): This signifies the selecion of the mode of reply.Possible values include DoNotReply, ReplyViaApplicationLevelControlChannel, ReplyViaIpv4Ipv6UdpPacket and ReplyViaIpv4Ipv6UdpPacketWithRouterAlert.
        - TxInterval (number): This signifies the minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Control packets.
        - VendorEnterpriseNumber (number): This signifies the specification of the enterprise number of the vendor.

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BfdCvType=None, BfdDiscriminatorEnd=None, BfdDiscriminatorStart=None, ControlChannel=None, DestinationAddressIpv4=None, DownStreamAddressType=None, DownStreamInterfaceAddress=None, DownStreamIpAddress=None, EchoRequestInterval=None, EchoResponseTimeout=None, EnableDownStreamMappingTlv=None, EnableDsIflag=None, EnableDsNflag=None, EnableFecValidation=None, EnablePeriodicPing=None, Enabled=None, FlapTxIntervals=None, IncludePadTlv=None, IncludeVendorEnterpriseNumberTlv=None, Interfaces=None, MinRxInterval=None, Multiplier=None, PadTlvFirstOctet=None, PadTlvLength=None, ReplyMode=None, TxInterval=None, VendorEnterpriseNumber=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - BfdCvType (str(bfdCvTypeIpUdp | bfdCvTypePwAch)): This signifies the BFD Connectivity Verification type. Possible values include:
        - BfdDiscriminatorEnd (number): This signifies the last BFD Discriminator value. This value should be greater than the BFD.
        - BfdDiscriminatorStart (number): This signifies the first BFD Discriminator value. The default value is 5000.
        - ControlChannel (str(controlChannelRouterAlert | controlChannelPwAch)): This signifies the communication control channel. Possible values include
        - DestinationAddressIpv4 (str): This signifies the destination IPv4 address.
        - DownStreamAddressType (str(ipv4Numbered | ipv4UnNumbered | ipv6Numbered | ipv6UnNumbered)): This signifies the address type of the downstream traffic. Possible values include:
        - DownStreamInterfaceAddress (number): This signifies the interface address of the downstream traffic.
        - DownStreamIpAddress (str): This signifies the IPv4/IPv6 address of the downstream traffic.
        - EchoRequestInterval (number): This signifies the minimum interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        - EchoResponseTimeout (number): This signifies the minimum tiomeout interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
        - EnableDownStreamMappingTlv (bool): This signifies the enablement of downstream mapping TLV.
        - EnableDsIflag (bool): This signifies the activation of the DS I Flag.
        - EnableDsNflag (bool): This signifies the activation of the DS N Flag.
        - EnableFecValidation (bool): This signifies the selection of the check box to enable FEC validation.
        - EnablePeriodicPing (bool): If true, the router is pinged at regular intervals.
        - Enabled (bool): If true, it enables or disables the simulated router.
        - FlapTxIntervals (number): This signifies the number of seconds between route flaps for BFD. A value of zero means no flapping.
        - IncludePadTlv (bool): If true, includes Pad TLV in triggered ping.
        - IncludeVendorEnterpriseNumberTlv (bool): If true, includes the TLV number of the vendor, in triggered ping.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): This signifies the interfaces that are associated with the selected interface type.Object references are:
        - MinRxInterval (number): This signifies the minimum interval, in milliseconds, between received BFD Control packets that this interface is capable of supporting.
        - Multiplier (number): This signifies the negotiated transmit interval, multiplied by this value, provides the detection time for the interface.
        - PadTlvFirstOctet (str(dropPadTlvFromReply | copyPadTlvToReply)): This signifies the selection of the first octate of the Pad TLV. Possible values include:
        - PadTlvLength (number): This signifies the specification of the length of the Pad TLV.
        - ReplyMode (str(doNotReply | replyViaIpv4Ipv6UdpPacket | replyViaIpv4Ipv6UdpPacketWithRouterAlert | replyViaApplicationLevelControlChannel)): This signifies the selecion of the mode of reply.Possible values include DoNotReply, ReplyViaApplicationLevelControlChannel, ReplyViaIpv4Ipv6UdpPacket and ReplyViaIpv4Ipv6UdpPacketWithRouterAlert.
        - TxInterval (number): This signifies the minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Control packets.
        - VendorEnterpriseNumber (number): This signifies the specification of the enterprise number of the vendor.

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
