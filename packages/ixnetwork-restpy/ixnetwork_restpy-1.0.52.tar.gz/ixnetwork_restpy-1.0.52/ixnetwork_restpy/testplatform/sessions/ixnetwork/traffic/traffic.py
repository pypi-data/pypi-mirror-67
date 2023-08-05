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


class Traffic(Base):
    """The traffic object allows the user to create millions of traffic flows for validating emulated networks and hosts. This is the top-level object for traffic configuration.
    The Traffic class encapsulates a required traffic resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'traffic'

    def __init__(self, parent):
        super(Traffic, self).__init__(parent)

    @property
    def DynamicFrameSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicframesize.dynamicframesize.DynamicFrameSize): An instance of the DynamicFrameSize class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicframesize.dynamicframesize import DynamicFrameSize
        return DynamicFrameSize(self)

    @property
    def DynamicRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicrate.dynamicrate.DynamicRate): An instance of the DynamicRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.dynamicrate.dynamicrate import DynamicRate
        return DynamicRate(self)

    @property
    def EgressOnlyTracking(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.egressonlytracking.egressonlytracking.EgressOnlyTracking): An instance of the EgressOnlyTracking class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.egressonlytracking.egressonlytracking import EgressOnlyTracking
        return EgressOnlyTracking(self)

    @property
    def ProtocolTemplate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.protocoltemplate.protocoltemplate.ProtocolTemplate): An instance of the ProtocolTemplate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.protocoltemplate.protocoltemplate import ProtocolTemplate
        return ProtocolTemplate(self)

    @property
    def Statistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.statistics.Statistics): An instance of the Statistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.statistics import Statistics
        return Statistics(self)._select()

    @property
    def TrafficGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficgroup.trafficgroup.TrafficGroup): An instance of the TrafficGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficgroup.trafficgroup import TrafficGroup
        return TrafficGroup(self)

    @property
    def TrafficItem(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.trafficitem.TrafficItem): An instance of the TrafficItem class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.trafficitem import TrafficItem
        return TrafficItem(self)

    @property
    def AutoCorrectL4HeaderChecksums(self):
        """
        Returns
        -------
        - bool: This is used for Multis and Xdensity as checksum is not calculated correctly when change on the fly operations are performed. When this option is enabled IxOS uses 2 bytes before CRC, that way ensuring the checksum is correct when change on the fly operations are performed.
        """
        return self._get_attribute('autoCorrectL4HeaderChecksums')
    @AutoCorrectL4HeaderChecksums.setter
    def AutoCorrectL4HeaderChecksums(self, value):
        self._set_attribute('autoCorrectL4HeaderChecksums', value)

    @property
    def CycleOffsetForScheduledStart(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute('cycleOffsetForScheduledStart')
    @CycleOffsetForScheduledStart.setter
    def CycleOffsetForScheduledStart(self, value):
        self._set_attribute('cycleOffsetForScheduledStart', value)

    @property
    def CycleOffsetUnitForScheduledStart(self):
        """
        Returns
        -------
        - str(microseconds | milliseconds | nanoseconds | seconds): 
        """
        return self._get_attribute('cycleOffsetUnitForScheduledStart')
    @CycleOffsetUnitForScheduledStart.setter
    def CycleOffsetUnitForScheduledStart(self, value):
        self._set_attribute('cycleOffsetUnitForScheduledStart', value)

    @property
    def CycleTimeForScheduledStart(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute('cycleTimeForScheduledStart')
    @CycleTimeForScheduledStart.setter
    def CycleTimeForScheduledStart(self, value):
        self._set_attribute('cycleTimeForScheduledStart', value)

    @property
    def CycleTimeUnitForScheduledStart(self):
        """
        Returns
        -------
        - str(microseconds | milliseconds | nanoseconds | seconds): 
        """
        return self._get_attribute('cycleTimeUnitForScheduledStart')
    @CycleTimeUnitForScheduledStart.setter
    def CycleTimeUnitForScheduledStart(self, value):
        self._set_attribute('cycleTimeUnitForScheduledStart', value)

    @property
    def DataPlaneJitterWindow(self):
        """DEPRECATED 
        Returns
        -------
        - str(0 | 10485760 | 1310720 | 167772160 | 20971520 | 2621440 | 335544320 | 41943040 | 5242880 | 671088640 | 83886080): Indicates the number of packets received during a time interval. This is used forcalculating the rate on the recieve side.
        """
        return self._get_attribute('dataPlaneJitterWindow')
    @DataPlaneJitterWindow.setter
    def DataPlaneJitterWindow(self, value):
        self._set_attribute('dataPlaneJitterWindow', value)

    @property
    def DelayTimeForScheduledStart(self):
        """
        Returns
        -------
        - number: Delay Time For Scheduled Start Transmit in seconds
        """
        return self._get_attribute('delayTimeForScheduledStart')
    @DelayTimeForScheduledStart.setter
    def DelayTimeForScheduledStart(self, value):
        self._set_attribute('delayTimeForScheduledStart', value)

    @property
    def DestMacRetryCount(self):
        """
        Returns
        -------
        - number: The number of time to attempt to obtain the destination MAC address.
        """
        return self._get_attribute('destMacRetryCount')
    @DestMacRetryCount.setter
    def DestMacRetryCount(self, value):
        self._set_attribute('destMacRetryCount', value)

    @property
    def DestMacRetryDelay(self):
        """
        Returns
        -------
        - number: The number of seconds to wait between attempts to obtain the destination MAC address.
        """
        return self._get_attribute('destMacRetryDelay')
    @DestMacRetryDelay.setter
    def DestMacRetryDelay(self, value):
        self._set_attribute('destMacRetryDelay', value)

    @property
    def DetectMisdirectedOnAllPorts(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('detectMisdirectedOnAllPorts')
    @DetectMisdirectedOnAllPorts.setter
    def DetectMisdirectedOnAllPorts(self, value):
        self._set_attribute('detectMisdirectedOnAllPorts', value)

    @property
    def DisablePortLevelMisdirected(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('disablePortLevelMisdirected')
    @DisablePortLevelMisdirected.setter
    def DisablePortLevelMisdirected(self, value):
        self._set_attribute('disablePortLevelMisdirected', value)

    @property
    def DisplayMplsCurrentLabelValue(self):
        """
        Returns
        -------
        - bool: Displays current label value for LSP Endpoints.
        """
        return self._get_attribute('displayMplsCurrentLabelValue')
    @DisplayMplsCurrentLabelValue.setter
    def DisplayMplsCurrentLabelValue(self, value):
        self._set_attribute('displayMplsCurrentLabelValue', value)

    @property
    def ElapsedTransmitTime(self):
        """
        Returns
        -------
        - number: Specifies the amount of time traffic is running in milliseconds. If the traffic state is unapplied or errored then the transmit time will be 0.
        """
        return self._get_attribute('elapsedTransmitTime')

    @property
    def EnableDataIntegrityCheck(self):
        """
        Returns
        -------
        - bool: If true, enable data integrity check.
        """
        return self._get_attribute('enableDataIntegrityCheck')
    @EnableDataIntegrityCheck.setter
    def EnableDataIntegrityCheck(self, value):
        self._set_attribute('enableDataIntegrityCheck', value)

    @property
    def EnableDestMacRetry(self):
        """
        Returns
        -------
        - bool: If true, enables the destination MAC address retry function.
        """
        return self._get_attribute('enableDestMacRetry')
    @EnableDestMacRetry.setter
    def EnableDestMacRetry(self, value):
        self._set_attribute('enableDestMacRetry', value)

    @property
    def EnableEgressOnlyTracking(self):
        """
        Returns
        -------
        - bool: This flags enables/disables egress only tracking on the quick flow group. In this mode only quick flow groups are supported, user will have only PGID stats and the packets will not contain any instrumentation block.
        """
        return self._get_attribute('enableEgressOnlyTracking')
    @EnableEgressOnlyTracking.setter
    def EnableEgressOnlyTracking(self, value):
        self._set_attribute('enableEgressOnlyTracking', value)

    @property
    def EnableInstantaneousStatsSupport(self):
        """
        Returns
        -------
        - bool: If true, enables instantaneous stats support
        """
        return self._get_attribute('enableInstantaneousStatsSupport')
    @EnableInstantaneousStatsSupport.setter
    def EnableInstantaneousStatsSupport(self, value):
        self._set_attribute('enableInstantaneousStatsSupport', value)

    @property
    def EnableLagAutoRate(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('enableLagAutoRate')
    @EnableLagAutoRate.setter
    def EnableLagAutoRate(self, value):
        self._set_attribute('enableLagAutoRate', value)

    @property
    def EnableLagFlowBalancing(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('enableLagFlowBalancing')
    @EnableLagFlowBalancing.setter
    def EnableLagFlowBalancing(self, value):
        self._set_attribute('enableLagFlowBalancing', value)

    @property
    def EnableLagFlowFailoverMode(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('enableLagFlowFailoverMode')
    @EnableLagFlowFailoverMode.setter
    def EnableLagFlowFailoverMode(self, value):
        self._set_attribute('enableLagFlowFailoverMode', value)

    @property
    def EnableLagRebalanceOnPortUp(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('enableLagRebalanceOnPortUp')
    @EnableLagRebalanceOnPortUp.setter
    def EnableLagRebalanceOnPortUp(self, value):
        self._set_attribute('enableLagRebalanceOnPortUp', value)

    @property
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: If true, IxNetwork will allow the stream to use smaller packet sizes. (In the case of IPv4 and Ethernet, 64 bytes will be allowed.) This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.
        """
        return self._get_attribute('enableMinFrameSize')
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute('enableMinFrameSize', value)

    @property
    def EnableMulticastScalingFactor(self):
        """
        Returns
        -------
        - bool: If true, traffic items with the Merged Destination Ranges option selected have be to manually regenerated by the user.
        """
        return self._get_attribute('enableMulticastScalingFactor')
    @EnableMulticastScalingFactor.setter
    def EnableMulticastScalingFactor(self, value):
        self._set_attribute('enableMulticastScalingFactor', value)

    @property
    def EnableSequenceChecking(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, this field enables sequence checking. The default is false.
        """
        return self._get_attribute('enableSequenceChecking')
    @EnableSequenceChecking.setter
    def EnableSequenceChecking(self, value):
        self._set_attribute('enableSequenceChecking', value)

    @property
    def EnableStaggeredStartDelay(self):
        """
        Returns
        -------
        - bool: If checked, enables the staggered start delay function.
        """
        return self._get_attribute('enableStaggeredStartDelay')
    @EnableStaggeredStartDelay.setter
    def EnableStaggeredStartDelay(self, value):
        self._set_attribute('enableStaggeredStartDelay', value)

    @property
    def EnableStaggeredTransmit(self):
        """
        Returns
        -------
        - bool: If true, the start of transmit is staggered across ports. A 25-30 ms delay is introduced between the time one port begins transmitting and the time next port begins transmitting.
        """
        return self._get_attribute('enableStaggeredTransmit')
    @EnableStaggeredTransmit.setter
    def EnableStaggeredTransmit(self, value):
        self._set_attribute('enableStaggeredTransmit', value)

    @property
    def EnableStreamOrdering(self):
        """
        Returns
        -------
        - bool: If true, IxNetwork will allow stream ordering per RFC 2889.
        """
        return self._get_attribute('enableStreamOrdering')
    @EnableStreamOrdering.setter
    def EnableStreamOrdering(self, value):
        self._set_attribute('enableStreamOrdering', value)

    @property
    def FrameOrderingMode(self):
        """
        Returns
        -------
        - str(flowGroupSetup | none | peakLoading | RFC2889): If true, enables frame ordering.
        """
        return self._get_attribute('frameOrderingMode')
    @FrameOrderingMode.setter
    def FrameOrderingMode(self, value):
        self._set_attribute('frameOrderingMode', value)

    @property
    def GlobalStreamControl(self):
        """
        Returns
        -------
        - str(continuous | iterations): The Global Stream Control parameters.
        """
        return self._get_attribute('globalStreamControl')
    @GlobalStreamControl.setter
    def GlobalStreamControl(self, value):
        self._set_attribute('globalStreamControl', value)

    @property
    def GlobalStreamControlIterations(self):
        """
        Returns
        -------
        - number: If true, the user can specify how many times each packet stream will be transmitted.
        """
        return self._get_attribute('globalStreamControlIterations')
    @GlobalStreamControlIterations.setter
    def GlobalStreamControlIterations(self, value):
        self._set_attribute('globalStreamControlIterations', value)

    @property
    def IsApplicationTrafficRunning(self):
        """
        Returns
        -------
        - bool: If true, application traffic is running.
        """
        return self._get_attribute('isApplicationTrafficRunning')

    @property
    def IsApplyOnTheFlyRequired(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('isApplyOnTheFlyRequired')

    @property
    def IsTrafficRunning(self):
        """
        Returns
        -------
        - bool: If true, non-application traffic is running.
        """
        return self._get_attribute('isTrafficRunning')

    @property
    def LargeErrorThreshhold(self):
        """
        Returns
        -------
        - number: The user-configurable threshold value used to determine error levels for out-of-sequence, received packets.
        """
        return self._get_attribute('largeErrorThreshhold')
    @LargeErrorThreshhold.setter
    def LargeErrorThreshhold(self, value):
        self._set_attribute('largeErrorThreshhold', value)

    @property
    def LearningFrameSize(self):
        """
        Returns
        -------
        - number: Learns frame size
        """
        return self._get_attribute('learningFrameSize')
    @LearningFrameSize.setter
    def LearningFrameSize(self, value):
        self._set_attribute('learningFrameSize', value)

    @property
    def LearningFramesCount(self):
        """
        Returns
        -------
        - number: Learns frames count
        """
        return self._get_attribute('learningFramesCount')
    @LearningFramesCount.setter
    def LearningFramesCount(self, value):
        self._set_attribute('learningFramesCount', value)

    @property
    def LearningFramesRate(self):
        """
        Returns
        -------
        - number: Learns frames rate
        """
        return self._get_attribute('learningFramesRate')
    @LearningFramesRate.setter
    def LearningFramesRate(self, value):
        self._set_attribute('learningFramesRate', value)

    @property
    def MacChangeOnFly(self):
        """
        Returns
        -------
        - bool: If true, enables IxNetwork's gratuitous ARP capability. When enabled, IxNetwork listens for gratuitous ARP messages from its neighbors.
        """
        return self._get_attribute('macChangeOnFly')
    @MacChangeOnFly.setter
    def MacChangeOnFly(self, value):
        self._set_attribute('macChangeOnFly', value)

    @property
    def MaxTrafficGenerationQueries(self):
        """
        Returns
        -------
        - number: The maximum number of traffic generation queries. The default is 500.
        """
        return self._get_attribute('maxTrafficGenerationQueries')
    @MaxTrafficGenerationQueries.setter
    def MaxTrafficGenerationQueries(self, value):
        self._set_attribute('maxTrafficGenerationQueries', value)

    @property
    def MplsLabelLearningTimeout(self):
        """
        Returns
        -------
        - number: The MPLS label learning timeout in seconds. The default is 30 seconds.
        """
        return self._get_attribute('mplsLabelLearningTimeout')
    @MplsLabelLearningTimeout.setter
    def MplsLabelLearningTimeout(self, value):
        self._set_attribute('mplsLabelLearningTimeout', value)

    @property
    def PeakLoadingReplicationCount(self):
        """
        Returns
        -------
        - number: The peak loading replication count
        """
        return self._get_attribute('peakLoadingReplicationCount')
    @PeakLoadingReplicationCount.setter
    def PeakLoadingReplicationCount(self, value):
        self._set_attribute('peakLoadingReplicationCount', value)

    @property
    def PreventDataPlaneToCpu(self):
        """
        Returns
        -------
        - bool: Prevent all data plane packets from being forwarded to Port CPU (disabling this option requires Port CPU reboot)
        """
        return self._get_attribute('preventDataPlaneToCpu')
    @PreventDataPlaneToCpu.setter
    def PreventDataPlaneToCpu(self, value):
        self._set_attribute('preventDataPlaneToCpu', value)

    @property
    def RefreshLearnedInfoBeforeApply(self):
        """
        Returns
        -------
        - bool: This field refreshes the learned information from the DUT.
        """
        return self._get_attribute('refreshLearnedInfoBeforeApply')
    @RefreshLearnedInfoBeforeApply.setter
    def RefreshLearnedInfoBeforeApply(self, value):
        self._set_attribute('refreshLearnedInfoBeforeApply', value)

    @property
    def State(self):
        """
        Returns
        -------
        - str(error | locked | started | startedWaitingForStats | startedWaitingForStreams | stopped | stoppedWaitingForStats | txStopWatchExpected | unapplied): Denotes the current state of traffic.
        """
        return self._get_attribute('state')

    @property
    def UseRfc5952(self):
        """
        Returns
        -------
        - bool: Use RFC 5952 for formatting IPv6 addresses (:ffff:1.2.3.4)
        """
        return self._get_attribute('useRfc5952')
    @UseRfc5952.setter
    def UseRfc5952(self, value):
        self._set_attribute('useRfc5952', value)

    @property
    def UseScheduledStartTransmit(self):
        """
        Returns
        -------
        - bool: Use Scheduled Start Transmit
        """
        return self._get_attribute('useScheduledStartTransmit')
    @UseScheduledStartTransmit.setter
    def UseScheduledStartTransmit(self, value):
        self._set_attribute('useScheduledStartTransmit', value)

    @property
    def UseTxRxSync(self):
        """
        Returns
        -------
        - bool: If true, enables the transmit/receive port synchronization algorithm.
        """
        return self._get_attribute('useTxRxSync')
    @UseTxRxSync.setter
    def UseTxRxSync(self, value):
        self._set_attribute('useTxRxSync', value)

    @property
    def WaitTime(self):
        """
        Returns
        -------
        - number: The time (in seconds) to wait after Stop Transmit before stopping Latency Measurement.
        """
        return self._get_attribute('waitTime')
    @WaitTime.setter
    def WaitTime(self, value):
        self._set_attribute('waitTime', value)

    def update(self, AutoCorrectL4HeaderChecksums=None, CycleOffsetForScheduledStart=None, CycleOffsetUnitForScheduledStart=None, CycleTimeForScheduledStart=None, CycleTimeUnitForScheduledStart=None, DataPlaneJitterWindow=None, DelayTimeForScheduledStart=None, DestMacRetryCount=None, DestMacRetryDelay=None, DetectMisdirectedOnAllPorts=None, DisablePortLevelMisdirected=None, DisplayMplsCurrentLabelValue=None, EnableDataIntegrityCheck=None, EnableDestMacRetry=None, EnableEgressOnlyTracking=None, EnableInstantaneousStatsSupport=None, EnableLagAutoRate=None, EnableLagFlowBalancing=None, EnableLagFlowFailoverMode=None, EnableLagRebalanceOnPortUp=None, EnableMinFrameSize=None, EnableMulticastScalingFactor=None, EnableSequenceChecking=None, EnableStaggeredStartDelay=None, EnableStaggeredTransmit=None, EnableStreamOrdering=None, FrameOrderingMode=None, GlobalStreamControl=None, GlobalStreamControlIterations=None, LargeErrorThreshhold=None, LearningFrameSize=None, LearningFramesCount=None, LearningFramesRate=None, MacChangeOnFly=None, MaxTrafficGenerationQueries=None, MplsLabelLearningTimeout=None, PeakLoadingReplicationCount=None, PreventDataPlaneToCpu=None, RefreshLearnedInfoBeforeApply=None, UseRfc5952=None, UseScheduledStartTransmit=None, UseTxRxSync=None, WaitTime=None):
        """Updates traffic resource on the server.

        Args
        ----
        - AutoCorrectL4HeaderChecksums (bool): This is used for Multis and Xdensity as checksum is not calculated correctly when change on the fly operations are performed. When this option is enabled IxOS uses 2 bytes before CRC, that way ensuring the checksum is correct when change on the fly operations are performed.
        - CycleOffsetForScheduledStart (number): 
        - CycleOffsetUnitForScheduledStart (str(microseconds | milliseconds | nanoseconds | seconds)): 
        - CycleTimeForScheduledStart (number): 
        - CycleTimeUnitForScheduledStart (str(microseconds | milliseconds | nanoseconds | seconds)): 
        - DataPlaneJitterWindow (str(0 | 10485760 | 1310720 | 167772160 | 20971520 | 2621440 | 335544320 | 41943040 | 5242880 | 671088640 | 83886080)): Indicates the number of packets received during a time interval. This is used forcalculating the rate on the recieve side.
        - DelayTimeForScheduledStart (number): Delay Time For Scheduled Start Transmit in seconds
        - DestMacRetryCount (number): The number of time to attempt to obtain the destination MAC address.
        - DestMacRetryDelay (number): The number of seconds to wait between attempts to obtain the destination MAC address.
        - DetectMisdirectedOnAllPorts (bool): 
        - DisablePortLevelMisdirected (bool): 
        - DisplayMplsCurrentLabelValue (bool): Displays current label value for LSP Endpoints.
        - EnableDataIntegrityCheck (bool): If true, enable data integrity check.
        - EnableDestMacRetry (bool): If true, enables the destination MAC address retry function.
        - EnableEgressOnlyTracking (bool): This flags enables/disables egress only tracking on the quick flow group. In this mode only quick flow groups are supported, user will have only PGID stats and the packets will not contain any instrumentation block.
        - EnableInstantaneousStatsSupport (bool): If true, enables instantaneous stats support
        - EnableLagAutoRate (bool): 
        - EnableLagFlowBalancing (bool): 
        - EnableLagFlowFailoverMode (bool): 
        - EnableLagRebalanceOnPortUp (bool): 
        - EnableMinFrameSize (bool): If true, IxNetwork will allow the stream to use smaller packet sizes. (In the case of IPv4 and Ethernet, 64 bytes will be allowed.) This is achieved by reducing the size of the instrumentation tag, which will be identified by receiving ports.
        - EnableMulticastScalingFactor (bool): If true, traffic items with the Merged Destination Ranges option selected have be to manually regenerated by the user.
        - EnableSequenceChecking (bool): If true, this field enables sequence checking. The default is false.
        - EnableStaggeredStartDelay (bool): If checked, enables the staggered start delay function.
        - EnableStaggeredTransmit (bool): If true, the start of transmit is staggered across ports. A 25-30 ms delay is introduced between the time one port begins transmitting and the time next port begins transmitting.
        - EnableStreamOrdering (bool): If true, IxNetwork will allow stream ordering per RFC 2889.
        - FrameOrderingMode (str(flowGroupSetup | none | peakLoading | RFC2889)): If true, enables frame ordering.
        - GlobalStreamControl (str(continuous | iterations)): The Global Stream Control parameters.
        - GlobalStreamControlIterations (number): If true, the user can specify how many times each packet stream will be transmitted.
        - LargeErrorThreshhold (number): The user-configurable threshold value used to determine error levels for out-of-sequence, received packets.
        - LearningFrameSize (number): Learns frame size
        - LearningFramesCount (number): Learns frames count
        - LearningFramesRate (number): Learns frames rate
        - MacChangeOnFly (bool): If true, enables IxNetwork's gratuitous ARP capability. When enabled, IxNetwork listens for gratuitous ARP messages from its neighbors.
        - MaxTrafficGenerationQueries (number): The maximum number of traffic generation queries. The default is 500.
        - MplsLabelLearningTimeout (number): The MPLS label learning timeout in seconds. The default is 30 seconds.
        - PeakLoadingReplicationCount (number): The peak loading replication count
        - PreventDataPlaneToCpu (bool): Prevent all data plane packets from being forwarded to Port CPU (disabling this option requires Port CPU reboot)
        - RefreshLearnedInfoBeforeApply (bool): This field refreshes the learned information from the DUT.
        - UseRfc5952 (bool): Use RFC 5952 for formatting IPv6 addresses (:ffff:1.2.3.4)
        - UseScheduledStartTransmit (bool): Use Scheduled Start Transmit
        - UseTxRxSync (bool): If true, enables the transmit/receive port synchronization algorithm.
        - WaitTime (number): The time (in seconds) to wait after Stop Transmit before stopping Latency Measurement.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def Apply(self):
        """Executes the apply operation on the server.

        Apply the traffic configuration.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyApplicationTraffic(self):
        """Executes the applyApplicationTraffic operation on the server.

        Apply the stateful traffic configuration.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyApplicationTraffic', payload=payload, response_object=None)

    def ApplyOnTheFlyTrafficChanges(self):
        """Executes the applyOnTheFlyTrafficChanges operation on the server.

        Apply on the fly traffic changes.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyOnTheFlyTrafficChanges', payload=payload, response_object=None)

    def ApplyStatefulTraffic(self):
        """Executes the applyStatefulTraffic operation on the server.

        Apply the traffic configuration for stateful traffic items only.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyStatefulTraffic', payload=payload, response_object=None)

    def GetFrameCountForDuration(self, *args, **kwargs):
        """Executes the getFrameCountForDuration operation on the server.

        Get the frame count for a specific duration.

        getFrameCountForDuration(Arg2=list)list
        ---------------------------------------
        - Arg2 (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/traffic/.../highLevelStream],arg2:number))): An array of structures. Each structure is one valid highLevelStream object reference and the duration to get the frame count for.
        - Returns list(number): An array of frame counts.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getFrameCountForDuration', payload=payload, response_object=None)

    def MakeStatelessTrafficUnapplied(self):
        """Executes the makeStatelessTrafficUnapplied operation on the server.

        Move stateless traffic to unapplied state.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('makeStatelessTrafficUnapplied', payload=payload, response_object=None)

    def SendL2L3Learning(self):
        """Executes the sendL2L3Learning operation on the server.

        Send L2 and L3 learning frames.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('sendL2L3Learning', payload=payload, response_object=None)

    def Start(self):
        """Executes the start operation on the server.

        Start the traffic configuration.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def StartApplicationTraffic(self):
        """Executes the startApplicationTraffic operation on the server.

        Start the stateful traffic configuration.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('startApplicationTraffic', payload=payload, response_object=None)

    def StartStatefulTraffic(self):
        """Executes the startStatefulTraffic operation on the server.

        Start stateful traffic items only.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('startStatefulTraffic', payload=payload, response_object=None)

    def StartStatelessTraffic(self):
        """Executes the startStatelessTraffic operation on the server.

        Start the traffic configuration for stateless traffic items only.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('startStatelessTraffic', payload=payload, response_object=None)

    def StartStatelessTrafficBlocking(self):
        """Executes the startStatelessTrafficBlocking operation on the server.

        Start the traffic configuration for stateless traffic items only. This will block until traffic is fully started.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('startStatelessTrafficBlocking', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stop the traffic configuration.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)

    def StopApplicationTraffic(self):
        """Executes the stopApplicationTraffic operation on the server.

        Stop the stateful traffic configuration.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stopApplicationTraffic', payload=payload, response_object=None)

    def StopStatefulTraffic(self):
        """Executes the stopStatefulTraffic operation on the server.

        Stop stateful traffic items only.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stopStatefulTraffic', payload=payload, response_object=None)

    def StopStatelessTraffic(self):
        """Executes the stopStatelessTraffic operation on the server.

        Stop the stateless traffic items.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stopStatelessTraffic', payload=payload, response_object=None)

    def StopStatelessTrafficBlocking(self):
        """Executes the stopStatelessTrafficBlocking operation on the server.

        Stop the traffic configuration for stateless traffic items only. This will block until traffic is fully stopped.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stopStatelessTrafficBlocking', payload=payload, response_object=None)
