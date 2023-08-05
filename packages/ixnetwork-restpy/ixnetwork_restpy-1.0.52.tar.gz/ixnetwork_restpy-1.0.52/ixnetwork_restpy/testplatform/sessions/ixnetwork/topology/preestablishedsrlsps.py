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


class PreEstablishedSrLsps(Base):
    """Pre-Established SR LSPs
    The PreEstablishedSrLsps class encapsulates a required preEstablishedSrLsps resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'preEstablishedSrLsps'

    def __init__(self, parent):
        super(PreEstablishedSrLsps, self).__init__(parent)

    @property
    def PcepEroSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceperosubobjectslist.PcepEroSubObjectsList): An instance of the PcepEroSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceperosubobjectslist import PcepEroSubObjectsList
        return PcepEroSubObjectsList(self)

    @property
    def PcepMetricSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslist.PcepMetricSubObjectsList): An instance of the PcepMetricSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslist import PcepMetricSubObjectsList
        return PcepMetricSubObjectsList(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
        return Tag(self)

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
    def ActiveDataTrafficEndpoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies whether that specific Data Traffic Endpoint will generate data traffic
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('activeDataTrafficEndpoint'))

    @property
    def AssociationId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Association ID of this LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('associationId'))

    @property
    def Bandwidth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth (bits/sec)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandwidth'))

    @property
    def BindingType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the type of binding included in the TLV. Types are as follows: 20bit MPLS Label 32bit MPLS Label. Default value is 20bit MPLS Label.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bindingType'))

    @property
    def Bos(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This bit is set to True for the last entry in the label stack i.e., for the bottom of the stack, and False for all other label stack entries. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bos'))

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
    def DestinationIpv4Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Destination IPv4 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('destinationIpv4Address'))

    @property
    def ExcludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a type of Resource Affinity Procedure that is used to validate a link. This control accepts a link only if the link carries all of the attributes in the set.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('excludeAny'))

    @property
    def HoldingPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The priority of the LSP with respect to holding resources. The value 0 is the highest priority. Holding Priority is used in deciding whether this session can be preempted by another session.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('holdingPriority'))

    @property
    def IncludeAll(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a type of Resource Affinity Procedure that is used to validate a link. This control excludes a link from consideration if the link carries any of the attributes in the set.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeAll'))

    @property
    def IncludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This is a type of Resource Affinity Procedure that is used to validate a link. This control accepts a link if the link carries any of the attributes in the set.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeAny'))

    @property
    def IncludeBandwidth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Bandwidth will be included in a PCInitiate message. All other attributes in sub-tab-Bandwidth would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeBandwidth'))

    @property
    def IncludeEro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specifies whether ERO is active or inactive. All subsequent attributes of the sub-tab-ERO would be editable only if this is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeEro'))

    @property
    def IncludeLsp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether LSP will be included in a PCInitiate message. All other attributes in sub-tab-LSP would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeLsp'))

    @property
    def IncludeLspa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether LSPA will be included in a PCInitiate message. All other attributes in sub-tab-LSPA would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeLspa'))

    @property
    def IncludeMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether the PCInitiate message will have the metric list that is configured. All subsequent attributes of the sub-tab-Metric would be editable only if this is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeMetric'))

    @property
    def IncludePpag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Association will be included in a Sync PCReport message. All other attributes in sub-tab-PPAG would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includePpag'))

    @property
    def IncludeSrp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeSrp'))

    @property
    def IncludeSymbolicPathNameTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if Symbolic-Path-Name TLV is to be included in PCInitiate message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeSymbolicPathNameTlv'))

    @property
    def IncludeTEPathBindingTLV(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if TE-PATH-BINDING TLV is to be included in PCC Sync LSP.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeTEPathBindingTLV'))

    @property
    def InitialDelegation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Initial Delegation
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('initialDelegation'))

    @property
    def InsertIpv6ExplicitNull(self):
        """
        Returns
        -------
        - bool: Insert IPv6 Explicit Null MPLS header if the traffic type is of type IPv6
        """
        return self._get_attribute('insertIpv6ExplicitNull')
    @InsertIpv6ExplicitNull.setter
    def InsertIpv6ExplicitNull(self, value):
        self._set_attribute('insertIpv6ExplicitNull', value)

    @property
    def LocalProtection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When set, this means that the path must include links protected with Fast Reroute
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('localProtection'))

    @property
    def LspDelegationState(self):
        """
        Returns
        -------
        - list(str[delegated | delegationConfirmed | delegationRejected | delegationReturned | delegationRevoked | nonDelegated | none]): LSP Delegation State
        """
        return self._get_attribute('lspDelegationState')

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This control will be editable if the Binding Type is set to either 20bit or 32bit MPLS-Label. This field will take the 20bit value of the MPLS-Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mplsLabel'))

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
    def NumberOfEroSubObjects(self):
        """
        Returns
        -------
        - number: Value that indicates the number of ERO Sub Objects to be configured.
        """
        return self._get_attribute('numberOfEroSubObjects')
    @NumberOfEroSubObjects.setter
    def NumberOfEroSubObjects(self, value):
        self._set_attribute('numberOfEroSubObjects', value)

    @property
    def NumberOfMetricSubObject(self):
        """
        Returns
        -------
        - number: Value that indicates the number of Metric Objects to be configured.
        """
        return self._get_attribute('numberOfMetricSubObject')
    @NumberOfMetricSubObject.setter
    def NumberOfMetricSubObject(self, value):
        self._set_attribute('numberOfMetricSubObject', value)

    @property
    def OverridePlspId(self):
        """
        Returns
        -------
        - bool: Indicates if PLSP-ID will be set by the state machine or user. If disabled user wont have the control and state machine will set it.
        """
        return self._get_attribute('overridePlspId')
    @OverridePlspId.setter
    def OverridePlspId(self, value):
        self._set_attribute('overridePlspId', value)

    @property
    def PlspId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): An identifier for the LSP. A PCC creates a unique PLSP-ID for each LSP that is constant for the lifetime of a PCEP session. The PCC will advertise the same PLSP-ID on all PCEP sessions it maintains at a given time.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('plspId'))

    @property
    def ProtectionLspBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Protection LSP Bit is On.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('protectionLspBit'))

    @property
    def ReDelegationTimerStatus(self):
        """
        Returns
        -------
        - list(str[expired | none | notStarted | running | stopped]): Re-Delegation Timer Status
        """
        return self._get_attribute('reDelegationTimerStatus')

    @property
    def RedelegationTimeoutInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The period of time a PCC waits for, when a PCEP session is terminated, before revoking LSP delegation to a PCE and attempting to redelegate LSPs associated with the terminated PCEP session to PCE.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('redelegationTimeoutInterval'))

    @property
    def SetupPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The priority of the LSP with respect to taking resources.The value 0 is the highest priority.The Setup Priority is used in deciding whether this session can preempt another session.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('setupPriority'))

    @property
    def SrcEndPointIpv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source IPv4 address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srcEndPointIpv4'))

    @property
    def SrcEndPointIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source IPv6 address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srcEndPointIpv6'))

    @property
    def StandbyLspBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether Standby LSP Bit is On.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('standbyLspBit'))

    @property
    def SymbolicPathName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Each LSP (path) must have a symbolic name that is unique in the PCC. It must remain constant throughout a path's lifetime, which may span across multiple consecutive PCEP sessions and/or PCC restarts.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('symbolicPathName'))

    @property
    def Tc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to carry traffic class information. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('tc'))

    @property
    def Ttl(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to encode a time-to-live value. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ttl'))

    def update(self, InsertIpv6ExplicitNull=None, Name=None, NumberOfEroSubObjects=None, NumberOfMetricSubObject=None, OverridePlspId=None):
        """Updates preEstablishedSrLsps resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - InsertIpv6ExplicitNull (bool): Insert IPv6 Explicit Null MPLS header if the traffic type is of type IPv6
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObject (number): Value that indicates the number of Metric Objects to be configured.
        - OverridePlspId (bool): Indicates if PLSP-ID will be set by the state machine or user. If disabled user wont have the control and state machine will set it.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def get_device_ids(self, PortNames=None, Active=None, ActiveDataTrafficEndpoint=None, AssociationId=None, Bandwidth=None, BindingType=None, Bos=None, DestinationIpv4Address=None, ExcludeAny=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeBandwidth=None, IncludeEro=None, IncludeLsp=None, IncludeLspa=None, IncludeMetric=None, IncludePpag=None, IncludeSrp=None, IncludeSymbolicPathNameTlv=None, IncludeTEPathBindingTLV=None, InitialDelegation=None, LocalProtection=None, MplsLabel=None, PlspId=None, ProtectionLspBit=None, RedelegationTimeoutInterval=None, SetupPriority=None, SrcEndPointIpv4=None, SrcEndPointIpv6=None, StandbyLspBit=None, SymbolicPathName=None, Tc=None, Ttl=None):
        """Base class infrastructure that gets a list of preEstablishedSrLsps device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ActiveDataTrafficEndpoint (str): optional regex of activeDataTrafficEndpoint
        - AssociationId (str): optional regex of associationId
        - Bandwidth (str): optional regex of bandwidth
        - BindingType (str): optional regex of bindingType
        - Bos (str): optional regex of bos
        - DestinationIpv4Address (str): optional regex of destinationIpv4Address
        - ExcludeAny (str): optional regex of excludeAny
        - HoldingPriority (str): optional regex of holdingPriority
        - IncludeAll (str): optional regex of includeAll
        - IncludeAny (str): optional regex of includeAny
        - IncludeBandwidth (str): optional regex of includeBandwidth
        - IncludeEro (str): optional regex of includeEro
        - IncludeLsp (str): optional regex of includeLsp
        - IncludeLspa (str): optional regex of includeLspa
        - IncludeMetric (str): optional regex of includeMetric
        - IncludePpag (str): optional regex of includePpag
        - IncludeSrp (str): optional regex of includeSrp
        - IncludeSymbolicPathNameTlv (str): optional regex of includeSymbolicPathNameTlv
        - IncludeTEPathBindingTLV (str): optional regex of includeTEPathBindingTLV
        - InitialDelegation (str): optional regex of initialDelegation
        - LocalProtection (str): optional regex of localProtection
        - MplsLabel (str): optional regex of mplsLabel
        - PlspId (str): optional regex of plspId
        - ProtectionLspBit (str): optional regex of protectionLspBit
        - RedelegationTimeoutInterval (str): optional regex of redelegationTimeoutInterval
        - SetupPriority (str): optional regex of setupPriority
        - SrcEndPointIpv4 (str): optional regex of srcEndPointIpv4
        - SrcEndPointIpv6 (str): optional regex of srcEndPointIpv6
        - StandbyLspBit (str): optional regex of standbyLspBit
        - SymbolicPathName (str): optional regex of symbolicPathName
        - Tc (str): optional regex of tc
        - Ttl (str): optional regex of ttl

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Delegate(self, *args, **kwargs):
        """Executes the delegate operation on the server.

        Delegate

        delegate(Arg2=list)list
        -----------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('delegate', payload=payload, response_object=None)

    def RevokeDelegation(self, *args, **kwargs):
        """Executes the revokeDelegation operation on the server.

        Revoke Delegation

        revokeDelegation(Arg2=list)list
        -------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('revokeDelegation', payload=payload, response_object=None)
