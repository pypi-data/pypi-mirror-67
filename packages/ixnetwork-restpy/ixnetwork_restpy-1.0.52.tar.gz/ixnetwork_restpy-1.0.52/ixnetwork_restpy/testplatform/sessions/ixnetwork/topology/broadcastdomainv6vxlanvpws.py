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


class BroadcastDomainV6VxlanVpws(Base):
    """BGP V6 Broadcast Domain Configuration
    The BroadcastDomainV6VxlanVpws class encapsulates a required broadcastDomainV6VxlanVpws resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'broadcastDomainV6VxlanVpws'

    def __init__(self, parent):
        super(BroadcastDomainV6VxlanVpws, self).__init__(parent)

    @property
    def PnTLVList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist.PnTLVList): An instance of the PnTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist import PnTLVList
        return PnTLVList(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('active'))

    @property
    def AdRouteLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AD Route Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('adRouteLabel'))

    @property
    def BVlanId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bVlanId'))

    @property
    def BVlanPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bVlanPriority'))

    @property
    def BVlanTpid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bVlanTpid'))

    @property
    def BackupFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Backup Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('backupFlag'))

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
    def EnableVlanAwareService(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable VLAN Aware Service
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableVlanAwareService'))

    @property
    def EthernetTagId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ethernet Tag ID. For VPWS, this acts as VPWS Service ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ethernetTagId'))

    @property
    def FxcType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FXC Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('fxcType'))

    @property
    def GroupAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('groupAddress'))

    @property
    def IncludeVpwsL2AttrExtComm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include VPWS Layer 2 Attributes Extended Community
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeVpwsL2AttrExtComm'))

    @property
    def L2Mtu(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L2 MTU
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('l2Mtu'))

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
    def NoOfMacPools(self):
        """
        Returns
        -------
        - number: Number of Mac Pools
        """
        return self._get_attribute('noOfMacPools')
    @NoOfMacPools.setter
    def NoOfMacPools(self, value):
        self._set_attribute('noOfMacPools', value)

    @property
    def PrimaryPE(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Primary PE
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('primaryPE'))

    @property
    def RemoteServiceId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remote Service ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('remoteServiceId'))

    @property
    def RequireCW(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Require CW
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('requireCW'))

    @property
    def RootAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Root Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('rootAddress'))

    @property
    def RsvpP2mpId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP P2MP ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('rsvpP2mpId'))

    @property
    def RsvpP2mpIdAsNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP P2MP ID as Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('rsvpP2mpIdAsNumber'))

    @property
    def RsvpTunnelId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP Tunnel ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('rsvpTunnelId'))

    @property
    def SenderAddressPRootNodeAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sender Address/P-Root Node Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('senderAddressPRootNodeAddress'))

    @property
    def UsebVlan(self):
        """
        Returns
        -------
        - bool: Use B-VLAN
        """
        return self._get_attribute('usebVlan')
    @UsebVlan.setter
    def UsebVlan(self, value):
        self._set_attribute('usebVlan', value)

    @property
    def VidNormalization(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VID Normalization
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('vidNormalization'))

    def update(self, Name=None, NoOfMacPools=None, UsebVlan=None):
        """Updates broadcastDomainV6VxlanVpws resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfMacPools (number): Number of Mac Pools
        - UsebVlan (bool): Use B-VLAN

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def get_device_ids(self, PortNames=None, Active=None, AdRouteLabel=None, BVlanId=None, BVlanPriority=None, BVlanTpid=None, BackupFlag=None, EnableVlanAwareService=None, EthernetTagId=None, FxcType=None, GroupAddress=None, IncludeVpwsL2AttrExtComm=None, L2Mtu=None, PrimaryPE=None, RemoteServiceId=None, RequireCW=None, RootAddress=None, RsvpP2mpId=None, RsvpP2mpIdAsNumber=None, RsvpTunnelId=None, SenderAddressPRootNodeAddress=None, VidNormalization=None):
        """Base class infrastructure that gets a list of broadcastDomainV6VxlanVpws device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdRouteLabel (str): optional regex of adRouteLabel
        - BVlanId (str): optional regex of bVlanId
        - BVlanPriority (str): optional regex of bVlanPriority
        - BVlanTpid (str): optional regex of bVlanTpid
        - BackupFlag (str): optional regex of backupFlag
        - EnableVlanAwareService (str): optional regex of enableVlanAwareService
        - EthernetTagId (str): optional regex of ethernetTagId
        - FxcType (str): optional regex of fxcType
        - GroupAddress (str): optional regex of groupAddress
        - IncludeVpwsL2AttrExtComm (str): optional regex of includeVpwsL2AttrExtComm
        - L2Mtu (str): optional regex of l2Mtu
        - PrimaryPE (str): optional regex of primaryPE
        - RemoteServiceId (str): optional regex of remoteServiceId
        - RequireCW (str): optional regex of requireCW
        - RootAddress (str): optional regex of rootAddress
        - RsvpP2mpId (str): optional regex of rsvpP2mpId
        - RsvpP2mpIdAsNumber (str): optional regex of rsvpP2mpIdAsNumber
        - RsvpTunnelId (str): optional regex of rsvpTunnelId
        - SenderAddressPRootNodeAddress (str): optional regex of senderAddressPRootNodeAddress
        - VidNormalization (str): optional regex of vidNormalization

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
