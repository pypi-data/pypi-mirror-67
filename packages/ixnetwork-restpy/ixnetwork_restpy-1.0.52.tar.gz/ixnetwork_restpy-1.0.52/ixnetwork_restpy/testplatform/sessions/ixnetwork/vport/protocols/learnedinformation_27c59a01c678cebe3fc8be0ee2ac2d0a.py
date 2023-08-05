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


class LearnedInformation(Base):
    """Indicates the port level aggregated view of Learned Information for per Interface.
    The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedInformation'

    def __init__(self, parent):
        super(LearnedInformation, self).__init__(parent)

    @property
    def AsyncConfStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.asyncconfstatlearnedinformation_b08b1965bae49f51dfcfeee0a9d426f7.AsyncConfStatLearnedInformation): An instance of the AsyncConfStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.asyncconfstatlearnedinformation_b08b1965bae49f51dfcfeee0a9d426f7 import AsyncConfStatLearnedInformation
        return AsyncConfStatLearnedInformation(self)

    @property
    def Controller131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controller131triggerattributes_2819aa69b9d44bae13c83fedb2dddad3.Controller131TriggerAttributes): An instance of the Controller131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controller131triggerattributes_2819aa69b9d44bae13c83fedb2dddad3 import Controller131TriggerAttributes
        return Controller131TriggerAttributes(self)._select()

    @property
    def DescriptionStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.descriptionstatlearnedinformation_f97b98bac1e292641750841538559f5f.DescriptionStatLearnedInformation): An instance of the DescriptionStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.descriptionstatlearnedinformation_f97b98bac1e292641750841538559f5f import DescriptionStatLearnedInformation
        return DescriptionStatLearnedInformation(self)

    @property
    def FlowAggregatedStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatlearnedinformation_eb394be03f1acf9d729fd92ad0560bc7.FlowAggregatedStatLearnedInformation): An instance of the FlowAggregatedStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatlearnedinformation_eb394be03f1acf9d729fd92ad0560bc7 import FlowAggregatedStatLearnedInformation
        return FlowAggregatedStatLearnedInformation(self)

    @property
    def FlowAggregatedStatMatchCriteria131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatmatchcriteria131triggerattributes_8bd0584bfa73f39bffcf44bddb1260c0.FlowAggregatedStatMatchCriteria131TriggerAttributes): An instance of the FlowAggregatedStatMatchCriteria131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatmatchcriteria131triggerattributes_8bd0584bfa73f39bffcf44bddb1260c0 import FlowAggregatedStatMatchCriteria131TriggerAttributes
        return FlowAggregatedStatMatchCriteria131TriggerAttributes(self)._select()

    @property
    def FlowStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatlearnedinformation_4a876cbd88a9437ff767c76cd8ef1e38.FlowStatLearnedInformation): An instance of the FlowStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatlearnedinformation_4a876cbd88a9437ff767c76cd8ef1e38 import FlowStatLearnedInformation
        return FlowStatLearnedInformation(self)

    @property
    def FlowStatMatchCriteria131TriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatmatchcriteria131triggerattributes_fd0bb0e603daa05412f7ea7c62ac7eb7.FlowStatMatchCriteria131TriggerAttributes): An instance of the FlowStatMatchCriteria131TriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatmatchcriteria131triggerattributes_fd0bb0e603daa05412f7ea7c62ac7eb7 import FlowStatMatchCriteria131TriggerAttributes
        return FlowStatMatchCriteria131TriggerAttributes(self)._select()

    @property
    def GroupDescriptionStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupdescriptionstatlearnedinformation_c37cfd4df344ef5bb441c6ddb9c41a04.GroupDescriptionStatLearnedInformation): An instance of the GroupDescriptionStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupdescriptionstatlearnedinformation_c37cfd4df344ef5bb441c6ddb9c41a04 import GroupDescriptionStatLearnedInformation
        return GroupDescriptionStatLearnedInformation(self)

    @property
    def GroupFeatureStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupfeaturestatlearnedinformation_6654288e3ef813eb06af8c9b2ea6e71d.GroupFeatureStatLearnedInformation): An instance of the GroupFeatureStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupfeaturestatlearnedinformation_6654288e3ef813eb06af8c9b2ea6e71d import GroupFeatureStatLearnedInformation
        return GroupFeatureStatLearnedInformation(self)

    @property
    def GroupStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatlearnedinformation_d01b412dc91a12ea79beabfa5f892fec.GroupStatLearnedInformation): An instance of the GroupStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatlearnedinformation_d01b412dc91a12ea79beabfa5f892fec import GroupStatLearnedInformation
        return GroupStatLearnedInformation(self)

    @property
    def MeterConfigStatsLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterconfigstatslearnedinformation_a0e37d863f837b82ab35a0aabe8ddf1e.MeterConfigStatsLearnedInformation): An instance of the MeterConfigStatsLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterconfigstatslearnedinformation_a0e37d863f837b82ab35a0aabe8ddf1e import MeterConfigStatsLearnedInformation
        return MeterConfigStatsLearnedInformation(self)

    @property
    def MeterFeatureStatsLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterfeaturestatslearnedinformation_1092f69d930b3a0dd24a18166d9bbf97.MeterFeatureStatsLearnedInformation): An instance of the MeterFeatureStatsLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterfeaturestatslearnedinformation_1092f69d930b3a0dd24a18166d9bbf97 import MeterFeatureStatsLearnedInformation
        return MeterFeatureStatsLearnedInformation(self)

    @property
    def MeterStatsLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterstatslearnedinformation_8cf2bc3084bf0f27179030930a640791.MeterStatsLearnedInformation): An instance of the MeterStatsLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterstatslearnedinformation_8cf2bc3084bf0f27179030930a640791 import MeterStatsLearnedInformation
        return MeterStatsLearnedInformation(self)

    @property
    def OfChannelLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannellearnedinformation_ef1e36cc1485b6bcb1cf5aba40505e4e.OfChannelLearnedInformation): An instance of the OfChannelLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannellearnedinformation_ef1e36cc1485b6bcb1cf5aba40505e4e import OfChannelLearnedInformation
        return OfChannelLearnedInformation(self)

    @property
    def PacketOutTriggerActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetouttriggeractions_231f7c469c47c383b2c8de99617924de.PacketOutTriggerActions): An instance of the PacketOutTriggerActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetouttriggeractions_231f7c469c47c383b2c8de99617924de import PacketOutTriggerActions
        return PacketOutTriggerActions(self)

    @property
    def PortFeaturesLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portfeatureslearnedinformation_e7fc7ca93da92cbc2b387ce9a264fee9.PortFeaturesLearnedInformation): An instance of the PortFeaturesLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portfeatureslearnedinformation_e7fc7ca93da92cbc2b387ce9a264fee9 import PortFeaturesLearnedInformation
        return PortFeaturesLearnedInformation(self)

    @property
    def PortModificationTriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portmodificationtriggerattributes_243e90e3cc83da46c5d0d0454bddba11.PortModificationTriggerAttributes): An instance of the PortModificationTriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portmodificationtriggerattributes_243e90e3cc83da46c5d0d0454bddba11 import PortModificationTriggerAttributes
        return PortModificationTriggerAttributes(self)._select()

    @property
    def PortStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatlearnedinformation_46b05eb89a5db488cec05d084f579bb9.PortStatLearnedInformation): An instance of the PortStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatlearnedinformation_46b05eb89a5db488cec05d084f579bb9 import PortStatLearnedInformation
        return PortStatLearnedInformation(self)

    @property
    def QueueConfigLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueconfiglearnedinformation_5d930b646d1e560e17d7290683ca2cfb.QueueConfigLearnedInformation): An instance of the QueueConfigLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueconfiglearnedinformation_5d930b646d1e560e17d7290683ca2cfb import QueueConfigLearnedInformation
        return QueueConfigLearnedInformation(self)

    @property
    def QueueStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queuestatlearnedinformation_2fbe3f59a038d0bd09df0a885f9e3682.QueueStatLearnedInformation): An instance of the QueueStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queuestatlearnedinformation_2fbe3f59a038d0bd09df0a885f9e3682 import QueueStatLearnedInformation
        return QueueStatLearnedInformation(self)

    @property
    def SwitchConfigLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchconfiglearnedinformation_52fc60e3e6ce65750d119a2ce8bf796b.SwitchConfigLearnedInformation): An instance of the SwitchConfigLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchconfiglearnedinformation_52fc60e3e6ce65750d119a2ce8bf796b import SwitchConfigLearnedInformation
        return SwitchConfigLearnedInformation(self)

    @property
    def TableFeaturePropertiesTrigger(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeaturepropertiestrigger_f0afa99a6d309a9f6841328848dc57e8.TableFeaturePropertiesTrigger): An instance of the TableFeaturePropertiesTrigger class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeaturepropertiestrigger_f0afa99a6d309a9f6841328848dc57e8 import TableFeaturePropertiesTrigger
        return TableFeaturePropertiesTrigger(self)

    @property
    def TableFeaturesLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeatureslearnedinformation_94c27ca516a413753cf89b4b81274faf.TableFeaturesLearnedInformation): An instance of the TableFeaturesLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeatureslearnedinformation_94c27ca516a413753cf89b4b81274faf import TableFeaturesLearnedInformation
        return TableFeaturesLearnedInformation(self)

    @property
    def TableStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablestatlearnedinformation_b51aa6814c28e085bfe34f3fd773ce36.TableStatLearnedInformation): An instance of the TableStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablestatlearnedinformation_b51aa6814c28e085bfe34f3fd773ce36 import TableStatLearnedInformation
        return TableStatLearnedInformation(self)

    @property
    def VendorStatLearnedInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vendorstatlearnedinformation_768c47d4fc3dfc39e1df572805904907.VendorStatLearnedInformation): An instance of the VendorStatLearnedInformation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vendorstatlearnedinformation_768c47d4fc3dfc39e1df572805904907 import VendorStatLearnedInformation
        return VendorStatLearnedInformation(self)

    @property
    def AsyncConfStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('asyncConfStatResponseTimeOut')
    @AsyncConfStatResponseTimeOut.setter
    def AsyncConfStatResponseTimeOut(self, value):
        self._set_attribute('asyncConfStatResponseTimeOut', value)

    @property
    def DescriptionStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no description statistics response is received.
        """
        return self._get_attribute('descriptionStatResponseTimeOut')
    @DescriptionStatResponseTimeOut.setter
    def DescriptionStatResponseTimeOut(self, value):
        self._set_attribute('descriptionStatResponseTimeOut', value)

    @property
    def EnableAsyncConfMasterFlowRemovedFlowDelete(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Flow Delete is received.
        """
        return self._get_attribute('enableAsyncConfMasterFlowRemovedFlowDelete')
    @EnableAsyncConfMasterFlowRemovedFlowDelete.setter
    def EnableAsyncConfMasterFlowRemovedFlowDelete(self, value):
        self._set_attribute('enableAsyncConfMasterFlowRemovedFlowDelete', value)

    @property
    def EnableAsyncConfMasterFlowRemovedGroupDelete(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Group Delete is received.
        """
        return self._get_attribute('enableAsyncConfMasterFlowRemovedGroupDelete')
    @EnableAsyncConfMasterFlowRemovedGroupDelete.setter
    def EnableAsyncConfMasterFlowRemovedGroupDelete(self, value):
        self._set_attribute('enableAsyncConfMasterFlowRemovedGroupDelete', value)

    @property
    def EnableAsyncConfMasterFlowRemovedHardTimeOut(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Hard Time Out is received.
        """
        return self._get_attribute('enableAsyncConfMasterFlowRemovedHardTimeOut')
    @EnableAsyncConfMasterFlowRemovedHardTimeOut.setter
    def EnableAsyncConfMasterFlowRemovedHardTimeOut(self, value):
        self._set_attribute('enableAsyncConfMasterFlowRemovedHardTimeOut', value)

    @property
    def EnableAsyncConfMasterFlowRemovedIdleTimeOut(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableAsyncConfMasterFlowRemovedIdleTimeOut')
    @EnableAsyncConfMasterFlowRemovedIdleTimeOut.setter
    def EnableAsyncConfMasterFlowRemovedIdleTimeOut(self, value):
        self._set_attribute('enableAsyncConfMasterFlowRemovedIdleTimeOut', value)

    @property
    def EnableAsyncConfMasterPacketInActionOutputToController(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Action Output To Controller is received.
        """
        return self._get_attribute('enableAsyncConfMasterPacketInActionOutputToController')
    @EnableAsyncConfMasterPacketInActionOutputToController.setter
    def EnableAsyncConfMasterPacketInActionOutputToController(self, value):
        self._set_attribute('enableAsyncConfMasterPacketInActionOutputToController', value)

    @property
    def EnableAsyncConfMasterPacketInInvalidTtl(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Invalid Ttl is received.
        """
        return self._get_attribute('enableAsyncConfMasterPacketInInvalidTtl')
    @EnableAsyncConfMasterPacketInInvalidTtl.setter
    def EnableAsyncConfMasterPacketInInvalidTtl(self, value):
        self._set_attribute('enableAsyncConfMasterPacketInInvalidTtl', value)

    @property
    def EnableAsyncConfMasterPacketInNoMatching(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Packet In No Matching is received.
        """
        return self._get_attribute('enableAsyncConfMasterPacketInNoMatching')
    @EnableAsyncConfMasterPacketInNoMatching.setter
    def EnableAsyncConfMasterPacketInNoMatching(self, value):
        self._set_attribute('enableAsyncConfMasterPacketInNoMatching', value)

    @property
    def EnableAsyncConfMasterPortStatusAdd(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Add is received.
        """
        return self._get_attribute('enableAsyncConfMasterPortStatusAdd')
    @EnableAsyncConfMasterPortStatusAdd.setter
    def EnableAsyncConfMasterPortStatusAdd(self, value):
        self._set_attribute('enableAsyncConfMasterPortStatusAdd', value)

    @property
    def EnableAsyncConfMasterPortStatusDelete(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Delete is received.
        """
        return self._get_attribute('enableAsyncConfMasterPortStatusDelete')
    @EnableAsyncConfMasterPortStatusDelete.setter
    def EnableAsyncConfMasterPortStatusDelete(self, value):
        self._set_attribute('enableAsyncConfMasterPortStatusDelete', value)

    @property
    def EnableAsyncConfMasterPortStatusModify(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
        """
        return self._get_attribute('enableAsyncConfMasterPortStatusModify')
    @EnableAsyncConfMasterPortStatusModify.setter
    def EnableAsyncConfMasterPortStatusModify(self, value):
        self._set_attribute('enableAsyncConfMasterPortStatusModify', value)

    @property
    def EnableAsyncConfSlaveFlowRemovedFlowDelete(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Flow Delete is received.
        """
        return self._get_attribute('enableAsyncConfSlaveFlowRemovedFlowDelete')
    @EnableAsyncConfSlaveFlowRemovedFlowDelete.setter
    def EnableAsyncConfSlaveFlowRemovedFlowDelete(self, value):
        self._set_attribute('enableAsyncConfSlaveFlowRemovedFlowDelete', value)

    @property
    def EnableAsyncConfSlaveFlowRemovedGroupDelete(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Group Delete is received.
        """
        return self._get_attribute('enableAsyncConfSlaveFlowRemovedGroupDelete')
    @EnableAsyncConfSlaveFlowRemovedGroupDelete.setter
    def EnableAsyncConfSlaveFlowRemovedGroupDelete(self, value):
        self._set_attribute('enableAsyncConfSlaveFlowRemovedGroupDelete', value)

    @property
    def EnableAsyncConfSlaveFlowRemovedHardTimeOut(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Hard Time Out is received.
        """
        return self._get_attribute('enableAsyncConfSlaveFlowRemovedHardTimeOut')
    @EnableAsyncConfSlaveFlowRemovedHardTimeOut.setter
    def EnableAsyncConfSlaveFlowRemovedHardTimeOut(self, value):
        self._set_attribute('enableAsyncConfSlaveFlowRemovedHardTimeOut', value)

    @property
    def EnableAsyncConfSlaveFlowRemovedIdleTimeOut(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Idle Time Out is received.
        """
        return self._get_attribute('enableAsyncConfSlaveFlowRemovedIdleTimeOut')
    @EnableAsyncConfSlaveFlowRemovedIdleTimeOut.setter
    def EnableAsyncConfSlaveFlowRemovedIdleTimeOut(self, value):
        self._set_attribute('enableAsyncConfSlaveFlowRemovedIdleTimeOut', value)

    @property
    def EnableAsyncConfSlavePacketInActionOutputToController(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Action Output To Controller is received.
        """
        return self._get_attribute('enableAsyncConfSlavePacketInActionOutputToController')
    @EnableAsyncConfSlavePacketInActionOutputToController.setter
    def EnableAsyncConfSlavePacketInActionOutputToController(self, value):
        self._set_attribute('enableAsyncConfSlavePacketInActionOutputToController', value)

    @property
    def EnableAsyncConfSlavePacketInInvalidTtl(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Invalid Ttl is received.
        """
        return self._get_attribute('enableAsyncConfSlavePacketInInvalidTtl')
    @EnableAsyncConfSlavePacketInInvalidTtl.setter
    def EnableAsyncConfSlavePacketInInvalidTtl(self, value):
        self._set_attribute('enableAsyncConfSlavePacketInInvalidTtl', value)

    @property
    def EnableAsyncConfSlavePacketInNoMatching(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In No Matching is received.
        """
        return self._get_attribute('enableAsyncConfSlavePacketInNoMatching')
    @EnableAsyncConfSlavePacketInNoMatching.setter
    def EnableAsyncConfSlavePacketInNoMatching(self, value):
        self._set_attribute('enableAsyncConfSlavePacketInNoMatching', value)

    @property
    def EnableAsyncConfSlavePortStatusAdd(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Add is received.
        """
        return self._get_attribute('enableAsyncConfSlavePortStatusAdd')
    @EnableAsyncConfSlavePortStatusAdd.setter
    def EnableAsyncConfSlavePortStatusAdd(self, value):
        self._set_attribute('enableAsyncConfSlavePortStatusAdd', value)

    @property
    def EnableAsyncConfSlavePortStatusDelete(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
        """
        return self._get_attribute('enableAsyncConfSlavePortStatusDelete')
    @EnableAsyncConfSlavePortStatusDelete.setter
    def EnableAsyncConfSlavePortStatusDelete(self, value):
        self._set_attribute('enableAsyncConfSlavePortStatusDelete', value)

    @property
    def EnableAsyncConfSlavePortStatusModify(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Modify is received.
        """
        return self._get_attribute('enableAsyncConfSlavePortStatusModify')
    @EnableAsyncConfSlavePortStatusModify.setter
    def EnableAsyncConfSlavePortStatusModify(self, value):
        self._set_attribute('enableAsyncConfSlavePortStatusModify', value)

    @property
    def EnableFlowAggregatedStatMatchCapability(self):
        """
        Returns
        -------
        - bool: Checks to see if the switch has the capability to publish Flow Aggregated Statistics
        """
        return self._get_attribute('enableFlowAggregatedStatMatchCapability')
    @EnableFlowAggregatedStatMatchCapability.setter
    def EnableFlowAggregatedStatMatchCapability(self, value):
        self._set_attribute('enableFlowAggregatedStatMatchCapability', value)

    @property
    def EnableFlowStatMatchCapability(self):
        """
        Returns
        -------
        - bool: Checks to see if the switch has the capability to publish Flow Statistics
        """
        return self._get_attribute('enableFlowStatMatchCapability')
    @EnableFlowStatMatchCapability.setter
    def EnableFlowStatMatchCapability(self, value):
        self._set_attribute('enableFlowStatMatchCapability', value)

    @property
    def EnableGroupStatMatchCapability(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Group Statistics Match Capability is received.
        """
        return self._get_attribute('enableGroupStatMatchCapability')
    @EnableGroupStatMatchCapability.setter
    def EnableGroupStatMatchCapability(self, value):
        self._set_attribute('enableGroupStatMatchCapability', value)

    @property
    def EnablePortStatMatchCapability(self):
        """
        Returns
        -------
        - bool: Checks to see if the switch has the capability to publish Port Statistics
        """
        return self._get_attribute('enablePortStatMatchCapability')
    @EnablePortStatMatchCapability.setter
    def EnablePortStatMatchCapability(self, value):
        self._set_attribute('enablePortStatMatchCapability', value)

    @property
    def EnableQueueStatMatchCapability(self):
        """
        Returns
        -------
        - bool: If true, the switch has the capability to publish Queue Statistics.
        """
        return self._get_attribute('enableQueueStatMatchCapability')
    @EnableQueueStatMatchCapability.setter
    def EnableQueueStatMatchCapability(self, value):
        self._set_attribute('enableQueueStatMatchCapability', value)

    @property
    def EnableSendTableFeaturesTrigger(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Send Table Features Trigger is received.
        """
        return self._get_attribute('enableSendTableFeaturesTrigger')
    @EnableSendTableFeaturesTrigger.setter
    def EnableSendTableFeaturesTrigger(self, value):
        self._set_attribute('enableSendTableFeaturesTrigger', value)

    @property
    def EnableSendTriggerPortFeaturesLearnedInformation(self):
        """
        Returns
        -------
        - bool: Enables Trigger for port features learned information.
        """
        return self._get_attribute('enableSendTriggerPortFeaturesLearnedInformation')
    @EnableSendTriggerPortFeaturesLearnedInformation.setter
    def EnableSendTriggerPortFeaturesLearnedInformation(self, value):
        self._set_attribute('enableSendTriggerPortFeaturesLearnedInformation', value)

    @property
    def EnableSendTriggeredAsyncConfStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the Triggered Asynchronous Configuration Statistics Learned Information is received.
        """
        return self._get_attribute('enableSendTriggeredAsyncConfStatLearnedInformation')
    @EnableSendTriggeredAsyncConfStatLearnedInformation.setter
    def EnableSendTriggeredAsyncConfStatLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredAsyncConfStatLearnedInformation', value)

    @property
    def EnableSendTriggeredBarrierRequestMessage(self):
        """
        Returns
        -------
        - bool: If true, enables trigger for barrier request message
        """
        return self._get_attribute('enableSendTriggeredBarrierRequestMessage')
    @EnableSendTriggeredBarrierRequestMessage.setter
    def EnableSendTriggeredBarrierRequestMessage(self, value):
        self._set_attribute('enableSendTriggeredBarrierRequestMessage', value)

    @property
    def EnableSendTriggeredDescriptionStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: If true, the description statistic trigger configuration parameters are available.
        """
        return self._get_attribute('enableSendTriggeredDescriptionStatLearnedInformation')
    @EnableSendTriggeredDescriptionStatLearnedInformation.setter
    def EnableSendTriggeredDescriptionStatLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredDescriptionStatLearnedInformation', value)

    @property
    def EnableSendTriggeredFlowAggregatedStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: If true, the flow aggregated statistic trigger configuration parameters are available.
        """
        return self._get_attribute('enableSendTriggeredFlowAggregatedStatLearnedInformation')
    @EnableSendTriggeredFlowAggregatedStatLearnedInformation.setter
    def EnableSendTriggeredFlowAggregatedStatLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredFlowAggregatedStatLearnedInformation', value)

    @property
    def EnableSendTriggeredFlowStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: If true, the flow statistic trigger configuration parameters are available.
        """
        return self._get_attribute('enableSendTriggeredFlowStatLearnedInformation')
    @EnableSendTriggeredFlowStatLearnedInformation.setter
    def EnableSendTriggeredFlowStatLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredFlowStatLearnedInformation', value)

    @property
    def EnableSendTriggeredGroupDescriptionStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Send Triggered Group Description Statistics Learned Information is received.
        """
        return self._get_attribute('enableSendTriggeredGroupDescriptionStatLearnedInformation')
    @EnableSendTriggeredGroupDescriptionStatLearnedInformation.setter
    def EnableSendTriggeredGroupDescriptionStatLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredGroupDescriptionStatLearnedInformation', value)

    @property
    def EnableSendTriggeredGroupFeatureStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Send Triggered Group Feature Statistics Learned Information is received.
        """
        return self._get_attribute('enableSendTriggeredGroupFeatureStatLearnedInformation')
    @EnableSendTriggeredGroupFeatureStatLearnedInformation.setter
    def EnableSendTriggeredGroupFeatureStatLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredGroupFeatureStatLearnedInformation', value)

    @property
    def EnableSendTriggeredGroupStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the Send Triggered Group Statistics Learned Information is received.
        """
        return self._get_attribute('enableSendTriggeredGroupStatLearnedInformation')
    @EnableSendTriggeredGroupStatLearnedInformation.setter
    def EnableSendTriggeredGroupStatLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredGroupStatLearnedInformation', value)

    @property
    def EnableSendTriggeredPacketOutMessage(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Send Triggered Packet Out Message is received.
        """
        return self._get_attribute('enableSendTriggeredPacketOutMessage')
    @EnableSendTriggeredPacketOutMessage.setter
    def EnableSendTriggeredPacketOutMessage(self, value):
        self._set_attribute('enableSendTriggeredPacketOutMessage', value)

    @property
    def EnableSendTriggeredPortModificationMessage(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Send Triggered Port Modification Message is received.
        """
        return self._get_attribute('enableSendTriggeredPortModificationMessage')
    @EnableSendTriggeredPortModificationMessage.setter
    def EnableSendTriggeredPortModificationMessage(self, value):
        self._set_attribute('enableSendTriggeredPortModificationMessage', value)

    @property
    def EnableSendTriggeredPortStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: If true, the port statistic trigger configuration parameters are available.
        """
        return self._get_attribute('enableSendTriggeredPortStatLearnedInformation')
    @EnableSendTriggeredPortStatLearnedInformation.setter
    def EnableSendTriggeredPortStatLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredPortStatLearnedInformation', value)

    @property
    def EnableSendTriggeredQueueConfigLearnedInformation(self):
        """
        Returns
        -------
        - bool: If true, the queue config trigger configuration parameters are available.
        """
        return self._get_attribute('enableSendTriggeredQueueConfigLearnedInformation')
    @EnableSendTriggeredQueueConfigLearnedInformation.setter
    def EnableSendTriggeredQueueConfigLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredQueueConfigLearnedInformation', value)

    @property
    def EnableSendTriggeredQueueStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: If true, the queue statistic trigger configuration parameters are available.
        """
        return self._get_attribute('enableSendTriggeredQueueStatLearnedInformation')
    @EnableSendTriggeredQueueStatLearnedInformation.setter
    def EnableSendTriggeredQueueStatLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredQueueStatLearnedInformation', value)

    @property
    def EnableSendTriggeredRoleRequestMessage(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the Triggered Role Request Message is received.
        """
        return self._get_attribute('enableSendTriggeredRoleRequestMessage')
    @EnableSendTriggeredRoleRequestMessage.setter
    def EnableSendTriggeredRoleRequestMessage(self, value):
        self._set_attribute('enableSendTriggeredRoleRequestMessage', value)

    @property
    def EnableSendTriggeredSwitchConfigLearnedInformation(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Switch Configuration Learned Information is received.
        """
        return self._get_attribute('enableSendTriggeredSwitchConfigLearnedInformation')
    @EnableSendTriggeredSwitchConfigLearnedInformation.setter
    def EnableSendTriggeredSwitchConfigLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredSwitchConfigLearnedInformation', value)

    @property
    def EnableSendTriggeredTableStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: If true, the table statistic trigger configuration parameters are available.
        """
        return self._get_attribute('enableSendTriggeredTableStatLearnedInformation')
    @EnableSendTriggeredTableStatLearnedInformation.setter
    def EnableSendTriggeredTableStatLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredTableStatLearnedInformation', value)

    @property
    def EnableSendTriggeredVendorStatLearnedInformation(self):
        """
        Returns
        -------
        - bool: If true, the vendor statistic trigger configuration parameters are available.
        """
        return self._get_attribute('enableSendTriggeredVendorStatLearnedInformation')
    @EnableSendTriggeredVendorStatLearnedInformation.setter
    def EnableSendTriggeredVendorStatLearnedInformation(self, value):
        self._set_attribute('enableSendTriggeredVendorStatLearnedInformation', value)

    @property
    def EnableSetAsyncConfig(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the Set Asynchronous Configuration is received.
        """
        return self._get_attribute('enableSetAsyncConfig')
    @EnableSetAsyncConfig.setter
    def EnableSetAsyncConfig(self, value):
        self._set_attribute('enableSetAsyncConfig', value)

    @property
    def EnableSetSwitchConfig(self):
        """
        Returns
        -------
        - bool: If enabled,it denotes that the enable Set Switch Configuration is received.
        """
        return self._get_attribute('enableSetSwitchConfig')
    @EnableSetSwitchConfig.setter
    def EnableSetSwitchConfig(self, value):
        self._set_attribute('enableSetSwitchConfig', value)

    @property
    def EnableSetTableFeatures(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableSetTableFeatures')
    @EnableSetTableFeatures.setter
    def EnableSetTableFeatures(self, value):
        self._set_attribute('enableSetTableFeatures', value)

    @property
    def EnableTableStatMatchCapability(self):
        """
        Returns
        -------
        - bool: If true, the switch has the capability to publish Table Statistics.
        """
        return self._get_attribute('enableTableStatMatchCapability')
    @EnableTableStatMatchCapability.setter
    def EnableTableStatMatchCapability(self, value):
        self._set_attribute('enableTableStatMatchCapability', value)

    @property
    def EnableTriggeredVendorMessage(self):
        """
        Returns
        -------
        - bool: If true, the vendor message trigger configuration parameters are available.
        """
        return self._get_attribute('enableTriggeredVendorMessage')
    @EnableTriggeredVendorMessage.setter
    def EnableTriggeredVendorMessage(self, value):
        self._set_attribute('enableTriggeredVendorMessage', value)

    @property
    def FlowAggregatedStatEthernetDestination(self):
        """
        Returns
        -------
        - str: Signifies the ethernet destination address.
        """
        return self._get_attribute('flowAggregatedStatEthernetDestination')
    @FlowAggregatedStatEthernetDestination.setter
    def FlowAggregatedStatEthernetDestination(self, value):
        self._set_attribute('flowAggregatedStatEthernetDestination', value)

    @property
    def FlowAggregatedStatEthernetSource(self):
        """
        Returns
        -------
        - str: Signifies the ethernet source address.
        """
        return self._get_attribute('flowAggregatedStatEthernetSource')
    @FlowAggregatedStatEthernetSource.setter
    def FlowAggregatedStatEthernetSource(self, value):
        self._set_attribute('flowAggregatedStatEthernetSource', value)

    @property
    def FlowAggregatedStatEthernetType(self):
        """
        Returns
        -------
        - str: Signifies the type of Ethernet used.
        """
        return self._get_attribute('flowAggregatedStatEthernetType')
    @FlowAggregatedStatEthernetType.setter
    def FlowAggregatedStatEthernetType(self, value):
        self._set_attribute('flowAggregatedStatEthernetType', value)

    @property
    def FlowAggregatedStatInPort(self):
        """
        Returns
        -------
        - str: Signifies the input port used.
        """
        return self._get_attribute('flowAggregatedStatInPort')
    @FlowAggregatedStatInPort.setter
    def FlowAggregatedStatInPort(self, value):
        self._set_attribute('flowAggregatedStatInPort', value)

    @property
    def FlowAggregatedStatIpDscp(self):
        """
        Returns
        -------
        - str: Signifies the IP DSCP value for advertising.
        """
        return self._get_attribute('flowAggregatedStatIpDscp')
    @FlowAggregatedStatIpDscp.setter
    def FlowAggregatedStatIpDscp(self, value):
        self._set_attribute('flowAggregatedStatIpDscp', value)

    @property
    def FlowAggregatedStatIpProtocol(self):
        """
        Returns
        -------
        - str: Signifies the IP protocol used.
        """
        return self._get_attribute('flowAggregatedStatIpProtocol')
    @FlowAggregatedStatIpProtocol.setter
    def FlowAggregatedStatIpProtocol(self, value):
        self._set_attribute('flowAggregatedStatIpProtocol', value)

    @property
    def FlowAggregatedStatIpv4Destination(self):
        """
        Returns
        -------
        - str: Signifies the IPv4 destination address.
        """
        return self._get_attribute('flowAggregatedStatIpv4Destination')
    @FlowAggregatedStatIpv4Destination.setter
    def FlowAggregatedStatIpv4Destination(self, value):
        self._set_attribute('flowAggregatedStatIpv4Destination', value)

    @property
    def FlowAggregatedStatIpv4Source(self):
        """
        Returns
        -------
        - str: Signifies the IPv4 source address.
        """
        return self._get_attribute('flowAggregatedStatIpv4Source')
    @FlowAggregatedStatIpv4Source.setter
    def FlowAggregatedStatIpv4Source(self, value):
        self._set_attribute('flowAggregatedStatIpv4Source', value)

    @property
    def FlowAggregatedStatOutPortInputMode(self):
        """
        Returns
        -------
        - str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom): Signifies the identifier output mode of the aggregated flow statistics table.
        """
        return self._get_attribute('flowAggregatedStatOutPortInputMode')
    @FlowAggregatedStatOutPortInputMode.setter
    def FlowAggregatedStatOutPortInputMode(self, value):
        self._set_attribute('flowAggregatedStatOutPortInputMode', value)

    @property
    def FlowAggregatedStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no flow aggregated statistics response is received.
        """
        return self._get_attribute('flowAggregatedStatResponseTimeOut')
    @FlowAggregatedStatResponseTimeOut.setter
    def FlowAggregatedStatResponseTimeOut(self, value):
        self._set_attribute('flowAggregatedStatResponseTimeOut', value)

    @property
    def FlowAggregatedStatTableIdInputMode(self):
        """
        Returns
        -------
        - str(allTables | emergency | custom): Signifies the identifier input mode of the flow aggregated statistics table.
        """
        return self._get_attribute('flowAggregatedStatTableIdInputMode')
    @FlowAggregatedStatTableIdInputMode.setter
    def FlowAggregatedStatTableIdInputMode(self, value):
        self._set_attribute('flowAggregatedStatTableIdInputMode', value)

    @property
    def FlowAggregatedStatTableIdInputModeNumber(self):
        """
        Returns
        -------
        - number: Signifies the identifier input mode of the flow aggregated statistics table.
        """
        return self._get_attribute('flowAggregatedStatTableIdInputModeNumber')
    @FlowAggregatedStatTableIdInputModeNumber.setter
    def FlowAggregatedStatTableIdInputModeNumber(self, value):
        self._set_attribute('flowAggregatedStatTableIdInputModeNumber', value)

    @property
    def FlowAggregatedStatTransportDestination(self):
        """
        Returns
        -------
        - str: Signifies the Transport destination address.
        """
        return self._get_attribute('flowAggregatedStatTransportDestination')
    @FlowAggregatedStatTransportDestination.setter
    def FlowAggregatedStatTransportDestination(self, value):
        self._set_attribute('flowAggregatedStatTransportDestination', value)

    @property
    def FlowAggregatedStatTransportSource(self):
        """
        Returns
        -------
        - str: Signifies the Transport source address.
        """
        return self._get_attribute('flowAggregatedStatTransportSource')
    @FlowAggregatedStatTransportSource.setter
    def FlowAggregatedStatTransportSource(self, value):
        self._set_attribute('flowAggregatedStatTransportSource', value)

    @property
    def FlowAggregatedStatVlanId(self):
        """
        Returns
        -------
        - str: Signifies the unique VLAN Identifier.
        """
        return self._get_attribute('flowAggregatedStatVlanId')
    @FlowAggregatedStatVlanId.setter
    def FlowAggregatedStatVlanId(self, value):
        self._set_attribute('flowAggregatedStatVlanId', value)

    @property
    def FlowAggregatedStatVlanPriority(self):
        """
        Returns
        -------
        - str: Signifies the User Priority for this VLAN.
        """
        return self._get_attribute('flowAggregatedStatVlanPriority')
    @FlowAggregatedStatVlanPriority.setter
    def FlowAggregatedStatVlanPriority(self, value):
        self._set_attribute('flowAggregatedStatVlanPriority', value)

    @property
    def FlowStatEthernetDestination(self):
        """
        Returns
        -------
        - str: Specifies the Ethernet destination address.
        """
        return self._get_attribute('flowStatEthernetDestination')
    @FlowStatEthernetDestination.setter
    def FlowStatEthernetDestination(self, value):
        self._set_attribute('flowStatEthernetDestination', value)

    @property
    def FlowStatEthernetSource(self):
        """
        Returns
        -------
        - str: Specifies the Ethernet source address.
        """
        return self._get_attribute('flowStatEthernetSource')
    @FlowStatEthernetSource.setter
    def FlowStatEthernetSource(self, value):
        self._set_attribute('flowStatEthernetSource', value)

    @property
    def FlowStatEthernetType(self):
        """
        Returns
        -------
        - str: Specifies the type of Ethernet used.
        """
        return self._get_attribute('flowStatEthernetType')
    @FlowStatEthernetType.setter
    def FlowStatEthernetType(self, value):
        self._set_attribute('flowStatEthernetType', value)

    @property
    def FlowStatInPort(self):
        """
        Returns
        -------
        - str: Specifies the input port used.
        """
        return self._get_attribute('flowStatInPort')
    @FlowStatInPort.setter
    def FlowStatInPort(self, value):
        self._set_attribute('flowStatInPort', value)

    @property
    def FlowStatIpDscp(self):
        """
        Returns
        -------
        - str: Specifies the IP DSCP value for advertising.
        """
        return self._get_attribute('flowStatIpDscp')
    @FlowStatIpDscp.setter
    def FlowStatIpDscp(self, value):
        self._set_attribute('flowStatIpDscp', value)

    @property
    def FlowStatIpProtocol(self):
        """
        Returns
        -------
        - str: Specifies the IP protocol used.
        """
        return self._get_attribute('flowStatIpProtocol')
    @FlowStatIpProtocol.setter
    def FlowStatIpProtocol(self, value):
        self._set_attribute('flowStatIpProtocol', value)

    @property
    def FlowStatIpv4Destination(self):
        """
        Returns
        -------
        - str: Specifies the The IPv4 destination address.
        """
        return self._get_attribute('flowStatIpv4Destination')
    @FlowStatIpv4Destination.setter
    def FlowStatIpv4Destination(self, value):
        self._set_attribute('flowStatIpv4Destination', value)

    @property
    def FlowStatIpv4Source(self):
        """
        Returns
        -------
        - str: Specifies the The IPv4 source address.
        """
        return self._get_attribute('flowStatIpv4Source')
    @FlowStatIpv4Source.setter
    def FlowStatIpv4Source(self, value):
        self._set_attribute('flowStatIpv4Source', value)

    @property
    def FlowStatOutPortInputMode(self):
        """
        Returns
        -------
        - str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom): Specifies the output mode of the Table identifier.
        """
        return self._get_attribute('flowStatOutPortInputMode')
    @FlowStatOutPortInputMode.setter
    def FlowStatOutPortInputMode(self, value):
        self._set_attribute('flowStatOutPortInputMode', value)

    @property
    def FlowStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no response is received.
        """
        return self._get_attribute('flowStatResponseTimeOut')
    @FlowStatResponseTimeOut.setter
    def FlowStatResponseTimeOut(self, value):
        self._set_attribute('flowStatResponseTimeOut', value)

    @property
    def FlowStatTableIdInputMode(self):
        """
        Returns
        -------
        - str(allTables | emergency | custom): Specifies the input mode of the Table identifier.
        """
        return self._get_attribute('flowStatTableIdInputMode')
    @FlowStatTableIdInputMode.setter
    def FlowStatTableIdInputMode(self, value):
        self._set_attribute('flowStatTableIdInputMode', value)

    @property
    def FlowStatTableIdInputModeNumber(self):
        """
        Returns
        -------
        - number: Signifies the identifier input mode of the flow statistics table.
        """
        return self._get_attribute('flowStatTableIdInputModeNumber')
    @FlowStatTableIdInputModeNumber.setter
    def FlowStatTableIdInputModeNumber(self, value):
        self._set_attribute('flowStatTableIdInputModeNumber', value)

    @property
    def FlowStatTransportDestination(self):
        """
        Returns
        -------
        - str: Specifies the Transport destination address.
        """
        return self._get_attribute('flowStatTransportDestination')
    @FlowStatTransportDestination.setter
    def FlowStatTransportDestination(self, value):
        self._set_attribute('flowStatTransportDestination', value)

    @property
    def FlowStatTransportSource(self):
        """
        Returns
        -------
        - str: Specifies the Transport source address.
        """
        return self._get_attribute('flowStatTransportSource')
    @FlowStatTransportSource.setter
    def FlowStatTransportSource(self, value):
        self._set_attribute('flowStatTransportSource', value)

    @property
    def FlowStatVlanId(self):
        """
        Returns
        -------
        - str: Specifies the unique VLAN Identifier.
        """
        return self._get_attribute('flowStatVlanId')
    @FlowStatVlanId.setter
    def FlowStatVlanId(self, value):
        self._set_attribute('flowStatVlanId', value)

    @property
    def FlowStatVlanPriority(self):
        """
        Returns
        -------
        - str: Specifies the User Priority for this VLAN.
        """
        return self._get_attribute('flowStatVlanPriority')
    @FlowStatVlanPriority.setter
    def FlowStatVlanPriority(self, value):
        self._set_attribute('flowStatVlanPriority', value)

    @property
    def GroupDescriptionStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('groupDescriptionStatResponseTimeOut')
    @GroupDescriptionStatResponseTimeOut.setter
    def GroupDescriptionStatResponseTimeOut(self, value):
        self._set_attribute('groupDescriptionStatResponseTimeOut', value)

    @property
    def GroupFeatureStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out if no response is received.
        """
        return self._get_attribute('groupFeatureStatResponseTimeOut')
    @GroupFeatureStatResponseTimeOut.setter
    def GroupFeatureStatResponseTimeOut(self, value):
        self._set_attribute('groupFeatureStatResponseTimeOut', value)

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: The ID of the group used. .
        """
        return self._get_attribute('groupId')
    @GroupId.setter
    def GroupId(self, value):
        self._set_attribute('groupId', value)

    @property
    def GroupIdType(self):
        """
        Returns
        -------
        - str(ofpgAll | ofpgAny | manual): NOT DEFINED
        """
        return self._get_attribute('groupIdType')
    @GroupIdType.setter
    def GroupIdType(self, value):
        self._set_attribute('groupIdType', value)

    @property
    def GroupStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out if no response is received.
        """
        return self._get_attribute('groupStatResponseTimeOut')
    @GroupStatResponseTimeOut.setter
    def GroupStatResponseTimeOut(self, value):
        self._set_attribute('groupStatResponseTimeOut', value)

    @property
    def IsAsyncConfStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Queue Statistics is received.
        """
        return self._get_attribute('isAsyncConfStatLearnedInformationRefreshed')

    @property
    def IsDescriptionStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Description Statistics is received.
        """
        return self._get_attribute('isDescriptionStatLearnedInformationRefreshed')

    @property
    def IsFlowAggregatedStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Flow Aggregated Statistics is received.
        """
        return self._get_attribute('isFlowAggregatedStatLearnedInformationRefreshed')

    @property
    def IsFlowStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Flow Statistics is received.
        """
        return self._get_attribute('isFlowStatLearnedInformationRefreshed')

    @property
    def IsGroupDescriptionStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('isGroupDescriptionStatLearnedInformationRefreshed')

    @property
    def IsGroupFeatureStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('isGroupFeatureStatLearnedInformationRefreshed')

    @property
    def IsGroupStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('isGroupStatLearnedInformationRefreshed')

    @property
    def IsOfChannelLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the OF Channels is received.
        """
        return self._get_attribute('isOfChannelLearnedInformationRefreshed')

    @property
    def IsPortFeaturesLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: Checks if the learned information for the port feature Learned Information is refreshed.
        """
        return self._get_attribute('isPortFeaturesLearnedInformationRefreshed')

    @property
    def IsPortStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Port Statistics is received.
        """
        return self._get_attribute('isPortStatLearnedInformationRefreshed')

    @property
    def IsQueueConfigLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the reply for the queue config request is received.
        """
        return self._get_attribute('isQueueConfigLearnedInformationRefreshed')

    @property
    def IsQueueStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Queue Statistics is received.
        """
        return self._get_attribute('isQueueStatLearnedInformationRefreshed')

    @property
    def IsTableStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Table Statistics is received.
        """
        return self._get_attribute('isTableStatLearnedInformationRefreshed')

    @property
    def IsVendorStatLearnedInformationRefreshed(self):
        """
        Returns
        -------
        - bool: If true, it denotes that the Learned Info for the Vendor Statistics is received
        """
        return self._get_attribute('isVendorStatLearnedInformationRefreshed')

    @property
    def PacketOutAuxiliaryId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('packetOutAuxiliaryId')
    @PacketOutAuxiliaryId.setter
    def PacketOutAuxiliaryId(self, value):
        self._set_attribute('packetOutAuxiliaryId', value)

    @property
    def PacketOutBufferId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('packetOutBufferId')
    @PacketOutBufferId.setter
    def PacketOutBufferId(self, value):
        self._set_attribute('packetOutBufferId', value)

    @property
    def PacketOutBufferIdInputMode(self):
        """
        Returns
        -------
        - str(opfNoBuffer | manual): NOT DEFINED
        """
        return self._get_attribute('packetOutBufferIdInputMode')
    @PacketOutBufferIdInputMode.setter
    def PacketOutBufferIdInputMode(self, value):
        self._set_attribute('packetOutBufferIdInputMode', value)

    @property
    def PacketOutData(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('packetOutData')
    @PacketOutData.setter
    def PacketOutData(self, value):
        self._set_attribute('packetOutData', value)

    @property
    def PacketOutDataLength(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('packetOutDataLength')
    @PacketOutDataLength.setter
    def PacketOutDataLength(self, value):
        self._set_attribute('packetOutDataLength', value)

    @property
    def PacketOutInPortInputMode(self):
        """
        Returns
        -------
        - str(ofppController | ofppLocal | manual): NOT DEFINED
        """
        return self._get_attribute('packetOutInPortInputMode')
    @PacketOutInPortInputMode.setter
    def PacketOutInPortInputMode(self, value):
        self._set_attribute('packetOutInPortInputMode', value)

    @property
    def PacketOutInPortNumber(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('packetOutInPortNumber')
    @PacketOutInPortNumber.setter
    def PacketOutInPortNumber(self, value):
        self._set_attribute('packetOutInPortNumber', value)

    @property
    def PortFeaturesResponseTimeOut(self):
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out if no response is received.
        """
        return self._get_attribute('portFeaturesResponseTimeOut')
    @PortFeaturesResponseTimeOut.setter
    def PortFeaturesResponseTimeOut(self, value):
        self._set_attribute('portFeaturesResponseTimeOut', value)

    @property
    def PortNumber(self):
        """
        Returns
        -------
        - number: Specifies the port number.
        """
        return self._get_attribute('portNumber')
    @PortNumber.setter
    def PortNumber(self, value):
        self._set_attribute('portNumber', value)

    @property
    def PortNumberInputMode(self):
        """
        Returns
        -------
        - str(ofppNone | custom): Specifies the input mode for the Port number.
        """
        return self._get_attribute('portNumberInputMode')
    @PortNumberInputMode.setter
    def PortNumberInputMode(self, value):
        self._set_attribute('portNumberInputMode', value)

    @property
    def PortStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no port statistics response is received.
        """
        return self._get_attribute('portStatResponseTimeOut')
    @PortStatResponseTimeOut.setter
    def PortStatResponseTimeOut(self, value):
        self._set_attribute('portStatResponseTimeOut', value)

    @property
    def QueueConfigPortNumber(self):
        """
        Returns
        -------
        - number: Indicates the Port for which the queue config request is sought.
        """
        return self._get_attribute('queueConfigPortNumber')
    @QueueConfigPortNumber.setter
    def QueueConfigPortNumber(self, value):
        self._set_attribute('queueConfigPortNumber', value)

    @property
    def QueueConfigResponseTimeOut(self):
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no queue config response is received.
        """
        return self._get_attribute('queueConfigResponseTimeOut')
    @QueueConfigResponseTimeOut.setter
    def QueueConfigResponseTimeOut(self, value):
        self._set_attribute('queueConfigResponseTimeOut', value)

    @property
    def QueueId(self):
        """
        Returns
        -------
        - number: Indicates the queue ID for which queue statistics is being sought.
        """
        return self._get_attribute('queueId')
    @QueueId.setter
    def QueueId(self, value):
        self._set_attribute('queueId', value)

    @property
    def QueueIdInputMode(self):
        """
        Returns
        -------
        - str(ofpqAll | custom): Request queue statistics for the queues belonging to the specified ports.
        """
        return self._get_attribute('queueIdInputMode')
    @QueueIdInputMode.setter
    def QueueIdInputMode(self, value):
        self._set_attribute('queueIdInputMode', value)

    @property
    def QueueStatPortNumber(self):
        """
        Returns
        -------
        - number: Specifies the port number for which queue statistics is sought.
        """
        return self._get_attribute('queueStatPortNumber')
    @QueueStatPortNumber.setter
    def QueueStatPortNumber(self, value):
        self._set_attribute('queueStatPortNumber', value)

    @property
    def QueueStatPortNumberInputMode(self):
        """
        Returns
        -------
        - str(ofppAll | custom): Indicates the ports for which queue statistics is sought.
        """
        return self._get_attribute('queueStatPortNumberInputMode')
    @QueueStatPortNumberInputMode.setter
    def QueueStatPortNumberInputMode(self, value):
        self._set_attribute('queueStatPortNumberInputMode', value)

    @property
    def QueueStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no queue statistics response is received.
        """
        return self._get_attribute('queueStatResponseTimeOut')
    @QueueStatResponseTimeOut.setter
    def QueueStatResponseTimeOut(self, value):
        self._set_attribute('queueStatResponseTimeOut', value)

    @property
    def RoleRequestGenerationId(self):
        """
        Returns
        -------
        - str: The generation ID number.
        """
        return self._get_attribute('roleRequestGenerationId')
    @RoleRequestGenerationId.setter
    def RoleRequestGenerationId(self, value):
        self._set_attribute('roleRequestGenerationId', value)

    @property
    def RoleRequestType(self):
        """
        Returns
        -------
        - str(equal | master | slave | noChange): Select the type of role for the controller.
        """
        return self._get_attribute('roleRequestType')
    @RoleRequestType.setter
    def RoleRequestType(self, value):
        self._set_attribute('roleRequestType', value)

    @property
    def SwitchConfigDropFragments(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('switchConfigDropFragments')
    @SwitchConfigDropFragments.setter
    def SwitchConfigDropFragments(self, value):
        self._set_attribute('switchConfigDropFragments', value)

    @property
    def SwitchConfigMissSendLength(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('switchConfigMissSendLength')
    @SwitchConfigMissSendLength.setter
    def SwitchConfigMissSendLength(self, value):
        self._set_attribute('switchConfigMissSendLength', value)

    @property
    def SwitchConfigReassembleFragments(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('switchConfigReassembleFragments')
    @SwitchConfigReassembleFragments.setter
    def SwitchConfigReassembleFragments(self, value):
        self._set_attribute('switchConfigReassembleFragments', value)

    @property
    def SwitchConfigResponseTimeOut(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('switchConfigResponseTimeOut')
    @SwitchConfigResponseTimeOut.setter
    def SwitchConfigResponseTimeOut(self, value):
        self._set_attribute('switchConfigResponseTimeOut', value)

    @property
    def TableFeatureConfig(self):
        """
        Returns
        -------
        - number: The bitmap of OFPTC_* values.
        """
        return self._get_attribute('tableFeatureConfig')
    @TableFeatureConfig.setter
    def TableFeatureConfig(self, value):
        self._set_attribute('tableFeatureConfig', value)

    @property
    def TableFeatureMaxEntries(self):
        """
        Returns
        -------
        - number: The maximum number of entries supported.
        """
        return self._get_attribute('tableFeatureMaxEntries')
    @TableFeatureMaxEntries.setter
    def TableFeatureMaxEntries(self, value):
        self._set_attribute('tableFeatureMaxEntries', value)

    @property
    def TableFeatureMetadataMatch(self):
        """
        Returns
        -------
        - str: The bits of metadata which the table can match.
        """
        return self._get_attribute('tableFeatureMetadataMatch')
    @TableFeatureMetadataMatch.setter
    def TableFeatureMetadataMatch(self, value):
        self._set_attribute('tableFeatureMetadataMatch', value)

    @property
    def TableFeatureMetadataWrite(self):
        """
        Returns
        -------
        - str: MetaData Write The bits of metadata which the table can write.
        """
        return self._get_attribute('tableFeatureMetadataWrite')
    @TableFeatureMetadataWrite.setter
    def TableFeatureMetadataWrite(self, value):
        self._set_attribute('tableFeatureMetadataWrite', value)

    @property
    def TableFeatureName(self):
        """
        Returns
        -------
        - str: The table name.
        """
        return self._get_attribute('tableFeatureName')
    @TableFeatureName.setter
    def TableFeatureName(self, value):
        self._set_attribute('tableFeatureName', value)

    @property
    def TableFeatureResponseTimeOut(self):
        """
        Returns
        -------
        - number: The time in milliseconds after which the trigger request times out if no response is received.
        """
        return self._get_attribute('tableFeatureResponseTimeOut')
    @TableFeatureResponseTimeOut.setter
    def TableFeatureResponseTimeOut(self, value):
        self._set_attribute('tableFeatureResponseTimeOut', value)

    @property
    def TableFeatureTableId(self):
        """
        Returns
        -------
        - number: The table identifier.
        """
        return self._get_attribute('tableFeatureTableId')
    @TableFeatureTableId.setter
    def TableFeatureTableId(self, value):
        self._set_attribute('tableFeatureTableId', value)

    @property
    def TableStatResponseTimeOut(self):
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no table statistics response is received.
        """
        return self._get_attribute('tableStatResponseTimeOut')
    @TableStatResponseTimeOut.setter
    def TableStatResponseTimeOut(self, value):
        self._set_attribute('tableStatResponseTimeOut', value)

    @property
    def TriggeredVendorMessage(self):
        """
        Returns
        -------
        - str: Indicates the vendor data of the vendor message trigger.
        """
        return self._get_attribute('triggeredVendorMessage')
    @TriggeredVendorMessage.setter
    def TriggeredVendorMessage(self, value):
        self._set_attribute('triggeredVendorMessage', value)

    @property
    def TriggeredVendorMessageId(self):
        """
        Returns
        -------
        - number: Indicates the ID of the vendor for which vendor message is triggered.
        """
        return self._get_attribute('triggeredVendorMessageId')
    @TriggeredVendorMessageId.setter
    def TriggeredVendorMessageId(self, value):
        self._set_attribute('triggeredVendorMessageId', value)

    @property
    def TriggeredVendorMessageLength(self):
        """
        Returns
        -------
        - number: Indicates the length of vendor data of the vendor message trigger.
        """
        return self._get_attribute('triggeredVendorMessageLength')
    @TriggeredVendorMessageLength.setter
    def TriggeredVendorMessageLength(self, value):
        self._set_attribute('triggeredVendorMessageLength', value)

    @property
    def VendorId(self):
        """
        Returns
        -------
        - number: Specifies the unique Vendor identifier.
        """
        return self._get_attribute('vendorId')
    @VendorId.setter
    def VendorId(self, value):
        self._set_attribute('vendorId', value)

    @property
    def VendorMessage(self):
        """
        Returns
        -------
        - str: Speciifes the vendor message value.
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
        - number: Specifies the length of the message being transmitted.
        """
        return self._get_attribute('vendorMessageLength')
    @VendorMessageLength.setter
    def VendorMessageLength(self, value):
        self._set_attribute('vendorMessageLength', value)

    @property
    def VendorStateResponseTimeOut(self):
        """
        Returns
        -------
        - number: Indicates the duration in milliseconds after which the trigger request times out if no vendor statistics response is received.
        """
        return self._get_attribute('vendorStateResponseTimeOut')
    @VendorStateResponseTimeOut.setter
    def VendorStateResponseTimeOut(self, value):
        self._set_attribute('vendorStateResponseTimeOut', value)

    def update(self, AsyncConfStatResponseTimeOut=None, DescriptionStatResponseTimeOut=None, EnableAsyncConfMasterFlowRemovedFlowDelete=None, EnableAsyncConfMasterFlowRemovedGroupDelete=None, EnableAsyncConfMasterFlowRemovedHardTimeOut=None, EnableAsyncConfMasterFlowRemovedIdleTimeOut=None, EnableAsyncConfMasterPacketInActionOutputToController=None, EnableAsyncConfMasterPacketInInvalidTtl=None, EnableAsyncConfMasterPacketInNoMatching=None, EnableAsyncConfMasterPortStatusAdd=None, EnableAsyncConfMasterPortStatusDelete=None, EnableAsyncConfMasterPortStatusModify=None, EnableAsyncConfSlaveFlowRemovedFlowDelete=None, EnableAsyncConfSlaveFlowRemovedGroupDelete=None, EnableAsyncConfSlaveFlowRemovedHardTimeOut=None, EnableAsyncConfSlaveFlowRemovedIdleTimeOut=None, EnableAsyncConfSlavePacketInActionOutputToController=None, EnableAsyncConfSlavePacketInInvalidTtl=None, EnableAsyncConfSlavePacketInNoMatching=None, EnableAsyncConfSlavePortStatusAdd=None, EnableAsyncConfSlavePortStatusDelete=None, EnableAsyncConfSlavePortStatusModify=None, EnableFlowAggregatedStatMatchCapability=None, EnableFlowStatMatchCapability=None, EnableGroupStatMatchCapability=None, EnablePortStatMatchCapability=None, EnableQueueStatMatchCapability=None, EnableSendTableFeaturesTrigger=None, EnableSendTriggerPortFeaturesLearnedInformation=None, EnableSendTriggeredAsyncConfStatLearnedInformation=None, EnableSendTriggeredBarrierRequestMessage=None, EnableSendTriggeredDescriptionStatLearnedInformation=None, EnableSendTriggeredFlowAggregatedStatLearnedInformation=None, EnableSendTriggeredFlowStatLearnedInformation=None, EnableSendTriggeredGroupDescriptionStatLearnedInformation=None, EnableSendTriggeredGroupFeatureStatLearnedInformation=None, EnableSendTriggeredGroupStatLearnedInformation=None, EnableSendTriggeredPacketOutMessage=None, EnableSendTriggeredPortModificationMessage=None, EnableSendTriggeredPortStatLearnedInformation=None, EnableSendTriggeredQueueConfigLearnedInformation=None, EnableSendTriggeredQueueStatLearnedInformation=None, EnableSendTriggeredRoleRequestMessage=None, EnableSendTriggeredSwitchConfigLearnedInformation=None, EnableSendTriggeredTableStatLearnedInformation=None, EnableSendTriggeredVendorStatLearnedInformation=None, EnableSetAsyncConfig=None, EnableSetSwitchConfig=None, EnableSetTableFeatures=None, EnableTableStatMatchCapability=None, EnableTriggeredVendorMessage=None, FlowAggregatedStatEthernetDestination=None, FlowAggregatedStatEthernetSource=None, FlowAggregatedStatEthernetType=None, FlowAggregatedStatInPort=None, FlowAggregatedStatIpDscp=None, FlowAggregatedStatIpProtocol=None, FlowAggregatedStatIpv4Destination=None, FlowAggregatedStatIpv4Source=None, FlowAggregatedStatOutPortInputMode=None, FlowAggregatedStatResponseTimeOut=None, FlowAggregatedStatTableIdInputMode=None, FlowAggregatedStatTableIdInputModeNumber=None, FlowAggregatedStatTransportDestination=None, FlowAggregatedStatTransportSource=None, FlowAggregatedStatVlanId=None, FlowAggregatedStatVlanPriority=None, FlowStatEthernetDestination=None, FlowStatEthernetSource=None, FlowStatEthernetType=None, FlowStatInPort=None, FlowStatIpDscp=None, FlowStatIpProtocol=None, FlowStatIpv4Destination=None, FlowStatIpv4Source=None, FlowStatOutPortInputMode=None, FlowStatResponseTimeOut=None, FlowStatTableIdInputMode=None, FlowStatTableIdInputModeNumber=None, FlowStatTransportDestination=None, FlowStatTransportSource=None, FlowStatVlanId=None, FlowStatVlanPriority=None, GroupDescriptionStatResponseTimeOut=None, GroupFeatureStatResponseTimeOut=None, GroupId=None, GroupIdType=None, GroupStatResponseTimeOut=None, PacketOutAuxiliaryId=None, PacketOutBufferId=None, PacketOutBufferIdInputMode=None, PacketOutData=None, PacketOutDataLength=None, PacketOutInPortInputMode=None, PacketOutInPortNumber=None, PortFeaturesResponseTimeOut=None, PortNumber=None, PortNumberInputMode=None, PortStatResponseTimeOut=None, QueueConfigPortNumber=None, QueueConfigResponseTimeOut=None, QueueId=None, QueueIdInputMode=None, QueueStatPortNumber=None, QueueStatPortNumberInputMode=None, QueueStatResponseTimeOut=None, RoleRequestGenerationId=None, RoleRequestType=None, SwitchConfigDropFragments=None, SwitchConfigMissSendLength=None, SwitchConfigReassembleFragments=None, SwitchConfigResponseTimeOut=None, TableFeatureConfig=None, TableFeatureMaxEntries=None, TableFeatureMetadataMatch=None, TableFeatureMetadataWrite=None, TableFeatureName=None, TableFeatureResponseTimeOut=None, TableFeatureTableId=None, TableStatResponseTimeOut=None, TriggeredVendorMessage=None, TriggeredVendorMessageId=None, TriggeredVendorMessageLength=None, VendorId=None, VendorMessage=None, VendorMessageLength=None, VendorStateResponseTimeOut=None):
        """Updates learnedInformation resource on the server.

        Args
        ----
        - AsyncConfStatResponseTimeOut (number): NOT DEFINED
        - DescriptionStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no description statistics response is received.
        - EnableAsyncConfMasterFlowRemovedFlowDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Flow Delete is received.
        - EnableAsyncConfMasterFlowRemovedGroupDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Group Delete is received.
        - EnableAsyncConfMasterFlowRemovedHardTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Hard Time Out is received.
        - EnableAsyncConfMasterFlowRemovedIdleTimeOut (bool): NOT DEFINED
        - EnableAsyncConfMasterPacketInActionOutputToController (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Action Output To Controller is received.
        - EnableAsyncConfMasterPacketInInvalidTtl (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Invalid Ttl is received.
        - EnableAsyncConfMasterPacketInNoMatching (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In No Matching is received.
        - EnableAsyncConfMasterPortStatusAdd (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Add is received.
        - EnableAsyncConfMasterPortStatusDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Delete is received.
        - EnableAsyncConfMasterPortStatusModify (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
        - EnableAsyncConfSlaveFlowRemovedFlowDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Flow Delete is received.
        - EnableAsyncConfSlaveFlowRemovedGroupDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Group Delete is received.
        - EnableAsyncConfSlaveFlowRemovedHardTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Hard Time Out is received.
        - EnableAsyncConfSlaveFlowRemovedIdleTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Idle Time Out is received.
        - EnableAsyncConfSlavePacketInActionOutputToController (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Action Output To Controller is received.
        - EnableAsyncConfSlavePacketInInvalidTtl (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Invalid Ttl is received.
        - EnableAsyncConfSlavePacketInNoMatching (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In No Matching is received.
        - EnableAsyncConfSlavePortStatusAdd (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Add is received.
        - EnableAsyncConfSlavePortStatusDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
        - EnableAsyncConfSlavePortStatusModify (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Modify is received.
        - EnableFlowAggregatedStatMatchCapability (bool): Checks to see if the switch has the capability to publish Flow Aggregated Statistics
        - EnableFlowStatMatchCapability (bool): Checks to see if the switch has the capability to publish Flow Statistics
        - EnableGroupStatMatchCapability (bool): If enabled,it denotes that the enable Group Statistics Match Capability is received.
        - EnablePortStatMatchCapability (bool): Checks to see if the switch has the capability to publish Port Statistics
        - EnableQueueStatMatchCapability (bool): If true, the switch has the capability to publish Queue Statistics.
        - EnableSendTableFeaturesTrigger (bool): If enabled,it denotes that the enable Send Table Features Trigger is received.
        - EnableSendTriggerPortFeaturesLearnedInformation (bool): Enables Trigger for port features learned information.
        - EnableSendTriggeredAsyncConfStatLearnedInformation (bool): If enabled,it denotes that the Triggered Asynchronous Configuration Statistics Learned Information is received.
        - EnableSendTriggeredBarrierRequestMessage (bool): If true, enables trigger for barrier request message
        - EnableSendTriggeredDescriptionStatLearnedInformation (bool): If true, the description statistic trigger configuration parameters are available.
        - EnableSendTriggeredFlowAggregatedStatLearnedInformation (bool): If true, the flow aggregated statistic trigger configuration parameters are available.
        - EnableSendTriggeredFlowStatLearnedInformation (bool): If true, the flow statistic trigger configuration parameters are available.
        - EnableSendTriggeredGroupDescriptionStatLearnedInformation (bool): If enabled,it denotes that the enable Send Triggered Group Description Statistics Learned Information is received.
        - EnableSendTriggeredGroupFeatureStatLearnedInformation (bool): If enabled,it denotes that the enable Send Triggered Group Feature Statistics Learned Information is received.
        - EnableSendTriggeredGroupStatLearnedInformation (bool): If enabled,it denotes that the Send Triggered Group Statistics Learned Information is received.
        - EnableSendTriggeredPacketOutMessage (bool): If enabled,it denotes that the enable Send Triggered Packet Out Message is received.
        - EnableSendTriggeredPortModificationMessage (bool): If enabled,it denotes that the enable Send Triggered Port Modification Message is received.
        - EnableSendTriggeredPortStatLearnedInformation (bool): If true, the port statistic trigger configuration parameters are available.
        - EnableSendTriggeredQueueConfigLearnedInformation (bool): If true, the queue config trigger configuration parameters are available.
        - EnableSendTriggeredQueueStatLearnedInformation (bool): If true, the queue statistic trigger configuration parameters are available.
        - EnableSendTriggeredRoleRequestMessage (bool): If enabled,it denotes that the Triggered Role Request Message is received.
        - EnableSendTriggeredSwitchConfigLearnedInformation (bool): If enabled,it denotes that the enable Switch Configuration Learned Information is received.
        - EnableSendTriggeredTableStatLearnedInformation (bool): If true, the table statistic trigger configuration parameters are available.
        - EnableSendTriggeredVendorStatLearnedInformation (bool): If true, the vendor statistic trigger configuration parameters are available.
        - EnableSetAsyncConfig (bool): If enabled,it denotes that the Set Asynchronous Configuration is received.
        - EnableSetSwitchConfig (bool): If enabled,it denotes that the enable Set Switch Configuration is received.
        - EnableSetTableFeatures (bool): NOT DEFINED
        - EnableTableStatMatchCapability (bool): If true, the switch has the capability to publish Table Statistics.
        - EnableTriggeredVendorMessage (bool): If true, the vendor message trigger configuration parameters are available.
        - FlowAggregatedStatEthernetDestination (str): Signifies the ethernet destination address.
        - FlowAggregatedStatEthernetSource (str): Signifies the ethernet source address.
        - FlowAggregatedStatEthernetType (str): Signifies the type of Ethernet used.
        - FlowAggregatedStatInPort (str): Signifies the input port used.
        - FlowAggregatedStatIpDscp (str): Signifies the IP DSCP value for advertising.
        - FlowAggregatedStatIpProtocol (str): Signifies the IP protocol used.
        - FlowAggregatedStatIpv4Destination (str): Signifies the IPv4 destination address.
        - FlowAggregatedStatIpv4Source (str): Signifies the IPv4 source address.
        - FlowAggregatedStatOutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom)): Signifies the identifier output mode of the aggregated flow statistics table.
        - FlowAggregatedStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no flow aggregated statistics response is received.
        - FlowAggregatedStatTableIdInputMode (str(allTables | emergency | custom)): Signifies the identifier input mode of the flow aggregated statistics table.
        - FlowAggregatedStatTableIdInputModeNumber (number): Signifies the identifier input mode of the flow aggregated statistics table.
        - FlowAggregatedStatTransportDestination (str): Signifies the Transport destination address.
        - FlowAggregatedStatTransportSource (str): Signifies the Transport source address.
        - FlowAggregatedStatVlanId (str): Signifies the unique VLAN Identifier.
        - FlowAggregatedStatVlanPriority (str): Signifies the User Priority for this VLAN.
        - FlowStatEthernetDestination (str): Specifies the Ethernet destination address.
        - FlowStatEthernetSource (str): Specifies the Ethernet source address.
        - FlowStatEthernetType (str): Specifies the type of Ethernet used.
        - FlowStatInPort (str): Specifies the input port used.
        - FlowStatIpDscp (str): Specifies the IP DSCP value for advertising.
        - FlowStatIpProtocol (str): Specifies the IP protocol used.
        - FlowStatIpv4Destination (str): Specifies the The IPv4 destination address.
        - FlowStatIpv4Source (str): Specifies the The IPv4 source address.
        - FlowStatOutPortInputMode (str(ofppInPort | ofppNormal | ofppFlood | ofppAll | ofppController | ofppLocal | ofppNone | custom)): Specifies the output mode of the Table identifier.
        - FlowStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no response is received.
        - FlowStatTableIdInputMode (str(allTables | emergency | custom)): Specifies the input mode of the Table identifier.
        - FlowStatTableIdInputModeNumber (number): Signifies the identifier input mode of the flow statistics table.
        - FlowStatTransportDestination (str): Specifies the Transport destination address.
        - FlowStatTransportSource (str): Specifies the Transport source address.
        - FlowStatVlanId (str): Specifies the unique VLAN Identifier.
        - FlowStatVlanPriority (str): Specifies the User Priority for this VLAN.
        - GroupDescriptionStatResponseTimeOut (number): NOT DEFINED
        - GroupFeatureStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - GroupId (number): The ID of the group used. .
        - GroupIdType (str(ofpgAll | ofpgAny | manual)): NOT DEFINED
        - GroupStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - PacketOutAuxiliaryId (number): NOT DEFINED
        - PacketOutBufferId (number): NOT DEFINED
        - PacketOutBufferIdInputMode (str(opfNoBuffer | manual)): NOT DEFINED
        - PacketOutData (str): NOT DEFINED
        - PacketOutDataLength (number): NOT DEFINED
        - PacketOutInPortInputMode (str(ofppController | ofppLocal | manual)): NOT DEFINED
        - PacketOutInPortNumber (number): NOT DEFINED
        - PortFeaturesResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - PortNumber (number): Specifies the port number.
        - PortNumberInputMode (str(ofppNone | custom)): Specifies the input mode for the Port number.
        - PortStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no port statistics response is received.
        - QueueConfigPortNumber (number): Indicates the Port for which the queue config request is sought.
        - QueueConfigResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no queue config response is received.
        - QueueId (number): Indicates the queue ID for which queue statistics is being sought.
        - QueueIdInputMode (str(ofpqAll | custom)): Request queue statistics for the queues belonging to the specified ports.
        - QueueStatPortNumber (number): Specifies the port number for which queue statistics is sought.
        - QueueStatPortNumberInputMode (str(ofppAll | custom)): Indicates the ports for which queue statistics is sought.
        - QueueStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no queue statistics response is received.
        - RoleRequestGenerationId (str): The generation ID number.
        - RoleRequestType (str(equal | master | slave | noChange)): Select the type of role for the controller.
        - SwitchConfigDropFragments (bool): NOT DEFINED
        - SwitchConfigMissSendLength (number): NOT DEFINED
        - SwitchConfigReassembleFragments (bool): NOT DEFINED
        - SwitchConfigResponseTimeOut (number): NOT DEFINED
        - TableFeatureConfig (number): The bitmap of OFPTC_* values.
        - TableFeatureMaxEntries (number): The maximum number of entries supported.
        - TableFeatureMetadataMatch (str): The bits of metadata which the table can match.
        - TableFeatureMetadataWrite (str): MetaData Write The bits of metadata which the table can write.
        - TableFeatureName (str): The table name.
        - TableFeatureResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
        - TableFeatureTableId (number): The table identifier.
        - TableStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no table statistics response is received.
        - TriggeredVendorMessage (str): Indicates the vendor data of the vendor message trigger.
        - TriggeredVendorMessageId (number): Indicates the ID of the vendor for which vendor message is triggered.
        - TriggeredVendorMessageLength (number): Indicates the length of vendor data of the vendor message trigger.
        - VendorId (number): Specifies the unique Vendor identifier.
        - VendorMessage (str): Speciifes the vendor message value.
        - VendorMessageLength (number): Specifies the length of the message being transmitted.
        - VendorStateResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no vendor statistics response is received.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def ClearRecordsForTrigger(self):
        """Executes the clearRecordsForTrigger operation on the server.

        This describes the record cleared for trigger settings.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('clearRecordsForTrigger', payload=payload, response_object=None)

    def RefreshLearnedInformation(self):
        """Executes the refreshLearnedInformation operation on the server.

        This describes the learned information is refreshed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInformation', payload=payload, response_object=None)

    def Trigger(self):
        """Executes the trigger operation on the server.

        This describes the learned info trigger settings.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('trigger', payload=payload, response_object=None)
