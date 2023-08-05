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


class Ppp(Base):
    """The Layer 1 Configuration is being configured for a POS port and PPP is selected as the Payload Type.
    The Ppp class encapsulates a required ppp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ppp'

    def __init__(self, parent):
        super(Ppp, self).__init__(parent)

    @property
    def ConfigurationRetries(self):
        """
        Returns
        -------
        - number: The number of additional PPP configuration requests to send before beginning the termination process (if the peer is not properly acknowledging them). The default is 9 requests.
        """
        return self._get_attribute('configurationRetries')
    @ConfigurationRetries.setter
    def ConfigurationRetries(self, value):
        self._set_attribute('configurationRetries', value)

    @property
    def EnableAccmNegotiation(self):
        """
        Returns
        -------
        - bool: Enables negotiation of Asynchronous Control Character Mask (ACCM).
        """
        return self._get_attribute('enableAccmNegotiation')
    @EnableAccmNegotiation.setter
    def EnableAccmNegotiation(self, value):
        self._set_attribute('enableAccmNegotiation', value)

    @property
    def EnableIpV4(self):
        """
        Returns
        -------
        - bool: Enables the IPv4 Network Control Protocol (IPCP).
        """
        return self._get_attribute('enableIpV4')
    @EnableIpV4.setter
    def EnableIpV4(self, value):
        self._set_attribute('enableIpV4', value)

    @property
    def EnableIpV6(self):
        """
        Returns
        -------
        - bool: Enables the IPv6 Network Control Protocol (IPCP).
        """
        return self._get_attribute('enableIpV6')
    @EnableIpV6.setter
    def EnableIpV6(self, value):
        self._set_attribute('enableIpV6', value)

    @property
    def EnableLqm(self):
        """
        Returns
        -------
        - bool: Enables Link Quality Monitoring (LQM) on the link.
        """
        return self._get_attribute('enableLqm')
    @EnableLqm.setter
    def EnableLqm(self, value):
        self._set_attribute('enableLqm', value)

    @property
    def EnableMpls(self):
        """
        Returns
        -------
        - bool: Enables MPLS on the link.
        """
        return self._get_attribute('enableMpls')
    @EnableMpls.setter
    def EnableMpls(self, value):
        self._set_attribute('enableMpls', value)

    @property
    def EnableOsi(self):
        """
        Returns
        -------
        - bool: Enables the Open System Interconnection (OSI) Network Layer Control Protocol (OSINLCP).
        """
        return self._get_attribute('enableOsi')
    @EnableOsi.setter
    def EnableOsi(self, value):
        self._set_attribute('enableOsi', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables PPP for the POS port.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def LocalIpAddress(self):
        """
        Returns
        -------
        - str: The local port's requested IPv4 address. This address is sent by the local peer to the remote peer, as a Configuration Option in an IPCP Configuration Request packet. The default is 0.0.0.1.
        """
        return self._get_attribute('localIpAddress')
    @LocalIpAddress.setter
    def LocalIpAddress(self, value):
        self._set_attribute('localIpAddress', value)

    @property
    def LocalIpV6IdType(self):
        """
        Returns
        -------
        - str(ipV6 | lastNegotiated | macBased | random): The type of Interface Identifier (IID). It is a Configuration Options sent in the Configuration Request packet. A globally unique, non-zero Interface Identifier is preferred.
        """
        return self._get_attribute('localIpV6IdType')
    @LocalIpV6IdType.setter
    def LocalIpV6IdType(self, value):
        self._set_attribute('localIpV6IdType', value)

    @property
    def LocalIpV6Iid(self):
        """
        Returns
        -------
        - str: (a 64-bit/8-octet value) The IPv6 Interface Identifier. It MUST be unique on the link.
        """
        return self._get_attribute('localIpV6Iid')
    @LocalIpV6Iid.setter
    def LocalIpV6Iid(self, value):
        self._set_attribute('localIpV6Iid', value)

    @property
    def LocalIpV6MacBasedIid(self):
        """
        Returns
        -------
        - str: (a 48-bit/6-octet value) The MAC Interface Identifier. It MUST be unique on the link.
        """
        return self._get_attribute('localIpV6MacBasedIid')
    @LocalIpV6MacBasedIid.setter
    def LocalIpV6MacBasedIid(self, value):
        self._set_attribute('localIpV6MacBasedIid', value)

    @property
    def LocalIpV6NegotiationMode(self):
        """
        Returns
        -------
        - str(localMay | localMust | peerMust): Before the negotiation of the Interface Identifier (IID), the node chooses a tentative Interface Identifier.
        """
        return self._get_attribute('localIpV6NegotiationMode')
    @LocalIpV6NegotiationMode.setter
    def LocalIpV6NegotiationMode(self, value):
        self._set_attribute('localIpV6NegotiationMode', value)

    @property
    def LqmReportInterval(self):
        """
        Returns
        -------
        - number: The number of seconds between Link Quality Monitoring (LQM) reports.
        """
        return self._get_attribute('lqmReportInterval')
    @LqmReportInterval.setter
    def LqmReportInterval(self, value):
        self._set_attribute('lqmReportInterval', value)

    @property
    def PeerIpV6IdType(self):
        """
        Returns
        -------
        - str(ipV6 | lastNegotiated | macBased | random): The type of Interface Identifier (IID). It is a Configuration Options sent in the Configuration Request packet. A globally unique, non-zero Interface Identifier is preferred.
        """
        return self._get_attribute('peerIpV6IdType')
    @PeerIpV6IdType.setter
    def PeerIpV6IdType(self, value):
        self._set_attribute('peerIpV6IdType', value)

    @property
    def PeerIpV6Iid(self):
        """
        Returns
        -------
        - str: (a 64-bit/8-octet value) The IPv6 Interface Identifier. It MUST be unique on the link.
        """
        return self._get_attribute('peerIpV6Iid')
    @PeerIpV6Iid.setter
    def PeerIpV6Iid(self, value):
        self._set_attribute('peerIpV6Iid', value)

    @property
    def PeerIpV6MacBasedIid(self):
        """
        Returns
        -------
        - str: (a 48-bit/6-octet value) The MAC Interface Identifier. It MUST be unique on the link.
        """
        return self._get_attribute('peerIpV6MacBasedIid')
    @PeerIpV6MacBasedIid.setter
    def PeerIpV6MacBasedIid(self, value):
        self._set_attribute('peerIpV6MacBasedIid', value)

    @property
    def PeerIpV6NegotiationMode(self):
        """
        Returns
        -------
        - str(localMust | peerMay | peerMust): Before the negotiation of the Interface Identifier (IID), the node chooses a tentative Interface Identifier.
        """
        return self._get_attribute('peerIpV6NegotiationMode')
    @PeerIpV6NegotiationMode.setter
    def PeerIpV6NegotiationMode(self, value):
        self._set_attribute('peerIpV6NegotiationMode', value)

    @property
    def PppLinkState(self):
        """
        Returns
        -------
        - str: (Read-only) Indicates the current port link state. If PPP is enabled, the fully operational link state is indicated as PPP Up.
        """
        return self._get_attribute('pppLinkState')

    @property
    def RetryTimeout(self):
        """
        Returns
        -------
        - number: The time, in seconds, between retransmissions of successive configuration or termination requests. The default is 8 seconds.
        """
        return self._get_attribute('retryTimeout')
    @RetryTimeout.setter
    def RetryTimeout(self, value):
        self._set_attribute('retryTimeout', value)

    @property
    def RxAlignment(self):
        """
        Returns
        -------
        - number: The byte alignment desired for Receive, in bytes. The default is 0 bytes.
        """
        return self._get_attribute('rxAlignment')
    @RxAlignment.setter
    def RxAlignment(self, value):
        self._set_attribute('rxAlignment', value)

    @property
    def RxMaxReceiveUnit(self):
        """
        Returns
        -------
        - number: The maximum transmit frame size desired, in bytes. The default is 65,535 bytes.
        """
        return self._get_attribute('rxMaxReceiveUnit')
    @RxMaxReceiveUnit.setter
    def RxMaxReceiveUnit(self, value):
        self._set_attribute('rxMaxReceiveUnit', value)

    @property
    def TxAlignment(self):
        """
        Returns
        -------
        - number: The byte alignment desired for Transmit, in bytes. The default is 0 bytes.
        """
        return self._get_attribute('txAlignment')
    @TxAlignment.setter
    def TxAlignment(self, value):
        self._set_attribute('txAlignment', value)

    @property
    def TxMaxReceiveUnit(self):
        """
        Returns
        -------
        - number: The maximum transmit frame size desired, in bytes. The default is 65,535 bytes.
        """
        return self._get_attribute('txMaxReceiveUnit')
    @TxMaxReceiveUnit.setter
    def TxMaxReceiveUnit(self, value):
        self._set_attribute('txMaxReceiveUnit', value)

    @property
    def UseMagicNumber(self):
        """
        Returns
        -------
        - bool: If enabled, magic number handling is enabled for negotiation and usage. The magic number is used primarily to detect looped connections.
        """
        return self._get_attribute('useMagicNumber')
    @UseMagicNumber.setter
    def UseMagicNumber(self, value):
        self._set_attribute('useMagicNumber', value)

    def update(self, ConfigurationRetries=None, EnableAccmNegotiation=None, EnableIpV4=None, EnableIpV6=None, EnableLqm=None, EnableMpls=None, EnableOsi=None, Enabled=None, LocalIpAddress=None, LocalIpV6IdType=None, LocalIpV6Iid=None, LocalIpV6MacBasedIid=None, LocalIpV6NegotiationMode=None, LqmReportInterval=None, PeerIpV6IdType=None, PeerIpV6Iid=None, PeerIpV6MacBasedIid=None, PeerIpV6NegotiationMode=None, RetryTimeout=None, RxAlignment=None, RxMaxReceiveUnit=None, TxAlignment=None, TxMaxReceiveUnit=None, UseMagicNumber=None):
        """Updates ppp resource on the server.

        Args
        ----
        - ConfigurationRetries (number): The number of additional PPP configuration requests to send before beginning the termination process (if the peer is not properly acknowledging them). The default is 9 requests.
        - EnableAccmNegotiation (bool): Enables negotiation of Asynchronous Control Character Mask (ACCM).
        - EnableIpV4 (bool): Enables the IPv4 Network Control Protocol (IPCP).
        - EnableIpV6 (bool): Enables the IPv6 Network Control Protocol (IPCP).
        - EnableLqm (bool): Enables Link Quality Monitoring (LQM) on the link.
        - EnableMpls (bool): Enables MPLS on the link.
        - EnableOsi (bool): Enables the Open System Interconnection (OSI) Network Layer Control Protocol (OSINLCP).
        - Enabled (bool): If true, enables PPP for the POS port.
        - LocalIpAddress (str): The local port's requested IPv4 address. This address is sent by the local peer to the remote peer, as a Configuration Option in an IPCP Configuration Request packet. The default is 0.0.0.1.
        - LocalIpV6IdType (str(ipV6 | lastNegotiated | macBased | random)): The type of Interface Identifier (IID). It is a Configuration Options sent in the Configuration Request packet. A globally unique, non-zero Interface Identifier is preferred.
        - LocalIpV6Iid (str): (a 64-bit/8-octet value) The IPv6 Interface Identifier. It MUST be unique on the link.
        - LocalIpV6MacBasedIid (str): (a 48-bit/6-octet value) The MAC Interface Identifier. It MUST be unique on the link.
        - LocalIpV6NegotiationMode (str(localMay | localMust | peerMust)): Before the negotiation of the Interface Identifier (IID), the node chooses a tentative Interface Identifier.
        - LqmReportInterval (number): The number of seconds between Link Quality Monitoring (LQM) reports.
        - PeerIpV6IdType (str(ipV6 | lastNegotiated | macBased | random)): The type of Interface Identifier (IID). It is a Configuration Options sent in the Configuration Request packet. A globally unique, non-zero Interface Identifier is preferred.
        - PeerIpV6Iid (str): (a 64-bit/8-octet value) The IPv6 Interface Identifier. It MUST be unique on the link.
        - PeerIpV6MacBasedIid (str): (a 48-bit/6-octet value) The MAC Interface Identifier. It MUST be unique on the link.
        - PeerIpV6NegotiationMode (str(localMust | peerMay | peerMust)): Before the negotiation of the Interface Identifier (IID), the node chooses a tentative Interface Identifier.
        - RetryTimeout (number): The time, in seconds, between retransmissions of successive configuration or termination requests. The default is 8 seconds.
        - RxAlignment (number): The byte alignment desired for Receive, in bytes. The default is 0 bytes.
        - RxMaxReceiveUnit (number): The maximum transmit frame size desired, in bytes. The default is 65,535 bytes.
        - TxAlignment (number): The byte alignment desired for Transmit, in bytes. The default is 0 bytes.
        - TxMaxReceiveUnit (number): The maximum transmit frame size desired, in bytes. The default is 65,535 bytes.
        - UseMagicNumber (bool): If enabled, magic number handling is enabled for negotiation and usage. The magic number is used primarily to detect looped connections.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
