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


class Capabilities(Base):
    """Filters routes based on route type.
    The Capabilities class encapsulates a required capabilities resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'capabilities'

    def __init__(self, parent):
        super(Capabilities, self).__init__(parent)

    @property
    def AdVpls(self):
        """
        Returns
        -------
        - bool: If true, enables the BGP autodiscovery VPLS tunnels.
        """
        return self._get_attribute('adVpls')
    @AdVpls.setter
    def AdVpls(self, value):
        self._set_attribute('adVpls', value)

    @property
    def Evpn(self):
        """
        Returns
        -------
        - bool: If enabled, then this BGP peer range supports BGP MPLS Based Ethernet VPN per draft-ietf-l2vpn-evpn-03. Default value is false.
        """
        return self._get_attribute('evpn')
    @Evpn.setter
    def Evpn(self, value):
        self._set_attribute('evpn', value)

    @property
    def FetchDetailedIpV4UnicastInfo(self):
        """
        Returns
        -------
        - bool: If enabled, this BGP router displays complete information about the Ipv4UnicastInfo.
        """
        return self._get_attribute('fetchDetailedIpV4UnicastInfo')
    @FetchDetailedIpV4UnicastInfo.setter
    def FetchDetailedIpV4UnicastInfo(self, value):
        self._set_attribute('fetchDetailedIpV4UnicastInfo', value)

    @property
    def FetchDetailedIpV6UnicastInfo(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('fetchDetailedIpV6UnicastInfo')
    @FetchDetailedIpV6UnicastInfo.setter
    def FetchDetailedIpV6UnicastInfo(self, value):
        self._set_attribute('fetchDetailedIpV6UnicastInfo', value)

    @property
    def IpV4Mpls(self):
        """
        Returns
        -------
        - bool: If true, learns IPv4 MPLS routes.
        """
        return self._get_attribute('ipV4Mpls')
    @IpV4Mpls.setter
    def IpV4Mpls(self, value):
        self._set_attribute('ipV4Mpls', value)

    @property
    def IpV4MplsVpn(self):
        """
        Returns
        -------
        - bool: If true, learns MPLS VPN routes.
        """
        return self._get_attribute('ipV4MplsVpn')
    @IpV4MplsVpn.setter
    def IpV4MplsVpn(self, value):
        self._set_attribute('ipV4MplsVpn', value)

    @property
    def IpV4Multicast(self):
        """
        Returns
        -------
        - bool: If true, learns IPv4 Multicast routes.
        """
        return self._get_attribute('ipV4Multicast')
    @IpV4Multicast.setter
    def IpV4Multicast(self, value):
        self._set_attribute('ipV4Multicast', value)

    @property
    def IpV4MulticastMplsVpn(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipV4MulticastMplsVpn')
    @IpV4MulticastMplsVpn.setter
    def IpV4MulticastMplsVpn(self, value):
        self._set_attribute('ipV4MulticastMplsVpn', value)

    @property
    def IpV4MulticastVpn(self):
        """
        Returns
        -------
        - bool: If enabled, this BGP router/peer supports the IPv4 Multicast/VPN address family.
        """
        return self._get_attribute('ipV4MulticastVpn')
    @IpV4MulticastVpn.setter
    def IpV4MulticastVpn(self, value):
        self._set_attribute('ipV4MulticastVpn', value)

    @property
    def IpV4Unicast(self):
        """
        Returns
        -------
        - bool: If true, learns IPv4 Unicast routes.
        """
        return self._get_attribute('ipV4Unicast')
    @IpV4Unicast.setter
    def IpV4Unicast(self, value):
        self._set_attribute('ipV4Unicast', value)

    @property
    def IpV6Mpls(self):
        """
        Returns
        -------
        - bool: If true, learns IPv6 MPLS routes.
        """
        return self._get_attribute('ipV6Mpls')
    @IpV6Mpls.setter
    def IpV6Mpls(self, value):
        self._set_attribute('ipV6Mpls', value)

    @property
    def IpV6MplsVpn(self):
        """
        Returns
        -------
        - bool: If true, learns IPv6 MPLS VPN routes.
        """
        return self._get_attribute('ipV6MplsVpn')
    @IpV6MplsVpn.setter
    def IpV6MplsVpn(self, value):
        self._set_attribute('ipV6MplsVpn', value)

    @property
    def IpV6Multicast(self):
        """
        Returns
        -------
        - bool: If true, learns IPv6 Multicast routes.
        """
        return self._get_attribute('ipV6Multicast')
    @IpV6Multicast.setter
    def IpV6Multicast(self, value):
        self._set_attribute('ipV6Multicast', value)

    @property
    def IpV6MulticastMplsVpn(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ipV6MulticastMplsVpn')
    @IpV6MulticastMplsVpn.setter
    def IpV6MulticastMplsVpn(self, value):
        self._set_attribute('ipV6MulticastMplsVpn', value)

    @property
    def IpV6MulticastVpn(self):
        """
        Returns
        -------
        - bool: If enabled, this BGP router/peer supports the IPv6 Multicast/VPN address family.
        """
        return self._get_attribute('ipV6MulticastVpn')
    @IpV6MulticastVpn.setter
    def IpV6MulticastVpn(self, value):
        self._set_attribute('ipV6MulticastVpn', value)

    @property
    def IpV6Unicast(self):
        """
        Returns
        -------
        - bool: If true, learns IPv6 Unicast routes.
        """
        return self._get_attribute('ipV6Unicast')
    @IpV6Unicast.setter
    def IpV6Unicast(self, value):
        self._set_attribute('ipV6Unicast', value)

    @property
    def Vpls(self):
        """
        Returns
        -------
        - bool: If true, learns VPLS routes.
        """
        return self._get_attribute('vpls')
    @Vpls.setter
    def Vpls(self, value):
        self._set_attribute('vpls', value)

    def update(self, AdVpls=None, Evpn=None, FetchDetailedIpV4UnicastInfo=None, FetchDetailedIpV6UnicastInfo=None, IpV4Mpls=None, IpV4MplsVpn=None, IpV4Multicast=None, IpV4MulticastMplsVpn=None, IpV4MulticastVpn=None, IpV4Unicast=None, IpV6Mpls=None, IpV6MplsVpn=None, IpV6Multicast=None, IpV6MulticastMplsVpn=None, IpV6MulticastVpn=None, IpV6Unicast=None, Vpls=None):
        """Updates capabilities resource on the server.

        Args
        ----
        - AdVpls (bool): If true, enables the BGP autodiscovery VPLS tunnels.
        - Evpn (bool): If enabled, then this BGP peer range supports BGP MPLS Based Ethernet VPN per draft-ietf-l2vpn-evpn-03. Default value is false.
        - FetchDetailedIpV4UnicastInfo (bool): If enabled, this BGP router displays complete information about the Ipv4UnicastInfo.
        - FetchDetailedIpV6UnicastInfo (bool): NOT DEFINED
        - IpV4Mpls (bool): If true, learns IPv4 MPLS routes.
        - IpV4MplsVpn (bool): If true, learns MPLS VPN routes.
        - IpV4Multicast (bool): If true, learns IPv4 Multicast routes.
        - IpV4MulticastMplsVpn (bool): NOT DEFINED
        - IpV4MulticastVpn (bool): If enabled, this BGP router/peer supports the IPv4 Multicast/VPN address family.
        - IpV4Unicast (bool): If true, learns IPv4 Unicast routes.
        - IpV6Mpls (bool): If true, learns IPv6 MPLS routes.
        - IpV6MplsVpn (bool): If true, learns IPv6 MPLS VPN routes.
        - IpV6Multicast (bool): If true, learns IPv6 Multicast routes.
        - IpV6MulticastMplsVpn (bool): NOT DEFINED
        - IpV6MulticastVpn (bool): If enabled, this BGP router/peer supports the IPv6 Multicast/VPN address family.
        - IpV6Unicast (bool): If true, learns IPv6 Unicast routes.
        - Vpls (bool): If true, learns VPLS routes.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
