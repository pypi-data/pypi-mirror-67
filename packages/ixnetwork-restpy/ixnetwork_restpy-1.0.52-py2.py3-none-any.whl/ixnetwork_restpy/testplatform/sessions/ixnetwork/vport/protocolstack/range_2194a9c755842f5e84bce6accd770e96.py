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


class Range(Base):
    """
    The Range class encapsulates a list of range resources that are managed by the user.
    A list of resources can be retrieved from the server using the Range.find() method.
    The list can be managed by using the Range.add() and Range.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'range'

    def __init__(self, parent):
        super(Range, self).__init__(parent)

    @property
    def AmtRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtrange_329d9d76ec488d10b90229d82f782fa5.AmtRange): An instance of the AmtRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtrange_329d9d76ec488d10b90229d82f782fa5 import AmtRange
        return AmtRange(self)

    @property
    def AncpRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancprange_d773e793a0ca6c0075a3e2ae42703771.AncpRange): An instance of the AncpRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancprange_d773e793a0ca6c0075a3e2ae42703771 import AncpRange
        return AncpRange(self)

    @property
    def DhcpHostsRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsrange_7575d518897bb87c8285820fefd10aa6.DhcpHostsRange): An instance of the DhcpHostsRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsrange_7575d518897bb87c8285820fefd10aa6 import DhcpHostsRange
        return DhcpHostsRange(self)._select()

    @property
    def Dhcpv6ClientRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientrange_4d77be1212f690eef2a2bc745b02ba7f.Dhcpv6ClientRange): An instance of the Dhcpv6ClientRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientrange_4d77be1212f690eef2a2bc745b02ba7f import Dhcpv6ClientRange
        return Dhcpv6ClientRange(self)

    @property
    def Dhcpv6PdClientRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientrange_d3712d16253f17b4dcc51d572efa2149.Dhcpv6PdClientRange): An instance of the Dhcpv6PdClientRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientrange_d3712d16253f17b4dcc51d572efa2149 import Dhcpv6PdClientRange
        return Dhcpv6PdClientRange(self)

    @property
    def Dhcpv6ServerRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serverrange_497b0b8820d8a5021e03f0b83abbeee6.Dhcpv6ServerRange): An instance of the Dhcpv6ServerRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serverrange_497b0b8820d8a5021e03f0b83abbeee6 import Dhcpv6ServerRange
        return Dhcpv6ServerRange(self)

    @property
    def Dot1xRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xrange_75e778ee056523cfc4c0741b26b0f79f.Dot1xRange): An instance of the Dot1xRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xrange_75e778ee056523cfc4c0741b26b0f79f import Dot1xRange
        return Dot1xRange(self)

    @property
    def EapoUdpRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudprange_e3987b59cef46c06104696d23e253ed1.EapoUdpRange): An instance of the EapoUdpRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudprange_e3987b59cef46c06104696d23e253ed1 import EapoUdpRange
        return EapoUdpRange(self)

    @property
    def EsmcRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.esmcrange_610feff14d4057681422446cef6d5172.EsmcRange): An instance of the EsmcRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.esmcrange_610feff14d4057681422446cef6d5172 import EsmcRange
        return EsmcRange(self)

    @property
    def IgmpMldRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpmldrange_4a4ee86fc995e36eb2053e32804f7389.IgmpMldRange): An instance of the IgmpMldRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpmldrange_4a4ee86fc995e36eb2053e32804f7389 import IgmpMldRange
        return IgmpMldRange(self)

    @property
    def IgmpQuerierRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpquerierrange_890a21a638ba03ec27bc22a43f0051fb.IgmpQuerierRange): An instance of the IgmpQuerierRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpquerierrange_890a21a638ba03ec27bc22a43f0051fb import IgmpQuerierRange
        return IgmpQuerierRange(self)

    @property
    def IpRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprange_197754fdf296ad433a3d4e4a00a83d40.IpRange): An instance of the IpRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprange_197754fdf296ad433a3d4e4a00a83d40 import IpRange
        return IpRange(self)._select()

    @property
    def IptvRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iptvrange_90085eb053923be08eea3e1bd10978b5.IptvRange): An instance of the IptvRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iptvrange_90085eb053923be08eea3e1bd10978b5 import IptvRange
        return IptvRange(self)

    @property
    def L2tpRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tprange_e9a5ab0d3ec325c532ca0af4f54eb85d.L2tpRange): An instance of the L2tpRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tprange_e9a5ab0d3ec325c532ca0af4f54eb85d import L2tpRange
        return L2tpRange(self)._select()

    @property
    def MacRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.macrange_af6a6e581a9e45f997967be8fc4416f5.MacRange): An instance of the MacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.macrange_af6a6e581a9e45f997967be8fc4416f5 import MacRange
        return MacRange(self)._select()

    @property
    def PtpRangeOverIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeoverip_72afb4ff152e89fc5e34dfde6949c5c6.PtpRangeOverIp): An instance of the PtpRangeOverIp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeoverip_72afb4ff152e89fc5e34dfde6949c5c6 import PtpRangeOverIp
        return PtpRangeOverIp(self)

    @property
    def PtpRangeOverMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeovermac_473de0ae21ac06dded02326a54d85e0b.PtpRangeOverMac): An instance of the PtpRangeOverMac class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptprangeovermac_473de0ae21ac06dded02326a54d85e0b import PtpRangeOverMac
        return PtpRangeOverMac(self)

    @property
    def RadiusRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.radiusrange_02f9244feab7e7129f8671d76a8d8f67.RadiusRange): An instance of the RadiusRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.radiusrange_02f9244feab7e7129f8671d76a8d8f67 import RadiusRange
        return RadiusRange(self)

    @property
    def TwampControlRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampcontrolrange_2633e46a195c50097d4c6fa356bb396d.TwampControlRange): An instance of the TwampControlRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampcontrolrange_2633e46a195c50097d4c6fa356bb396d import TwampControlRange
        return TwampControlRange(self)

    @property
    def TwampServerRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserverrange_b9cef64e3ef5164faed4bd1e7e845fcb.TwampServerRange): An instance of the TwampServerRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserverrange_b9cef64e3ef5164faed4bd1e7e845fcb import TwampServerRange
        return TwampServerRange(self)

    @property
    def TwampTestRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twamptestrange_eff675272ead66373cb9ccc5f41780d3.TwampTestRange): An instance of the TwampTestRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twamptestrange_eff675272ead66373cb9ccc5f41780d3 import TwampTestRange
        return TwampTestRange(self)

    @property
    def VicClientRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vicclientrange_f334b83f99c5486f74e3dba217d58f46.VicClientRange): An instance of the VicClientRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vicclientrange_f334b83f99c5486f74e3dba217d58f46 import VicClientRange
        return VicClientRange(self)

    @property
    def VlanRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanrange_afd81185ed8c3bb5459ca36e2f1f1e6a.VlanRange): An instance of the VlanRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vlanrange_afd81185ed8c3bb5459ca36e2f1f1e6a import VlanRange
        return VlanRange(self)._select()

    @property
    def WebAuthRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthrange_021d954442f75fa7615f5921a8318ffe.WebAuthRange): An instance of the WebAuthRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthrange_021d954442f75fa7615f5921a8318ffe import WebAuthRange
        return WebAuthRange(self)

    def add(self):
        """Adds a new range resource on the server and adds it to the container.

        Returns
        -------
        - self: This instance with all currently retrieved range resources using find and the newly added range resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained range resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self):
        """Finds and retrieves range resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve range resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all range resources from the server.

        Returns
        -------
        - self: This instance with matching range resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of range data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the range resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DhcpHostsPause(self):
        """Executes the dhcpHostsPause operation on the server.

        Pause negotiation of DHCPHosts for selected plugins and ranges

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('dhcpHostsPause', payload=payload, response_object=None)

    def DhcpHostsResume(self):
        """Executes the dhcpHostsResume operation on the server.

        Resume previously paused negotiation of DHCPHosts for selected plugins and ranges

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('dhcpHostsResume', payload=payload, response_object=None)

    def DhcpHostsStart(self, *args, **kwargs):
        """Executes the dhcpHostsStart operation on the server.

        Negotiate DHCPHosts for selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        dhcpHostsStart(Arg2=enum)
        -------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dhcpHostsStart', payload=payload, response_object=None)

    def DhcpHostsStop(self, *args, **kwargs):
        """Executes the dhcpHostsStop operation on the server.

        Release DHCPHosts for selected plugins and ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        dhcpHostsStop(Arg2=enum)
        ------------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('dhcpHostsStop', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)

    def Ipv6SendNdpNS(self, *args, **kwargs):
        """Executes the ipv6SendNdpNS operation on the server.

        Send NS on NDP for IPv6 ports.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ipv6SendNdpNS(Arg2=number)
        --------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]

        ipv6SendNdpNS(Arg2=number, Arg3=enum)
        -------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]
        - Arg3 (str(async | sync)): IPv6 NDP rate for NS messages.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ipv6SendNdpNS', payload=payload, response_object=None)

    def Ipv6SendNdpRS(self, *args, **kwargs):
        """Executes the ipv6SendNdpRS operation on the server.

        Send RS on NDP for IPv6 ports.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        ipv6SendNdpRS(Arg2=number)
        --------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]

        ipv6SendNdpRS(Arg2=number, Arg3=enum)
        -------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range,/vport/protocolStack/atm/emulatedRouterEndpoint/range,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpUeEndpoint/range,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/smDnsEndpoint/range,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/range]
        - Arg3 (str(async | sync)): IPv6 NDP rate for RS messages.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('ipv6SendNdpRS', payload=payload, response_object=None)

    def L2tpCancel(self):
        """Executes the l2tpCancel operation on the server.

        Cancel ending L2TP operations

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('l2tpCancel', payload=payload, response_object=None)

    def L2tpConfigure(self):
        """Executes the l2tpConfigure operation on the server.

        Configure L2TP protocol on selected ranges.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('l2tpConfigure', payload=payload, response_object=None)

    def L2tpDeconfigure(self):
        """Executes the l2tpDeconfigure operation on the server.

        Deconfigure L2TP protocol on selected ranges.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('l2tpDeconfigure', payload=payload, response_object=None)

    def L2tpPause(self, *args, **kwargs):
        """Executes the l2tpPause operation on the server.

        Pause negotiation for L2TP tunnels and PPP sessions in specified range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        l2tpPause(Arg2=enum)
        --------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('l2tpPause', payload=payload, response_object=None)

    def L2tpResume(self, *args, **kwargs):
        """Executes the l2tpResume operation on the server.

        Resume previously paused negotiation for L2TP tunnels and PPP sessions in specified range

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        l2tpResume(Arg2=enum)
        ---------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('l2tpResume', payload=payload, response_object=None)

    def L2tpRetry(self, *args, **kwargs):
        """Executes the l2tpRetry operation on the server.

        Retry negotiating L2TP tunnels and PPP sessions if specified range timed out

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        l2tpRetry(Arg2=enum)
        --------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('l2tpRetry', payload=payload, response_object=None)

    def L2tpSendNdpRs(self, *args, **kwargs):
        """Executes the l2tpSendNdpRs operation on the server.

        Send RS on NDP for IPv6 ports

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        l2tpSendNdpRs(Arg2=number)
        --------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range]

        l2tpSendNdpRs(Arg2=number, Arg3=enum)
        -------------------------------------
        - Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range]
        - Arg3 (str(async | sync)): IPv6 NDP rate for NS messages.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('l2tpSendNdpRs', payload=payload, response_object=None)

    def L2tpStart(self, *args, **kwargs):
        """Executes the l2tpStart operation on the server.

        Negotiate L2TP tunnels and PPP sessions for selected ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        l2tpStart(Arg2=enum)
        --------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('l2tpStart', payload=payload, response_object=None)

    def L2tpStop(self, *args, **kwargs):
        """Executes the l2tpStop operation on the server.

        Teardown L2TP tunnels and PPP sessions for selected ranges

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        l2tpStop(Arg2=enum)
        -------------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('l2tpStop', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Negotiate sessions for all protocols on all ranges belonging to selected plugins

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(Arg2=enum)
        ----------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm,/vport/protocolStack/atm/dhcpEndpoint,/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/dhcpServerEndpoint,/vport/protocolStack/atm/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/twampClient,/vport/protocolStack/atm/emulatedRouter/ip/twampServer,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/atm/emulatedRouterEndpoint,/vport/protocolStack/atm/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeEndpoint,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/smDnsEndpoint,/vport/protocolStack/atm/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/twampClient,/vport/protocolStack/atm/ip/twampServer,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/amtRange,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/ipEndpoint/twampClient,/vport/protocolStack/atm/ipEndpoint/twampServer,/vport/protocolStack/atm/pppox,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppoxEndpoint,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet,/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpServerEndpoint,/vport/protocolStack/ethernet/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ip/twampServer,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/ethernet/emulatedRouterEndpoint,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFdiscRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFlogiRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range,/vport/protocolStack/ethernet/fcoeFwdEndpoint/secondaryRange,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/twampClient,/vport/protocolStack/ethernet/ip/twampServer,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ipEndpoint/twampClient,/vport/protocolStack/ethernet/ipEndpoint/twampServer,/vport/protocolStack/ethernet/pppox,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppoxEndpoint,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/vepaEndpoint,/vport/protocolStack/ethernet/vepaEndpoint/range,/vport/protocolStack/ethernetEndpoint,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/fcClientEndpoint,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range/fcClientFdiscRange,/vport/protocolStack/fcClientEndpoint/range/fcClientFlogiRange,/vport/protocolStack/fcFportFwdEndpoint,/vport/protocolStack/fcFportFwdEndpoint/range,/vport/protocolStack/fcFportFwdEndpoint/secondaryRange]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Teardown sessions for all protocols on all ranges belonging to selected plugins

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(Arg2=enum)
        ---------------
        - Arg2 (str(async | sync)): kArray[kObjref=/vport/protocolStack/atm,/vport/protocolStack/atm/dhcpEndpoint,/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/dhcpServerEndpoint,/vport/protocolStack/atm/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/twampClient,/vport/protocolStack/atm/emulatedRouter/ip/twampServer,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/atm/emulatedRouterEndpoint,/vport/protocolStack/atm/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeEndpoint,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/smDnsEndpoint,/vport/protocolStack/atm/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/twampClient,/vport/protocolStack/atm/ip/twampServer,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/amtRange,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/ipEndpoint/twampClient,/vport/protocolStack/atm/ipEndpoint/twampServer,/vport/protocolStack/atm/pppox,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppoxEndpoint,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet,/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpServerEndpoint,/vport/protocolStack/ethernet/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ip/twampServer,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/ethernet/emulatedRouterEndpoint,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFdiscRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFlogiRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range,/vport/protocolStack/ethernet/fcoeFwdEndpoint/secondaryRange,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/twampClient,/vport/protocolStack/ethernet/ip/twampServer,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ipEndpoint/twampClient,/vport/protocolStack/ethernet/ipEndpoint/twampServer,/vport/protocolStack/ethernet/pppox,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppoxEndpoint,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/vepaEndpoint,/vport/protocolStack/ethernet/vepaEndpoint/range,/vport/protocolStack/ethernetEndpoint,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/fcClientEndpoint,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range/fcClientFdiscRange,/vport/protocolStack/fcClientEndpoint/range/fcClientFlogiRange,/vport/protocolStack/fcFportFwdEndpoint,/vport/protocolStack/fcFportFwdEndpoint/range,/vport/protocolStack/fcFportFwdEndpoint/secondaryRange]

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
