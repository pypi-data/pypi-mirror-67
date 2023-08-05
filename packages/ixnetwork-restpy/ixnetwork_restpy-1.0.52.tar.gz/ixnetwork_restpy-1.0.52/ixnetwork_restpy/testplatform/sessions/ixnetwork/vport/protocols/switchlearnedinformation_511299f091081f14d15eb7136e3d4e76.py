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


class SwitchLearnedInformation(Base):
    """This object allows to configure the switch learned information parameters.
    The SwitchLearnedInformation class encapsulates a required switchLearnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'switchLearnedInformation'

    def __init__(self, parent):
        super(SwitchLearnedInformation, self).__init__(parent)

    @property
    def OfChannelSwitchLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelswitchlearnedinfo_d072aa31df2ae7f59ee7c558fa30f44f.OfChannelSwitchLearnedInfo): An instance of the OfChannelSwitchLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannelswitchlearnedinfo_d072aa31df2ae7f59ee7c558fa30f44f import OfChannelSwitchLearnedInfo
        return OfChannelSwitchLearnedInfo(self)

    @property
    def SwitchFlow131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflow131triggerattributes_6a434ef978da3f531ba03a3c164a42af.SwitchFlow131TriggerAttributes): An instance of the SwitchFlow131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflow131triggerattributes_6a434ef978da3f531ba03a3c164a42af import SwitchFlow131TriggerAttributes
        return SwitchFlow131TriggerAttributes(self)._select()

    @property
    def SwitchFlowLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowlearnedinfo_17918b5ebece4c9ef28c83b16e87fe3f.SwitchFlowLearnedInfo): An instance of the SwitchFlowLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowlearnedinfo_17918b5ebece4c9ef28c83b16e87fe3f import SwitchFlowLearnedInfo
        return SwitchFlowLearnedInfo(self)

    @property
    def SwitchFlowMatchCriteria131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowmatchcriteria131triggerattributes_346a67e7976ee2e486d6c9f6bb4f592a.SwitchFlowMatchCriteria131TriggerAttributes): An instance of the SwitchFlowMatchCriteria131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchflowmatchcriteria131triggerattributes_346a67e7976ee2e486d6c9f6bb4f592a import SwitchFlowMatchCriteria131TriggerAttributes
        return SwitchFlowMatchCriteria131TriggerAttributes(self)._select()

    @property
    def SwitchGroupLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgrouplearnedinfo_749b8a50084ea9ccd942f4eb5e8fca83.SwitchGroupLearnedInfo): An instance of the SwitchGroupLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgrouplearnedinfo_749b8a50084ea9ccd942f4eb5e8fca83 import SwitchGroupLearnedInfo
        return SwitchGroupLearnedInfo(self)

    @property
    def SwitchMeterLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterlearnedinfo_e2f1bb551eccac275cacd7ff58969fb6.SwitchMeterLearnedInfo): An instance of the SwitchMeterLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterlearnedinfo_e2f1bb551eccac275cacd7ff58969fb6 import SwitchMeterLearnedInfo
        return SwitchMeterLearnedInfo(self)

    @property
    def SwitchTableFeaturesStatLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtablefeaturesstatlearnedinfo_fee7717a999ca279cd83aa9fd8d5481e.SwitchTableFeaturesStatLearnedInfo): An instance of the SwitchTableFeaturesStatLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtablefeaturesstatlearnedinfo_fee7717a999ca279cd83aa9fd8d5481e import SwitchTableFeaturesStatLearnedInfo
        return SwitchTableFeaturesStatLearnedInfo(self)

    @property
    def EnableVendorExperimenterMessage(self):
        """
        Returns
        -------
        - bool: If true, the vendor message trigger configuration parameters are available.
        """
        return self._get_attribute('enableVendorExperimenterMessage')
    @EnableVendorExperimenterMessage.setter
    def EnableVendorExperimenterMessage(self, value):
        self._set_attribute('enableVendorExperimenterMessage', value)

    @property
    def EthernetDestination(self):
        """
        Returns
        -------
        - str: This describes the flow match value for ethernet destination address field.
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
        - str: This describes the flow match value for ethernet source address field.
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
        - str: This describes the Ethernet type of the flow match.
        """
        return self._get_attribute('ethernetType')
    @EthernetType.setter
    def EthernetType(self, value):
        self._set_attribute('ethernetType', value)

    @property
    def InPort(self):
        """
        Returns
        -------
        - str: This describes the flow match value for input port field
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
        - str: This describes the flow match value for IP ToS field.
        """
        return self._get_attribute('ipDscp')
    @IpDscp.setter
    def IpDscp(self, value):
        self._set_attribute('ipDscp', value)

    @property
    def IpProtocol(self):
        """
        Returns
        -------
        - str: This describes the flow match value for IP Protocol field.
        """
        return self._get_attribute('ipProtocol')
    @IpProtocol.setter
    def IpProtocol(self, value):
        self._set_attribute('ipProtocol', value)

    @property
    def Ipv4Source(self):
        """
        Returns
        -------
        - str: This describes the flow match value for IPv4 source address field.
        """
        return self._get_attribute('ipv4Source')
    @Ipv4Source.setter
    def Ipv4Source(self, value):
        self._set_attribute('ipv4Source', value)

    @property
    def Ipv4destination(self):
        """
        Returns
        -------
        - str: This describes the flow match value for IPv4 destination address field.
        """
        return self._get_attribute('ipv4destination')
    @Ipv4destination.setter
    def Ipv4destination(self, value):
        self._set_attribute('ipv4destination', value)

    @property
    def IsOfChannelLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the OF Channels is received.
        """
        return self._get_attribute('isOfChannelLearnedInformationRefreshed')

    @property
    def IsOfFlowsLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Flow Learned Info for the OF Channels is received.
        """
        return self._get_attribute('isOfFlowsLearnedInformationRefreshed')

    @property
    def OutPort(self):
        """
        Returns
        -------
        - number: This describes the flow match value for output port field.
        """
        return self._get_attribute('outPort')
    @OutPort.setter
    def OutPort(self, value):
        self._set_attribute('outPort', value)

    @property
    def OutPortInputMode(self):
        """
        Returns
        -------
        - str(ofppMax | ofppInPort | ofppTable | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | outPortCustom): This describes the output port type.
        """
        return self._get_attribute('outPortInputMode')
    @OutPortInputMode.setter
    def OutPortInputMode(self, value):
        self._set_attribute('outPortInputMode', value)

    @property
    def TableId(self):
        """
        Returns
        -------
        - number: This describes the table identifier. It indicates the next table in the packet processing pipeline.
        """
        return self._get_attribute('tableId')
    @TableId.setter
    def TableId(self, value):
        self._set_attribute('tableId', value)

    @property
    def TableIdInputMode(self):
        """
        Returns
        -------
        - str(allTables | emergency | tableIdCustom): This describes the type of table from which flow statistics will be sought.
        """
        return self._get_attribute('tableIdInputMode')
    @TableIdInputMode.setter
    def TableIdInputMode(self, value):
        self._set_attribute('tableIdInputMode', value)

    @property
    def TansportSource(self):
        """
        Returns
        -------
        - str: This describes the flow match value for transport source field.
        """
        return self._get_attribute('tansportSource')
    @TansportSource.setter
    def TansportSource(self, value):
        self._set_attribute('tansportSource', value)

    @property
    def TransportDestination(self):
        """
        Returns
        -------
        - str: This describes the flow match value for transport destination field.
        """
        return self._get_attribute('transportDestination')
    @TransportDestination.setter
    def TransportDestination(self, value):
        self._set_attribute('transportDestination', value)

    @property
    def VendorExperimenterId(self):
        """
        Returns
        -------
        - number: This describes the ID of the vendor for which vendor message is triggered.
        """
        return self._get_attribute('vendorExperimenterId')
    @VendorExperimenterId.setter
    def VendorExperimenterId(self, value):
        self._set_attribute('vendorExperimenterId', value)

    @property
    def VendorExperimenterType(self):
        """
        Returns
        -------
        - number: This describes the Type of experimenter only for v 1.3.
        """
        return self._get_attribute('vendorExperimenterType')
    @VendorExperimenterType.setter
    def VendorExperimenterType(self, value):
        self._set_attribute('vendorExperimenterType', value)

    @property
    def VendorMessage(self):
        """
        Returns
        -------
        - str: This describes the vendor data of the vendor message trigger.
        """
        return self._get_attribute('vendorMessage')
    @VendorMessage.setter
    def VendorMessage(self, value):
        self._set_attribute('vendorMessage', value)

    @property
    def VendorMessageLength(self):
        """
        Returns
        -------
        - number: This describes the length of vendor data of the vendor message trigger.
        """
        return self._get_attribute('vendorMessageLength')
    @VendorMessageLength.setter
    def VendorMessageLength(self, value):
        self._set_attribute('vendorMessageLength', value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - str: This describes the flow match value for VLAN ID field.
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
        - str: This describes the flow match value for VLAN Priority field.
        """
        return self._get_attribute('vlanPriority')
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute('vlanPriority', value)

    def update(self, EnableVendorExperimenterMessage=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, InPort=None, IpDscp=None, IpProtocol=None, Ipv4Source=None, Ipv4destination=None, OutPort=None, OutPortInputMode=None, TableId=None, TableIdInputMode=None, TansportSource=None, TransportDestination=None, VendorExperimenterId=None, VendorExperimenterType=None, VendorMessage=None, VendorMessageLength=None, VlanId=None, VlanPriority=None):
        """Updates switchLearnedInformation resource on the server.

        Args
        ----
        - EnableVendorExperimenterMessage (bool): If true, the vendor message trigger configuration parameters are available.
        - EthernetDestination (str): This describes the flow match value for ethernet destination address field.
        - EthernetSource (str): This describes the flow match value for ethernet source address field.
        - EthernetType (str): This describes the Ethernet type of the flow match.
        - InPort (str): This describes the flow match value for input port field
        - IpDscp (str): This describes the flow match value for IP ToS field.
        - IpProtocol (str): This describes the flow match value for IP Protocol field.
        - Ipv4Source (str): This describes the flow match value for IPv4 source address field.
        - Ipv4destination (str): This describes the flow match value for IPv4 destination address field.
        - OutPort (number): This describes the flow match value for output port field.
        - OutPortInputMode (str(ofppMax | ofppInPort | ofppTable | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | outPortCustom)): This describes the output port type.
        - TableId (number): This describes the table identifier. It indicates the next table in the packet processing pipeline.
        - TableIdInputMode (str(allTables | emergency | tableIdCustom)): This describes the type of table from which flow statistics will be sought.
        - TansportSource (str): This describes the flow match value for transport source field.
        - TransportDestination (str): This describes the flow match value for transport destination field.
        - VendorExperimenterId (number): This describes the ID of the vendor for which vendor message is triggered.
        - VendorExperimenterType (number): This describes the Type of experimenter only for v 1.3.
        - VendorMessage (str): This describes the vendor data of the vendor message trigger.
        - VendorMessageLength (number): This describes the length of vendor data of the vendor message trigger.
        - VlanId (str): This describes the flow match value for VLAN ID field.
        - VlanPriority (str): This describes the flow match value for VLAN Priority field.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def ClearRecordsForTrigger(self):
        """Executes the clearRecordsForTrigger operation on the server.

        API to clear records for any trigger.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('clearRecordsForTrigger', payload=payload, response_object=None)

    def RefreshFlows(self):
        """Executes the refreshFlows operation on the server.

        This describes that the flows learned information is refreshed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshFlows', payload=payload, response_object=None)

    def RefreshGroupLearnedInformation(self):
        """Executes the refreshGroupLearnedInformation operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshGroupLearnedInformation', payload=payload, response_object=None)

    def RefreshMeterLearnedInformation(self):
        """Executes the refreshMeterLearnedInformation operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshMeterLearnedInformation', payload=payload, response_object=None)

    def RefreshOfChannelLearnedInformation(self):
        """Executes the refreshOfChannelLearnedInformation operation on the server.

        This describes that the ofChannellearned information is refreshed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshOfChannelLearnedInformation', payload=payload, response_object=None)

    def RefreshTableFeature(self):
        """Executes the refreshTableFeature operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshTableFeature', payload=payload, response_object=None)

    def Trigger(self):
        """Executes the trigger operation on the server.

        API to send Trigger.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('trigger', payload=payload, response_object=None)
