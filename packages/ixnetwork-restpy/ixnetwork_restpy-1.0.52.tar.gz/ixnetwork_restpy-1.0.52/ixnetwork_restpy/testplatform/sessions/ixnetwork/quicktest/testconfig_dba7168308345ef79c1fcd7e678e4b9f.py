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


class TestConfig(Base):
    """The test configuration.
    The TestConfig class encapsulates a required testConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testConfig'

    def __init__(self, parent):
        super(TestConfig, self).__init__(parent)

    @property
    def ApplyMode(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('applyMode')
    @ApplyMode.setter
    def ApplyMode(self, value):
        self._set_attribute('applyMode', value)

    @property
    def AssignGroupType(self):
        """
        Returns
        -------
        - str(accumulated | distributed): The assigned group type.
        """
        return self._get_attribute('assignGroupType')
    @AssignGroupType.setter
    def AssignGroupType(self, value):
        self._set_attribute('assignGroupType', value)

    @property
    def BackoffIteration(self):
        """
        Returns
        -------
        - number: IF true, the iteration is backed off.
        """
        return self._get_attribute('backoffIteration')
    @BackoffIteration.setter
    def BackoffIteration(self, value):
        self._set_attribute('backoffIteration', value)

    @property
    def BidirectionalOptionEnabled(self):
        """
        Returns
        -------
        - bool: if true, the bidirectional option is enabled.
        """
        return self._get_attribute('bidirectionalOptionEnabled')
    @BidirectionalOptionEnabled.setter
    def BidirectionalOptionEnabled(self, value):
        self._set_attribute('bidirectionalOptionEnabled', value)

    @property
    def BinaryBackoff(self):
        """
        Returns
        -------
        - number: The binary backoff.
        """
        return self._get_attribute('binaryBackoff')
    @BinaryBackoff.setter
    def BinaryBackoff(self, value):
        self._set_attribute('binaryBackoff', value)

    @property
    def BinaryFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): The binary frame loss unit.
        """
        return self._get_attribute('binaryFrameLossUnit')
    @BinaryFrameLossUnit.setter
    def BinaryFrameLossUnit(self, value):
        self._set_attribute('binaryFrameLossUnit', value)

    @property
    def BinaryLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The binary load unit.
        """
        return self._get_attribute('binaryLoadUnit')
    @BinaryLoadUnit.setter
    def BinaryLoadUnit(self, value):
        self._set_attribute('binaryLoadUnit', value)

    @property
    def BinaryResolution(self):
        """
        Returns
        -------
        - number: The binary resolution.
        """
        return self._get_attribute('binaryResolution')
    @BinaryResolution.setter
    def BinaryResolution(self, value):
        self._set_attribute('binaryResolution', value)

    @property
    def BinarySearchType(self):
        """
        Returns
        -------
        - str(linear): The binary search type.
        """
        return self._get_attribute('binarySearchType')
    @BinarySearchType.setter
    def BinarySearchType(self, value):
        self._set_attribute('binarySearchType', value)

    @property
    def BinaryTolerance(self):
        """
        Returns
        -------
        - number: The binary tolerance.
        """
        return self._get_attribute('binaryTolerance')
    @BinaryTolerance.setter
    def BinaryTolerance(self, value):
        self._set_attribute('binaryTolerance', value)

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - number: The burst size.
        """
        return self._get_attribute('burstSize')
    @BurstSize.setter
    def BurstSize(self, value):
        self._set_attribute('burstSize', value)

    @property
    def CalculateJitter(self):
        """
        Returns
        -------
        - bool: The calculated jitter.
        """
        return self._get_attribute('calculateJitter')
    @CalculateJitter.setter
    def CalculateJitter(self, value):
        self._set_attribute('calculateJitter', value)

    @property
    def CalculateLatency(self):
        """
        Returns
        -------
        - bool: The latency is calculated.
        """
        return self._get_attribute('calculateLatency')
    @CalculateLatency.setter
    def CalculateLatency(self, value):
        self._set_attribute('calculateLatency', value)

    @property
    def CountRandomFrameSize(self):
        """
        Returns
        -------
        - number: if true, the random frame size is counted.
        """
        return self._get_attribute('countRandomFrameSize')
    @CountRandomFrameSize.setter
    def CountRandomFrameSize(self, value):
        self._set_attribute('countRandomFrameSize', value)

    @property
    def DelayAfterTransmit(self):
        """
        Returns
        -------
        - number: The delay after transmit of test config.
        """
        return self._get_attribute('delayAfterTransmit')
    @DelayAfterTransmit.setter
    def DelayAfterTransmit(self, value):
        self._set_attribute('delayAfterTransmit', value)

    @property
    def Duration(self):
        """
        Returns
        -------
        - number: The test configuration duration.
        """
        return self._get_attribute('duration')
    @Duration.setter
    def Duration(self, value):
        self._set_attribute('duration', value)

    @property
    def EnableBackoffIteration(self):
        """
        Returns
        -------
        - bool: If true, the back off iteration is enabled.
        """
        return self._get_attribute('enableBackoffIteration')
    @EnableBackoffIteration.setter
    def EnableBackoffIteration(self, value):
        self._set_attribute('enableBackoffIteration', value)

    @property
    def EnableDataIntegrity(self):
        """
        Returns
        -------
        - bool: If true, data integrity is enabled.
        """
        return self._get_attribute('enableDataIntegrity')
    @EnableDataIntegrity.setter
    def EnableDataIntegrity(self, value):
        self._set_attribute('enableDataIntegrity', value)

    @property
    def EnableExtraIterations(self):
        """
        Returns
        -------
        - bool: If true, extra iterations are enabled.
        """
        return self._get_attribute('enableExtraIterations')
    @EnableExtraIterations.setter
    def EnableExtraIterations(self, value):
        self._set_attribute('enableExtraIterations', value)

    @property
    def EnableFastConvergence(self):
        """
        Returns
        -------
        - bool: If true, fast convergence is enabled.
        """
        return self._get_attribute('enableFastConvergence')
    @EnableFastConvergence.setter
    def EnableFastConvergence(self, value):
        self._set_attribute('enableFastConvergence', value)

    @property
    def EnableLayer1Rate(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableLayer1Rate')
    @EnableLayer1Rate.setter
    def EnableLayer1Rate(self, value):
        self._set_attribute('enableLayer1Rate', value)

    @property
    def EnableLeaveGroup(self):
        """
        Returns
        -------
        - bool: If true, the leave group is enabled.
        """
        return self._get_attribute('enableLeaveGroup')
    @EnableLeaveGroup.setter
    def EnableLeaveGroup(self, value):
        self._set_attribute('enableLeaveGroup', value)

    @property
    def EnableMinFrameSize(self):
        """
        Returns
        -------
        - bool: If true,the minimum frame size is enabled.
        """
        return self._get_attribute('enableMinFrameSize')
    @EnableMinFrameSize.setter
    def EnableMinFrameSize(self, value):
        self._set_attribute('enableMinFrameSize', value)

    @property
    def EnableMulticastQuerier(self):
        """
        Returns
        -------
        - bool: Enable Multicast Querier Settings
        """
        return self._get_attribute('enableMulticastQuerier')
    @EnableMulticastQuerier.setter
    def EnableMulticastQuerier(self, value):
        self._set_attribute('enableMulticastQuerier', value)

    @property
    def EnableOldStatsForReef(self):
        """
        Returns
        -------
        - bool: If true, the old stats for reef is enabled.
        """
        return self._get_attribute('enableOldStatsForReef')
    @EnableOldStatsForReef.setter
    def EnableOldStatsForReef(self, value):
        self._set_attribute('enableOldStatsForReef', value)

    @property
    def EnableSaturationIteration(self):
        """
        Returns
        -------
        - bool: If true, the saturation iteration us enabled.
        """
        return self._get_attribute('enableSaturationIteration')
    @EnableSaturationIteration.setter
    def EnableSaturationIteration(self, value):
        self._set_attribute('enableSaturationIteration', value)

    @property
    def EnableStopTestOnHighLoss(self):
        """
        Returns
        -------
        - bool: If true, the test is stopped on high loss.
        """
        return self._get_attribute('enableStopTestOnHighLoss')
    @EnableStopTestOnHighLoss.setter
    def EnableStopTestOnHighLoss(self, value):
        self._set_attribute('enableStopTestOnHighLoss', value)

    @property
    def ExtraIterationOffsets(self):
        """
        Returns
        -------
        - str: The extra iteration offsets.
        """
        return self._get_attribute('extraIterationOffsets')
    @ExtraIterationOffsets.setter
    def ExtraIterationOffsets(self, value):
        self._set_attribute('extraIterationOffsets', value)

    @property
    def FastConvergenceDuration(self):
        """
        Returns
        -------
        - number: The fast convergence duration.
        """
        return self._get_attribute('fastConvergenceDuration')
    @FastConvergenceDuration.setter
    def FastConvergenceDuration(self, value):
        self._set_attribute('fastConvergenceDuration', value)

    @property
    def FastConvergenceThreshold(self):
        """
        Returns
        -------
        - number: The fast convergence threshold.
        """
        return self._get_attribute('fastConvergenceThreshold')
    @FastConvergenceThreshold.setter
    def FastConvergenceThreshold(self, value):
        self._set_attribute('fastConvergenceThreshold', value)

    @property
    def FloodedFramesEnabled(self):
        """
        Returns
        -------
        - bool: If true, it enables the flooded frames statistics
        """
        return self._get_attribute('floodedFramesEnabled')
    @FloodedFramesEnabled.setter
    def FloodedFramesEnabled(self, value):
        self._set_attribute('floodedFramesEnabled', value)

    @property
    def ForceRegenerate(self):
        """
        Returns
        -------
        - bool: If true, the test configuration is forcefully regenerated.
        """
        return self._get_attribute('forceRegenerate')
    @ForceRegenerate.setter
    def ForceRegenerate(self, value):
        self._set_attribute('forceRegenerate', value)

    @property
    def FrameLossUnit(self):
        """
        Returns
        -------
        - str: The frame loss unit.
        """
        return self._get_attribute('frameLossUnit')
    @FrameLossUnit.setter
    def FrameLossUnit(self, value):
        self._set_attribute('frameLossUnit', value)

    @property
    def FrameSizeMode(self):
        """
        Returns
        -------
        - str(custom | fixed | increment | random): The frame size mode of test configuration.
        """
        return self._get_attribute('frameSizeMode')
    @FrameSizeMode.setter
    def FrameSizeMode(self, value):
        self._set_attribute('frameSizeMode', value)

    @property
    def FramelossPercentValue(self):
        """
        Returns
        -------
        - number: The frame loss percentage value.
        """
        return self._get_attribute('framelossPercentValue')
    @FramelossPercentValue.setter
    def FramelossPercentValue(self, value):
        self._set_attribute('framelossPercentValue', value)

    @property
    def FramesPerBurstGap(self):
        """
        Returns
        -------
        - number: The frames per burst gap.
        """
        return self._get_attribute('framesPerBurstGap')
    @FramesPerBurstGap.setter
    def FramesPerBurstGap(self, value):
        self._set_attribute('framesPerBurstGap', value)

    @property
    def FramesizeList(self):
        """
        Returns
        -------
        - list(str): The frame size list of the test configuration.
        """
        return self._get_attribute('framesizeList')
    @FramesizeList.setter
    def FramesizeList(self, value):
        self._set_attribute('framesizeList', value)

    @property
    def Gap(self):
        """
        Returns
        -------
        - number: The test configuration gap.
        """
        return self._get_attribute('gap')
    @Gap.setter
    def Gap(self, value):
        self._set_attribute('gap', value)

    @property
    def GroupDistributionType(self):
        """
        Returns
        -------
        - str(acrossHosts | acrossPorts): The group distribution type.
        """
        return self._get_attribute('groupDistributionType')
    @GroupDistributionType.setter
    def GroupDistributionType(self, value):
        self._set_attribute('groupDistributionType', value)

    @property
    def IgmpV1Timeout(self):
        """
        Returns
        -------
        - number: The igmp V1 timeout.
        """
        return self._get_attribute('igmpV1Timeout')
    @IgmpV1Timeout.setter
    def IgmpV1Timeout(self, value):
        self._set_attribute('igmpV1Timeout', value)

    @property
    def IgmpVersion(self):
        """
        Returns
        -------
        - number: The igmp version of the test configuration.
        """
        return self._get_attribute('igmpVersion')
    @IgmpVersion.setter
    def IgmpVersion(self, value):
        self._set_attribute('igmpVersion', value)

    @property
    def Igmpv3MessageType(self):
        """
        Returns
        -------
        - str(exclude | include): It gives details about the igmpv3 message type in the test configuration
        """
        return self._get_attribute('igmpv3MessageType')
    @Igmpv3MessageType.setter
    def Igmpv3MessageType(self, value):
        self._set_attribute('igmpv3MessageType', value)

    @property
    def Igmpv3SourceAddrList(self):
        """
        Returns
        -------
        - str: It gives details about the igmpv3 source address list in the test configuration
        """
        return self._get_attribute('igmpv3SourceAddrList')
    @Igmpv3SourceAddrList.setter
    def Igmpv3SourceAddrList(self, value):
        self._set_attribute('igmpv3SourceAddrList', value)

    @property
    def IncrAddresses(self):
        """
        Returns
        -------
        - number: The incremented address of the test configuration.
        """
        return self._get_attribute('incrAddresses')
    @IncrAddresses.setter
    def IncrAddresses(self, value):
        self._set_attribute('incrAddresses', value)

    @property
    def InitialBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The initial binary load rate.
        """
        return self._get_attribute('initialBinaryLoadRate')
    @InitialBinaryLoadRate.setter
    def InitialBinaryLoadRate(self, value):
        self._set_attribute('initialBinaryLoadRate', value)

    @property
    def InitialRate(self):
        """
        Returns
        -------
        - str: The initial rate of the test configuration.
        """
        return self._get_attribute('initialRate')
    @InitialRate.setter
    def InitialRate(self, value):
        self._set_attribute('initialRate', value)

    @property
    def InitialStepLoadRate(self):
        """
        Returns
        -------
        - number: The initial step of the load type.
        """
        return self._get_attribute('initialStepLoadRate')
    @InitialStepLoadRate.setter
    def InitialStepLoadRate(self, value):
        self._set_attribute('initialStepLoadRate', value)

    @property
    def Ipv4Address(self):
        """
        Returns
        -------
        - str: The IPV4 address.
        """
        return self._get_attribute('ipv4Address')
    @Ipv4Address.setter
    def Ipv4Address(self, value):
        self._set_attribute('ipv4Address', value)

    @property
    def Ipv6Address(self):
        """
        Returns
        -------
        - str: The IPV6 address.
        """
        return self._get_attribute('ipv6Address')
    @Ipv6Address.setter
    def Ipv6Address(self, value):
        self._set_attribute('ipv6Address', value)

    @property
    def IsIPv6(self):
        """
        Returns
        -------
        - str: The ipv6 address.
        """
        return self._get_attribute('isIPv6')
    @IsIPv6.setter
    def IsIPv6(self, value):
        self._set_attribute('isIPv6', value)

    @property
    def IsMulticastAutomaticFrameData(self):
        """
        Returns
        -------
        - str: The Multicast automatic frame data.
        """
        return self._get_attribute('isMulticastAutomaticFrameData')
    @IsMulticastAutomaticFrameData.setter
    def IsMulticastAutomaticFrameData(self, value):
        self._set_attribute('isMulticastAutomaticFrameData', value)

    @property
    def JoinLeaveMultiplier(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('joinLeaveMultiplier')
    @JoinLeaveMultiplier.setter
    def JoinLeaveMultiplier(self, value):
        self._set_attribute('joinLeaveMultiplier', value)

    @property
    def JoinLeaveRate(self):
        """
        Returns
        -------
        - number: The join and leave rate of the test configuration.
        """
        return self._get_attribute('joinLeaveRate')
    @JoinLeaveRate.setter
    def JoinLeaveRate(self, value):
        self._set_attribute('joinLeaveRate', value)

    @property
    def JoinLeaveWaitTime(self):
        """
        Returns
        -------
        - number: The join and leave wait time.
        """
        return self._get_attribute('joinLeaveWaitTime')
    @JoinLeaveWaitTime.setter
    def JoinLeaveWaitTime(self, value):
        self._set_attribute('joinLeaveWaitTime', value)

    @property
    def LatencyBins(self):
        """DEPRECATED 
        Returns
        -------
        - str: Sets the latency bins statistics
        """
        return self._get_attribute('latencyBins')
    @LatencyBins.setter
    def LatencyBins(self, value):
        self._set_attribute('latencyBins', value)

    @property
    def LatencyBinsEnabled(self):
        """
        Returns
        -------
        - bool: Enables the latency bins statistics
        """
        return self._get_attribute('latencyBinsEnabled')
    @LatencyBinsEnabled.setter
    def LatencyBinsEnabled(self, value):
        self._set_attribute('latencyBinsEnabled', value)

    @property
    def LatencyType(self):
        """
        Returns
        -------
        - str(cutThrough | storeForward): The latency type.
        """
        return self._get_attribute('latencyType')
    @LatencyType.setter
    def LatencyType(self, value):
        self._set_attribute('latencyType', value)

    @property
    def LoadInitialRate(self):
        """
        Returns
        -------
        - number: The initial rate of the load.
        """
        return self._get_attribute('loadInitialRate')
    @LoadInitialRate.setter
    def LoadInitialRate(self, value):
        self._set_attribute('loadInitialRate', value)

    @property
    def LoadType(self):
        """
        Returns
        -------
        - str(binary | quickSearch | step): The load type.
        """
        return self._get_attribute('loadType')
    @LoadType.setter
    def LoadType(self, value):
        self._set_attribute('loadType', value)

    @property
    def MapType(self):
        """
        Returns
        -------
        - str: The map type.
        """
        return self._get_attribute('mapType')
    @MapType.setter
    def MapType(self, value):
        self._set_attribute('mapType', value)

    @property
    def MaxBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The maximum binary load rate.
        """
        return self._get_attribute('maxBinaryLoadRate')
    @MaxBinaryLoadRate.setter
    def MaxBinaryLoadRate(self, value):
        self._set_attribute('maxBinaryLoadRate', value)

    @property
    def MaxIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The maximum frame size incrememnt.
        """
        return self._get_attribute('maxIncrementFrameSize')
    @MaxIncrementFrameSize.setter
    def MaxIncrementFrameSize(self, value):
        self._set_attribute('maxIncrementFrameSize', value)

    @property
    def MaxQuickSearchLoadRate(self):
        """
        Returns
        -------
        - number: Sets the maximum QuickSearch load rate
        """
        return self._get_attribute('maxQuickSearchLoadRate')
    @MaxQuickSearchLoadRate.setter
    def MaxQuickSearchLoadRate(self, value):
        self._set_attribute('maxQuickSearchLoadRate', value)

    @property
    def MaxRandomFrameSize(self):
        """
        Returns
        -------
        - number: The maximum random frame size.
        """
        return self._get_attribute('maxRandomFrameSize')
    @MaxRandomFrameSize.setter
    def MaxRandomFrameSize(self, value):
        self._set_attribute('maxRandomFrameSize', value)

    @property
    def MaxStepLoadRate(self):
        """
        Returns
        -------
        - number: The maximum step of the load rate.
        """
        return self._get_attribute('maxStepLoadRate')
    @MaxStepLoadRate.setter
    def MaxStepLoadRate(self, value):
        self._set_attribute('maxStepLoadRate', value)

    @property
    def MinBinaryLoadRate(self):
        """
        Returns
        -------
        - number: The minimum binary load rate.
        """
        return self._get_attribute('minBinaryLoadRate')
    @MinBinaryLoadRate.setter
    def MinBinaryLoadRate(self, value):
        self._set_attribute('minBinaryLoadRate', value)

    @property
    def MinIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The minimum frame size increment.
        """
        return self._get_attribute('minIncrementFrameSize')
    @MinIncrementFrameSize.setter
    def MinIncrementFrameSize(self, value):
        self._set_attribute('minIncrementFrameSize', value)

    @property
    def MinQuickSearchLoadRate(self):
        """
        Returns
        -------
        - number: Sets the minum Quick Search load rate
        """
        return self._get_attribute('minQuickSearchLoadRate')
    @MinQuickSearchLoadRate.setter
    def MinQuickSearchLoadRate(self, value):
        self._set_attribute('minQuickSearchLoadRate', value)

    @property
    def MinRandomFrameSize(self):
        """
        Returns
        -------
        - number: The minimum random frame size.
        """
        return self._get_attribute('minRandomFrameSize')
    @MinRandomFrameSize.setter
    def MinRandomFrameSize(self, value):
        self._set_attribute('minRandomFrameSize', value)

    @property
    def MldVersion(self):
        """
        Returns
        -------
        - number: The mld version of the test configuration.
        """
        return self._get_attribute('mldVersion')
    @MldVersion.setter
    def MldVersion(self, value):
        self._set_attribute('mldVersion', value)

    @property
    def NumAddresses(self):
        """
        Returns
        -------
        - number: The number of addresses of the test configuration.
        """
        return self._get_attribute('numAddresses')
    @NumAddresses.setter
    def NumAddresses(self, value):
        self._set_attribute('numAddresses', value)

    @property
    def NumIterations(self):
        """
        Returns
        -------
        - number: The number of iterations.
        """
        return self._get_attribute('numIterations')
    @NumIterations.setter
    def NumIterations(self, value):
        self._set_attribute('numIterations', value)

    @property
    def Numtrials(self):
        """
        Returns
        -------
        - number: The number of trials for the test configuration.
        """
        return self._get_attribute('numtrials')
    @Numtrials.setter
    def Numtrials(self, value):
        self._set_attribute('numtrials', value)

    @property
    def PortDelayEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('portDelayEnabled')
    @PortDelayEnabled.setter
    def PortDelayEnabled(self, value):
        self._set_attribute('portDelayEnabled', value)

    @property
    def PortDelayUnit(self):
        """
        Returns
        -------
        - str(bytes | nanoseconds): Sets the port delay unit in which it will be measured
        """
        return self._get_attribute('portDelayUnit')
    @PortDelayUnit.setter
    def PortDelayUnit(self, value):
        self._set_attribute('portDelayUnit', value)

    @property
    def PortDelayValue(self):
        """
        Returns
        -------
        - number: Sets the port delay value
        """
        return self._get_attribute('portDelayValue')
    @PortDelayValue.setter
    def PortDelayValue(self, value):
        self._set_attribute('portDelayValue', value)

    @property
    def ProtocolItem(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan]): Protocol Items
        """
        return self._get_attribute('protocolItem')
    @ProtocolItem.setter
    def ProtocolItem(self, value):
        self._set_attribute('protocolItem', value)

    @property
    def QuickSearchFrameLossUnit(self):
        """
        Returns
        -------
        - str(%): Sets the quick search frame loss unit
        """
        return self._get_attribute('quickSearchFrameLossUnit')
    @QuickSearchFrameLossUnit.setter
    def QuickSearchFrameLossUnit(self, value):
        self._set_attribute('quickSearchFrameLossUnit', value)

    @property
    def QuickSearchLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): Sets the quick search load unit
        """
        return self._get_attribute('quickSearchLoadUnit')
    @QuickSearchLoadUnit.setter
    def QuickSearchLoadUnit(self, value):
        self._set_attribute('quickSearchLoadUnit', value)

    @property
    def QuickSearchResolution(self):
        """
        Returns
        -------
        - number: Sets the quick search resolution
        """
        return self._get_attribute('quickSearchResolution')
    @QuickSearchResolution.setter
    def QuickSearchResolution(self, value):
        self._set_attribute('quickSearchResolution', value)

    @property
    def QuickSearchSearchType(self):
        """
        Returns
        -------
        - str(linear): Sets the quick search type
        """
        return self._get_attribute('quickSearchSearchType')
    @QuickSearchSearchType.setter
    def QuickSearchSearchType(self, value):
        self._set_attribute('quickSearchSearchType', value)

    @property
    def QuickSearchTolerance(self):
        """
        Returns
        -------
        - number: Sets the quick search tolerance
        """
        return self._get_attribute('quickSearchTolerance')
    @QuickSearchTolerance.setter
    def QuickSearchTolerance(self, value):
        self._set_attribute('quickSearchTolerance', value)

    @property
    def ReportSequenceError(self):
        """
        Returns
        -------
        - bool: The report of sequence error.
        """
        return self._get_attribute('reportSequenceError')
    @ReportSequenceError.setter
    def ReportSequenceError(self, value):
        self._set_attribute('reportSequenceError', value)

    @property
    def ReportTputRateUnit(self):
        """
        Returns
        -------
        - str(gbps | gBps | kbps | kBps | mbps | mBps): The report throughput rate unit.
        """
        return self._get_attribute('reportTputRateUnit')
    @ReportTputRateUnit.setter
    def ReportTputRateUnit(self, value):
        self._set_attribute('reportTputRateUnit', value)

    @property
    def RouterAlert(self):
        """
        Returns
        -------
        - bool: The router alert.
        """
        return self._get_attribute('routerAlert')
    @RouterAlert.setter
    def RouterAlert(self, value):
        self._set_attribute('routerAlert', value)

    @property
    def SaturationIteration(self):
        """
        Returns
        -------
        - number: The saturation iteration.
        """
        return self._get_attribute('saturationIteration')
    @SaturationIteration.setter
    def SaturationIteration(self, value):
        self._set_attribute('saturationIteration', value)

    @property
    def ShowDetailedBinaryResults(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('showDetailedBinaryResults')
    @ShowDetailedBinaryResults.setter
    def ShowDetailedBinaryResults(self, value):
        self._set_attribute('showDetailedBinaryResults', value)

    @property
    def StepFrameLossUnit(self):
        """
        Returns
        -------
        - str(% | frames): The step frame loss unit.
        """
        return self._get_attribute('stepFrameLossUnit')
    @StepFrameLossUnit.setter
    def StepFrameLossUnit(self, value):
        self._set_attribute('stepFrameLossUnit', value)

    @property
    def StepIncrementFrameSize(self):
        """
        Returns
        -------
        - number: The step increment frame size.
        """
        return self._get_attribute('stepIncrementFrameSize')
    @StepIncrementFrameSize.setter
    def StepIncrementFrameSize(self, value):
        self._set_attribute('stepIncrementFrameSize', value)

    @property
    def StepLoadUnit(self):
        """
        Returns
        -------
        - str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate): The step load unit.
        """
        return self._get_attribute('stepLoadUnit')
    @StepLoadUnit.setter
    def StepLoadUnit(self, value):
        self._set_attribute('stepLoadUnit', value)

    @property
    def StepStepLoadRate(self):
        """
        Returns
        -------
        - number: The step of the step load rate.
        """
        return self._get_attribute('stepStepLoadRate')
    @StepStepLoadRate.setter
    def StepStepLoadRate(self, value):
        self._set_attribute('stepStepLoadRate', value)

    @property
    def StepTolerance(self):
        """
        Returns
        -------
        - number: The step tolerance.
        """
        return self._get_attribute('stepTolerance')
    @StepTolerance.setter
    def StepTolerance(self, value):
        self._set_attribute('stepTolerance', value)

    @property
    def StopTestOnHighLoss(self):
        """
        Returns
        -------
        - number: If true, the test is stopped at high loss.
        """
        return self._get_attribute('stopTestOnHighLoss')
    @StopTestOnHighLoss.setter
    def StopTestOnHighLoss(self, value):
        self._set_attribute('stopTestOnHighLoss', value)

    @property
    def SupportedTrafficTypes(self):
        """
        Returns
        -------
        - str: The supported traffic types.
        """
        return self._get_attribute('supportedTrafficTypes')
    @SupportedTrafficTypes.setter
    def SupportedTrafficTypes(self, value):
        self._set_attribute('supportedTrafficTypes', value)

    @property
    def TestMapType(self):
        """
        Returns
        -------
        - str(fullymesh | one2many): The test map type.
        """
        return self._get_attribute('testMapType')
    @TestMapType.setter
    def TestMapType(self, value):
        self._set_attribute('testMapType', value)

    @property
    def TestTrafficType(self):
        """
        Returns
        -------
        - str: The test traffic type.
        """
        return self._get_attribute('testTrafficType')
    @TestTrafficType.setter
    def TestTrafficType(self, value):
        self._set_attribute('testTrafficType', value)

    @property
    def TxDelay(self):
        """
        Returns
        -------
        - number: The transmission delay.
        """
        return self._get_attribute('txDelay')
    @TxDelay.setter
    def TxDelay(self, value):
        self._set_attribute('txDelay', value)

    @property
    def UnchangedInitial(self):
        """
        Returns
        -------
        - str(False | True): If true, the initial is unchanged.
        """
        return self._get_attribute('unchangedInitial')
    @UnchangedInitial.setter
    def UnchangedInitial(self, value):
        self._set_attribute('unchangedInitial', value)

    @property
    def UsePercentOffsets(self):
        """
        Returns
        -------
        - str: The use percent offsets.
        """
        return self._get_attribute('usePercentOffsets')
    @UsePercentOffsets.setter
    def UsePercentOffsets(self, value):
        self._set_attribute('usePercentOffsets', value)

    def update(self, ApplyMode=None, AssignGroupType=None, BackoffIteration=None, BidirectionalOptionEnabled=None, BinaryBackoff=None, BinaryFrameLossUnit=None, BinaryLoadUnit=None, BinaryResolution=None, BinarySearchType=None, BinaryTolerance=None, BurstSize=None, CalculateJitter=None, CalculateLatency=None, CountRandomFrameSize=None, DelayAfterTransmit=None, Duration=None, EnableBackoffIteration=None, EnableDataIntegrity=None, EnableExtraIterations=None, EnableFastConvergence=None, EnableLayer1Rate=None, EnableLeaveGroup=None, EnableMinFrameSize=None, EnableMulticastQuerier=None, EnableOldStatsForReef=None, EnableSaturationIteration=None, EnableStopTestOnHighLoss=None, ExtraIterationOffsets=None, FastConvergenceDuration=None, FastConvergenceThreshold=None, FloodedFramesEnabled=None, ForceRegenerate=None, FrameLossUnit=None, FrameSizeMode=None, FramelossPercentValue=None, FramesPerBurstGap=None, FramesizeList=None, Gap=None, GroupDistributionType=None, IgmpV1Timeout=None, IgmpVersion=None, Igmpv3MessageType=None, Igmpv3SourceAddrList=None, IncrAddresses=None, InitialBinaryLoadRate=None, InitialRate=None, InitialStepLoadRate=None, Ipv4Address=None, Ipv6Address=None, IsIPv6=None, IsMulticastAutomaticFrameData=None, JoinLeaveMultiplier=None, JoinLeaveRate=None, JoinLeaveWaitTime=None, LatencyBins=None, LatencyBinsEnabled=None, LatencyType=None, LoadInitialRate=None, LoadType=None, MapType=None, MaxBinaryLoadRate=None, MaxIncrementFrameSize=None, MaxQuickSearchLoadRate=None, MaxRandomFrameSize=None, MaxStepLoadRate=None, MinBinaryLoadRate=None, MinIncrementFrameSize=None, MinQuickSearchLoadRate=None, MinRandomFrameSize=None, MldVersion=None, NumAddresses=None, NumIterations=None, Numtrials=None, PortDelayEnabled=None, PortDelayUnit=None, PortDelayValue=None, ProtocolItem=None, QuickSearchFrameLossUnit=None, QuickSearchLoadUnit=None, QuickSearchResolution=None, QuickSearchSearchType=None, QuickSearchTolerance=None, ReportSequenceError=None, ReportTputRateUnit=None, RouterAlert=None, SaturationIteration=None, ShowDetailedBinaryResults=None, StepFrameLossUnit=None, StepIncrementFrameSize=None, StepLoadUnit=None, StepStepLoadRate=None, StepTolerance=None, StopTestOnHighLoss=None, SupportedTrafficTypes=None, TestMapType=None, TestTrafficType=None, TxDelay=None, UnchangedInitial=None, UsePercentOffsets=None):
        """Updates testConfig resource on the server.

        Args
        ----
        - ApplyMode (str): NOT DEFINED
        - AssignGroupType (str(accumulated | distributed)): The assigned group type.
        - BackoffIteration (number): IF true, the iteration is backed off.
        - BidirectionalOptionEnabled (bool): if true, the bidirectional option is enabled.
        - BinaryBackoff (number): The binary backoff.
        - BinaryFrameLossUnit (str(% | frames)): The binary frame loss unit.
        - BinaryLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The binary load unit.
        - BinaryResolution (number): The binary resolution.
        - BinarySearchType (str(linear)): The binary search type.
        - BinaryTolerance (number): The binary tolerance.
        - BurstSize (number): The burst size.
        - CalculateJitter (bool): The calculated jitter.
        - CalculateLatency (bool): The latency is calculated.
        - CountRandomFrameSize (number): if true, the random frame size is counted.
        - DelayAfterTransmit (number): The delay after transmit of test config.
        - Duration (number): The test configuration duration.
        - EnableBackoffIteration (bool): If true, the back off iteration is enabled.
        - EnableDataIntegrity (bool): If true, data integrity is enabled.
        - EnableExtraIterations (bool): If true, extra iterations are enabled.
        - EnableFastConvergence (bool): If true, fast convergence is enabled.
        - EnableLayer1Rate (bool): NOT DEFINED
        - EnableLeaveGroup (bool): If true, the leave group is enabled.
        - EnableMinFrameSize (bool): If true,the minimum frame size is enabled.
        - EnableMulticastQuerier (bool): Enable Multicast Querier Settings
        - EnableOldStatsForReef (bool): If true, the old stats for reef is enabled.
        - EnableSaturationIteration (bool): If true, the saturation iteration us enabled.
        - EnableStopTestOnHighLoss (bool): If true, the test is stopped on high loss.
        - ExtraIterationOffsets (str): The extra iteration offsets.
        - FastConvergenceDuration (number): The fast convergence duration.
        - FastConvergenceThreshold (number): The fast convergence threshold.
        - FloodedFramesEnabled (bool): If true, it enables the flooded frames statistics
        - ForceRegenerate (bool): If true, the test configuration is forcefully regenerated.
        - FrameLossUnit (str): The frame loss unit.
        - FrameSizeMode (str(custom | fixed | increment | random)): The frame size mode of test configuration.
        - FramelossPercentValue (number): The frame loss percentage value.
        - FramesPerBurstGap (number): The frames per burst gap.
        - FramesizeList (list(str)): The frame size list of the test configuration.
        - Gap (number): The test configuration gap.
        - GroupDistributionType (str(acrossHosts | acrossPorts)): The group distribution type.
        - IgmpV1Timeout (number): The igmp V1 timeout.
        - IgmpVersion (number): The igmp version of the test configuration.
        - Igmpv3MessageType (str(exclude | include)): It gives details about the igmpv3 message type in the test configuration
        - Igmpv3SourceAddrList (str): It gives details about the igmpv3 source address list in the test configuration
        - IncrAddresses (number): The incremented address of the test configuration.
        - InitialBinaryLoadRate (number): The initial binary load rate.
        - InitialRate (str): The initial rate of the test configuration.
        - InitialStepLoadRate (number): The initial step of the load type.
        - Ipv4Address (str): The IPV4 address.
        - Ipv6Address (str): The IPV6 address.
        - IsIPv6 (str): The ipv6 address.
        - IsMulticastAutomaticFrameData (str): The Multicast automatic frame data.
        - JoinLeaveMultiplier (number): NOT DEFINED
        - JoinLeaveRate (number): The join and leave rate of the test configuration.
        - JoinLeaveWaitTime (number): The join and leave wait time.
        - LatencyBins (str): Sets the latency bins statistics
        - LatencyBinsEnabled (bool): Enables the latency bins statistics
        - LatencyType (str(cutThrough | storeForward)): The latency type.
        - LoadInitialRate (number): The initial rate of the load.
        - LoadType (str(binary | quickSearch | step)): The load type.
        - MapType (str): The map type.
        - MaxBinaryLoadRate (number): The maximum binary load rate.
        - MaxIncrementFrameSize (number): The maximum frame size incrememnt.
        - MaxQuickSearchLoadRate (number): Sets the maximum QuickSearch load rate
        - MaxRandomFrameSize (number): The maximum random frame size.
        - MaxStepLoadRate (number): The maximum step of the load rate.
        - MinBinaryLoadRate (number): The minimum binary load rate.
        - MinIncrementFrameSize (number): The minimum frame size increment.
        - MinQuickSearchLoadRate (number): Sets the minum Quick Search load rate
        - MinRandomFrameSize (number): The minimum random frame size.
        - MldVersion (number): The mld version of the test configuration.
        - NumAddresses (number): The number of addresses of the test configuration.
        - NumIterations (number): The number of iterations.
        - Numtrials (number): The number of trials for the test configuration.
        - PortDelayEnabled (bool): NOT DEFINED
        - PortDelayUnit (str(bytes | nanoseconds)): Sets the port delay unit in which it will be measured
        - PortDelayValue (number): Sets the port delay value
        - ProtocolItem (list(str[None | /api/v1/sessions/1/ixnetwork/vport | /api/v1/sessions/1/ixnetwork/vport/.../lan])): Protocol Items
        - QuickSearchFrameLossUnit (str(%)): Sets the quick search frame loss unit
        - QuickSearchLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): Sets the quick search load unit
        - QuickSearchResolution (number): Sets the quick search resolution
        - QuickSearchSearchType (str(linear)): Sets the quick search type
        - QuickSearchTolerance (number): Sets the quick search tolerance
        - ReportSequenceError (bool): The report of sequence error.
        - ReportTputRateUnit (str(gbps | gBps | kbps | kBps | mbps | mBps)): The report throughput rate unit.
        - RouterAlert (bool): The router alert.
        - SaturationIteration (number): The saturation iteration.
        - ShowDetailedBinaryResults (bool): NOT DEFINED
        - StepFrameLossUnit (str(% | frames)): The step frame loss unit.
        - StepIncrementFrameSize (number): The step increment frame size.
        - StepLoadUnit (str(bpsRate | fpsRate | gbpsRate | gBpsRate | kbpsRate | kBpsRate | mbpsRate | mBpsRate | percentMaxRate)): The step load unit.
        - StepStepLoadRate (number): The step of the step load rate.
        - StepTolerance (number): The step tolerance.
        - StopTestOnHighLoss (number): If true, the test is stopped at high loss.
        - SupportedTrafficTypes (str): The supported traffic types.
        - TestMapType (str(fullymesh | one2many)): The test map type.
        - TestTrafficType (str): The test traffic type.
        - TxDelay (number): The transmission delay.
        - UnchangedInitial (str(False | True)): If true, the initial is unchanged.
        - UsePercentOffsets (str): The use percent offsets.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def Apply(self):
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyAsync(self):
        """Executes the applyAsync operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsync', payload=payload, response_object=None)

    def ApplyAsyncResult(self):
        """Executes the applyAsyncResult operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self):
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def GenerateReport(self):
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('generateReport', payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(InputParameters=string)list
        -------------------------------
        - InputParameters (str): The input arguments of the test.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('run', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(InputParameters=string)
        -----------------------------
        - InputParameters (str): The input arguments of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)

    def WaitForTest(self):
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('waitForTest', payload=payload, response_object=None)
