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


class CmacRouteAttributes(Base):
    """Configures route attributes for C-MAC ranges. These attributes are carried in MAC routes.
    The CmacRouteAttributes class encapsulates a required cmacRouteAttributes resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'cmacRouteAttributes'

    def __init__(self, parent):
        super(CmacRouteAttributes, self).__init__(parent)

    @property
    def AggregatorAs(self):
        """
        Returns
        -------
        - number: The AS associated with the aggregator router ID in the AGGREGATOR attribute. (default = 0)
        """
        return self._get_attribute('aggregatorAs')
    @AggregatorAs.setter
    def AggregatorAs(self, value):
        self._set_attribute('aggregatorAs', value)

    @property
    def AggregatorId(self):
        """
        Returns
        -------
        - str: The IP address of the router that aggregated two or more routes in the AGGREGATOR attribute. (default = 0.0.0.0)
        """
        return self._get_attribute('aggregatorId')
    @AggregatorId.setter
    def AggregatorId(self, value):
        self._set_attribute('aggregatorId', value)

    @property
    def AsPath(self):
        """
        Returns
        -------
        - list(dict(arg1:bool,arg2:str[unknown | asSet | asSequence | asConfedSet | asConfedSequence],arg3:list[number])): Indicates the local IP address of the BGP router
        """
        return self._get_attribute('asPath')
    @AsPath.setter
    def AsPath(self, value):
        self._set_attribute('asPath', value)

    @property
    def AsSetMode(self):
        """
        Returns
        -------
        - str(includeAsSeq | includeAsSeqConf | includeAsSet | includeAsSetConf | noInclude | prependAs): NOT DEFINED
        """
        return self._get_attribute('asSetMode')
    @AsSetMode.setter
    def AsSetMode(self, value):
        self._set_attribute('asSetMode', value)

    @property
    def Cluster(self):
        """
        Returns
        -------
        - list(number): The list of BGP clusters that a particular route has passed through
        """
        return self._get_attribute('cluster')
    @Cluster.setter
    def Cluster(self, value):
        self._set_attribute('cluster', value)

    @property
    def Community(self):
        """
        Returns
        -------
        - list(number): The BGP Community attribute to be added to the BGP entry
        """
        return self._get_attribute('community')
    @Community.setter
    def Community(self, value):
        self._set_attribute('community', value)

    @property
    def EnableAggregator(self):
        """
        Returns
        -------
        - bool: Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        """
        return self._get_attribute('enableAggregator')
    @EnableAggregator.setter
    def EnableAggregator(self, value):
        self._set_attribute('enableAggregator', value)

    @property
    def EnableAsPath(self):
        """
        Returns
        -------
        - bool: Indicates the local IP address of the BGP router.
        """
        return self._get_attribute('enableAsPath')
    @EnableAsPath.setter
    def EnableAsPath(self, value):
        self._set_attribute('enableAsPath', value)

    @property
    def EnableAtomicAggregate(self):
        """
        Returns
        -------
        - bool: Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        """
        return self._get_attribute('enableAtomicAggregate')
    @EnableAtomicAggregate.setter
    def EnableAtomicAggregate(self, value):
        self._set_attribute('enableAtomicAggregate', value)

    @property
    def EnableCluster(self):
        """
        Returns
        -------
        - bool: Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        """
        return self._get_attribute('enableCluster')
    @EnableCluster.setter
    def EnableCluster(self, value):
        self._set_attribute('enableCluster', value)

    @property
    def EnableCommunity(self):
        """
        Returns
        -------
        - bool: Enables the generation of a COMMUNITY attribute list. (default = false)
        """
        return self._get_attribute('enableCommunity')
    @EnableCommunity.setter
    def EnableCommunity(self, value):
        self._set_attribute('enableCommunity', value)

    @property
    def EnableLocalPref(self):
        """
        Returns
        -------
        - bool: Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        """
        return self._get_attribute('enableLocalPref')
    @EnableLocalPref.setter
    def EnableLocalPref(self, value):
        self._set_attribute('enableLocalPref', value)

    @property
    def EnableMultiExit(self):
        """
        Returns
        -------
        - bool: Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        """
        return self._get_attribute('enableMultiExit')
    @EnableMultiExit.setter
    def EnableMultiExit(self, value):
        self._set_attribute('enableMultiExit', value)

    @property
    def EnableNextHop(self):
        """
        Returns
        -------
        - bool: Enables the generation of a NEXT HOP attribute. (default = true)
        """
        return self._get_attribute('enableNextHop')
    @EnableNextHop.setter
    def EnableNextHop(self, value):
        self._set_attribute('enableNextHop', value)

    @property
    def EnableOrigin(self):
        """
        Returns
        -------
        - bool: Enables the generation of an ORIGIN attribute. (default = true)
        """
        return self._get_attribute('enableOrigin')
    @EnableOrigin.setter
    def EnableOrigin(self, value):
        self._set_attribute('enableOrigin', value)

    @property
    def EnableOriginator(self):
        """
        Returns
        -------
        - bool: Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        """
        return self._get_attribute('enableOriginator')
    @EnableOriginator.setter
    def EnableOriginator(self, value):
        self._set_attribute('enableOriginator', value)

    @property
    def ExtendedCommunity(self):
        """
        Returns
        -------
        - list(dict(arg1:str[decimal | hex | ip | ieeeFloat],arg2:str[decimal | hex | ip | ieeeFloat],arg3:str[twoOctetAs | ip | fourOctetAs | opaque | administratorAsTwoOctetLinkBw],arg4:str[routeTarget | origin | extendedBandwidthSubType],arg5:str)): This object is used to construct an extended community attribute for a route item
        """
        return self._get_attribute('extendedCommunity')
    @ExtendedCommunity.setter
    def ExtendedCommunity(self, value):
        self._set_attribute('extendedCommunity', value)

    @property
    def LocalPref(self):
        """
        Returns
        -------
        - number: The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        """
        return self._get_attribute('localPref')
    @LocalPref.setter
    def LocalPref(self, value):
        self._set_attribute('localPref', value)

    @property
    def MultiExit(self):
        """
        Returns
        -------
        - number: The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        """
        return self._get_attribute('multiExit')
    @MultiExit.setter
    def MultiExit(self, value):
        self._set_attribute('multiExit', value)

    @property
    def NextHop(self):
        """
        Returns
        -------
        - str: The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        """
        return self._get_attribute('nextHop')
    @NextHop.setter
    def NextHop(self, value):
        self._set_attribute('nextHop', value)

    @property
    def NextHopIpType(self):
        """
        Returns
        -------
        - str(ipv4 | ipv6): IP type of Next Hop. Default is IPv4.
        """
        return self._get_attribute('nextHopIpType')
    @NextHopIpType.setter
    def NextHopIpType(self, value):
        self._set_attribute('nextHopIpType', value)

    @property
    def NextHopMode(self):
        """
        Returns
        -------
        - str(fixed | incrementPerPeer): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses
        """
        return self._get_attribute('nextHopMode')
    @NextHopMode.setter
    def NextHopMode(self, value):
        self._set_attribute('nextHopMode', value)

    @property
    def Origin(self):
        """
        Returns
        -------
        - str(igp | egp | incomplete): An indication of where the route entry originated
        """
        return self._get_attribute('origin')
    @Origin.setter
    def Origin(self, value):
        self._set_attribute('origin', value)

    @property
    def OriginatorId(self):
        """
        Returns
        -------
        - str: The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        """
        return self._get_attribute('originatorId')
    @OriginatorId.setter
    def OriginatorId(self, value):
        self._set_attribute('originatorId', value)

    @property
    def SetNextHop(self):
        """
        Returns
        -------
        - str(manually | sameAsLocalIp): Indicates now to set the next hop IP address.
        """
        return self._get_attribute('setNextHop')
    @SetNextHop.setter
    def SetNextHop(self, value):
        self._set_attribute('setNextHop', value)

    def update(self, AggregatorAs=None, AggregatorId=None, AsPath=None, AsSetMode=None, Cluster=None, Community=None, EnableAggregator=None, EnableAsPath=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableLocalPref=None, EnableMultiExit=None, EnableNextHop=None, EnableOrigin=None, EnableOriginator=None, ExtendedCommunity=None, LocalPref=None, MultiExit=None, NextHop=None, NextHopIpType=None, NextHopMode=None, Origin=None, OriginatorId=None, SetNextHop=None):
        """Updates cmacRouteAttributes resource on the server.

        Args
        ----
        - AggregatorAs (number): The AS associated with the aggregator router ID in the AGGREGATOR attribute. (default = 0)
        - AggregatorId (str): The IP address of the router that aggregated two or more routes in the AGGREGATOR attribute. (default = 0.0.0.0)
        - AsPath (list(dict(arg1:bool,arg2:str[unknown | asSet | asSequence | asConfedSet | asConfedSequence],arg3:list[number]))): Indicates the local IP address of the BGP router
        - AsSetMode (str(includeAsSeq | includeAsSeqConf | includeAsSet | includeAsSetConf | noInclude | prependAs)): NOT DEFINED
        - Cluster (list(number)): The list of BGP clusters that a particular route has passed through
        - Community (list(number)): The BGP Community attribute to be added to the BGP entry
        - EnableAggregator (bool): Generates an AGGREGATOR attribute using the aggregatorIpAddress, aggregatorASNum, and aggregatorIDMode. (default = false)
        - EnableAsPath (bool): Indicates the local IP address of the BGP router.
        - EnableAtomicAggregate (bool): Sets the attribute bit that indicates that the router has aggregated two or more prefixes in the AGGREGATOR attribute. (default = false)
        - EnableCluster (bool): Enables the generation of the CLUSTER attribute list based on information in clusterList. (default = false)
        - EnableCommunity (bool): Enables the generation of a COMMUNITY attribute list. (default = false)
        - EnableLocalPref (bool): Enables the generation of a LOCAL PREF attribute based on the information in localPref. This value should be set to true only for EBGP. (default = false)
        - EnableMultiExit (bool): Enables the generation of a MULTI EXIT DISCRIMINATOR attribute. (default = false)
        - EnableNextHop (bool): Enables the generation of a NEXT HOP attribute. (default = true)
        - EnableOrigin (bool): Enables the generation of an ORIGIN attribute. (default = true)
        - EnableOriginator (bool): Enables the generation of an ORIGINATOR-ID attribute, based on information in originatorId. (default = false)
        - ExtendedCommunity (list(dict(arg1:str[decimal | hex | ip | ieeeFloat],arg2:str[decimal | hex | ip | ieeeFloat],arg3:str[twoOctetAs | ip | fourOctetAs | opaque | administratorAsTwoOctetLinkBw],arg4:str[routeTarget | origin | extendedBandwidthSubType],arg5:str))): This object is used to construct an extended community attribute for a route item
        - LocalPref (number): The local preference value for the routes with the LOCAL PREF attribute. (default = 0)
        - MultiExit (number): The multi-exit discriminator value in the MULTI EXIT DISCRIMINATOR attribute. (default = 0)
        - NextHop (str): The IP address, in either IPv4 or IPv6 format of the next hop associated with the NEXT HOP attribute. (default = 0.0.0.0)
        - NextHopIpType (str(ipv4 | ipv6)): IP type of Next Hop. Default is IPv4.
        - NextHopMode (str(fixed | incrementPerPeer)): Indicates that the nextHopIpAddress may be incremented for each neighbor session generated for the range of neighbor addresses
        - Origin (str(igp | egp | incomplete)): An indication of where the route entry originated
        - OriginatorId (str): The router that originated a particular route; associated with the ORIGINATOR-ID attribute. (default = 0.0.0.0)
        - SetNextHop (str(manually | sameAsLocalIp)): Indicates now to set the next hop IP address.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
