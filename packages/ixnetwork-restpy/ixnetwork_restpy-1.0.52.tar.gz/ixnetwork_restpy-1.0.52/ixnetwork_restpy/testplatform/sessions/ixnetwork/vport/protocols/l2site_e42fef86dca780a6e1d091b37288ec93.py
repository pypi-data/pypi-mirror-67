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


class L2Site(Base):
    """Represents a VPN layer 2 site.
    The L2Site class encapsulates a list of l2Site resources that are managed by the user.
    A list of resources can be retrieved from the server using the L2Site.find() method.
    The list can be managed by using the L2Site.add() and L2Site.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'l2Site'

    def __init__(self, parent):
        super(L2Site, self).__init__(parent)

    @property
    def Cluster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_19f4c8ac61fd4025d4ecd9a453c177fc.Cluster): An instance of the Cluster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_19f4c8ac61fd4025d4ecd9a453c177fc import Cluster
        return Cluster(self)._select()

    @property
    def LabelBlock(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelblock_5a0fdae930a00d599b2f7e774b2b2ec9.LabelBlock): An instance of the LabelBlock class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.labelblock_5a0fdae930a00d599b2f7e774b2b2ec9 import LabelBlock
        return LabelBlock(self)

    @property
    def LearnedRoute(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_c62f862792ee836ee06d00a685764f07.LearnedRoute): An instance of the LearnedRoute class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedroute_c62f862792ee836ee06d00a685764f07 import LearnedRoute
        return LearnedRoute(self)

    @property
    def MacAddressRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macaddressrange_ab1c67a792ad7e962a05f33883dd25c7.MacAddressRange): An instance of the MacAddressRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.macaddressrange_ab1c67a792ad7e962a05f33883dd25c7 import MacAddressRange
        return MacAddressRange(self)

    @property
    def DistinguishAssignedIncrement(self):
        """
        Returns
        -------
        - number: Distinguishes increment of the assigned value
        """
        return self._get_attribute('distinguishAssignedIncrement')
    @DistinguishAssignedIncrement.setter
    def DistinguishAssignedIncrement(self, value):
        self._set_attribute('distinguishAssignedIncrement', value)

    @property
    def DistinguishIpIncrement(self):
        """
        Returns
        -------
        - str: Distinguishes the increment of the IP address
        """
        return self._get_attribute('distinguishIpIncrement')
    @DistinguishIpIncrement.setter
    def DistinguishIpIncrement(self, value):
        self._set_attribute('distinguishIpIncrement', value)

    @property
    def DistinguishNumberIncrementAs(self):
        """
        Returns
        -------
        - number: Signifies the distinguished increment as number
        """
        return self._get_attribute('distinguishNumberIncrementAs')
    @DistinguishNumberIncrementAs.setter
    def DistinguishNumberIncrementAs(self, value):
        self._set_attribute('distinguishNumberIncrementAs', value)

    @property
    def EnableBfdVccv(self):
        """
        Returns
        -------
        - bool: If true, enables BFD VCCV
        """
        return self._get_attribute('enableBfdVccv')
    @EnableBfdVccv.setter
    def EnableBfdVccv(self, value):
        self._set_attribute('enableBfdVccv', value)

    @property
    def EnableCluster(self):
        """
        Returns
        -------
        - bool: Enables and controls the use of L2 VPN VPLS.
        """
        return self._get_attribute('enableCluster')
    @EnableCluster.setter
    def EnableCluster(self, value):
        self._set_attribute('enableCluster', value)

    @property
    def EnableControlWord(self):
        """
        Returns
        -------
        - bool: Enables the use of a control word, as part of the extended community information.
        """
        return self._get_attribute('enableControlWord')
    @EnableControlWord.setter
    def EnableControlWord(self, value):
        self._set_attribute('enableControlWord', value)

    @property
    def EnableL2SiteAsTrafficEndpoint(self):
        """
        Returns
        -------
        - bool: If true, enables L2 site as traffic endpoint
        """
        return self._get_attribute('enableL2SiteAsTrafficEndpoint')
    @EnableL2SiteAsTrafficEndpoint.setter
    def EnableL2SiteAsTrafficEndpoint(self, value):
        self._set_attribute('enableL2SiteAsTrafficEndpoint', value)

    @property
    def EnableSequenceDelivery(self):
        """
        Returns
        -------
        - bool: Enables the use of sequenced delivery of frames, as part of the extended community information.
        """
        return self._get_attribute('enableSequenceDelivery')
    @EnableSequenceDelivery.setter
    def EnableSequenceDelivery(self, value):
        self._set_attribute('enableSequenceDelivery', value)

    @property
    def EnableVccvPing(self):
        """
        Returns
        -------
        - bool: If true, enables the VCCV ping
        """
        return self._get_attribute('enableVccvPing')
    @EnableVccvPing.setter
    def EnableVccvPing(self, value):
        self._set_attribute('enableVccvPing', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables use of the L2 VPN site.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def IsLearnedInfoRefreshed(self):
        """
        Returns
        -------
        - bool: If true, learned information is refreshed.
        """
        return self._get_attribute('isLearnedInfoRefreshed')

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        """
        return self._get_attribute('mtu')
    @Mtu.setter
    def Mtu(self, value):
        self._set_attribute('mtu', value)

    @property
    def NoOfL2Site(self):
        """
        Returns
        -------
        - number: Signifies the number of L2 sites
        """
        return self._get_attribute('noOfL2Site')
    @NoOfL2Site.setter
    def NoOfL2Site(self, value):
        self._set_attribute('noOfL2Site', value)

    @property
    def RouteDistinguisherAs(self):
        """
        Returns
        -------
        - number: Available for use only if the route distinguish type is set to AS. The route distinguisher autonomous system (AS) number.
        """
        return self._get_attribute('routeDistinguisherAs')
    @RouteDistinguisherAs.setter
    def RouteDistinguisherAs(self, value):
        self._set_attribute('routeDistinguisherAs', value)

    @property
    def RouteDistinguisherAssignedNum(self):
        """
        Returns
        -------
        - number: The assigned number for use with the distinguisher IP address or AS number, to create the route distinguisher.The default is 0.
        """
        return self._get_attribute('routeDistinguisherAssignedNum')
    @RouteDistinguisherAssignedNum.setter
    def RouteDistinguisherAssignedNum(self, value):
        self._set_attribute('routeDistinguisherAssignedNum', value)

    @property
    def RouteDistinguisherIp(self):
        """
        Returns
        -------
        - str: Available for use only if the route Distinguish Type is set to IP. The route distinguisher IP address. A 4-byte IPv4 address.The default is 0.0.0.0.
        """
        return self._get_attribute('routeDistinguisherIp')
    @RouteDistinguisherIp.setter
    def RouteDistinguisherIp(self, value):
        self._set_attribute('routeDistinguisherIp', value)

    @property
    def RouteDistinguisherType(self):
        """
        Returns
        -------
        - str(twoOctetAs | ip | fourOctetAs): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        """
        return self._get_attribute('routeDistinguisherType')
    @RouteDistinguisherType.setter
    def RouteDistinguisherType(self, value):
        self._set_attribute('routeDistinguisherType', value)

    @property
    def RouteTargetAs(self):
        """
        Returns
        -------
        - number: Autonomous system (AS) number. A 2-byte AS number, used to create the route target extended community attribute associated with this L2 site.
        """
        return self._get_attribute('routeTargetAs')
    @RouteTargetAs.setter
    def RouteTargetAs(self, value):
        self._set_attribute('routeTargetAs', value)

    @property
    def RouteTargetAssignedNum(self):
        """
        Returns
        -------
        - number: Autonomous system (AS) and assigned number. A 2-byte AS number and a 4-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        """
        return self._get_attribute('routeTargetAssignedNum')
    @RouteTargetAssignedNum.setter
    def RouteTargetAssignedNum(self, value):
        self._set_attribute('routeTargetAssignedNum', value)

    @property
    def RouteTargetIp(self):
        """
        Returns
        -------
        - str: IP address and assigned number. A 4-byte IPv4 address and a 2-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        """
        return self._get_attribute('routeTargetIp')
    @RouteTargetIp.setter
    def RouteTargetIp(self, value):
        self._set_attribute('routeTargetIp', value)

    @property
    def RouteTargetType(self):
        """
        Returns
        -------
        - str(as | ip): The Admin part type is to the type of route target attribute
        """
        return self._get_attribute('routeTargetType')
    @RouteTargetType.setter
    def RouteTargetType(self, value):
        self._set_attribute('routeTargetType', value)

    @property
    def SiteId(self):
        """
        Returns
        -------
        - number: The identifier for the L2 (CE) site. The default is 0.
        """
        return self._get_attribute('siteId')
    @SiteId.setter
    def SiteId(self, value):
        self._set_attribute('siteId', value)

    @property
    def SiteIdIncrement(self):
        """
        Returns
        -------
        - number: Increments the site identifier
        """
        return self._get_attribute('siteIdIncrement')
    @SiteIdIncrement.setter
    def SiteIdIncrement(self, value):
        self._set_attribute('siteIdIncrement', value)

    @property
    def TargetAssignedNumberIncrement(self):
        """
        Returns
        -------
        - number: Signifies increment of the target assigned number
        """
        return self._get_attribute('targetAssignedNumberIncrement')
    @TargetAssignedNumberIncrement.setter
    def TargetAssignedNumberIncrement(self, value):
        self._set_attribute('targetAssignedNumberIncrement', value)

    @property
    def TargetIncrementAs(self):
        """
        Returns
        -------
        - number: Signifies increment as target
        """
        return self._get_attribute('targetIncrementAs')
    @TargetIncrementAs.setter
    def TargetIncrementAs(self, value):
        self._set_attribute('targetIncrementAs', value)

    @property
    def TargetIpIncrement(self):
        """
        Returns
        -------
        - str: Signifies the increment of IP as target
        """
        return self._get_attribute('targetIpIncrement')
    @TargetIpIncrement.setter
    def TargetIpIncrement(self, value):
        self._set_attribute('targetIpIncrement', value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
        """
        return self._get_attribute('trafficGroupId')
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute('trafficGroupId', value)

    def update(self, DistinguishAssignedIncrement=None, DistinguishIpIncrement=None, DistinguishNumberIncrementAs=None, EnableBfdVccv=None, EnableCluster=None, EnableControlWord=None, EnableL2SiteAsTrafficEndpoint=None, EnableSequenceDelivery=None, EnableVccvPing=None, Enabled=None, Mtu=None, NoOfL2Site=None, RouteDistinguisherAs=None, RouteDistinguisherAssignedNum=None, RouteDistinguisherIp=None, RouteDistinguisherType=None, RouteTargetAs=None, RouteTargetAssignedNum=None, RouteTargetIp=None, RouteTargetType=None, SiteId=None, SiteIdIncrement=None, TargetAssignedNumberIncrement=None, TargetIncrementAs=None, TargetIpIncrement=None, TrafficGroupId=None):
        """Updates l2Site resource on the server.

        Args
        ----
        - DistinguishAssignedIncrement (number): Distinguishes increment of the assigned value
        - DistinguishIpIncrement (str): Distinguishes the increment of the IP address
        - DistinguishNumberIncrementAs (number): Signifies the distinguished increment as number
        - EnableBfdVccv (bool): If true, enables BFD VCCV
        - EnableCluster (bool): Enables and controls the use of L2 VPN VPLS.
        - EnableControlWord (bool): Enables the use of a control word, as part of the extended community information.
        - EnableL2SiteAsTrafficEndpoint (bool): If true, enables L2 site as traffic endpoint
        - EnableSequenceDelivery (bool): Enables the use of sequenced delivery of frames, as part of the extended community information.
        - EnableVccvPing (bool): If true, enables the VCCV ping
        - Enabled (bool): Enables or disables use of the L2 VPN site.
        - Mtu (number): The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        - NoOfL2Site (number): Signifies the number of L2 sites
        - RouteDistinguisherAs (number): Available for use only if the route distinguish type is set to AS. The route distinguisher autonomous system (AS) number.
        - RouteDistinguisherAssignedNum (number): The assigned number for use with the distinguisher IP address or AS number, to create the route distinguisher.The default is 0.
        - RouteDistinguisherIp (str): Available for use only if the route Distinguish Type is set to IP. The route distinguisher IP address. A 4-byte IPv4 address.The default is 0.0.0.0.
        - RouteDistinguisherType (str(twoOctetAs | ip | fourOctetAs)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - RouteTargetAs (number): Autonomous system (AS) number. A 2-byte AS number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetAssignedNum (number): Autonomous system (AS) and assigned number. A 2-byte AS number and a 4-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetIp (str): IP address and assigned number. A 4-byte IPv4 address and a 2-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetType (str(as | ip)): The Admin part type is to the type of route target attribute
        - SiteId (number): The identifier for the L2 (CE) site. The default is 0.
        - SiteIdIncrement (number): Increments the site identifier
        - TargetAssignedNumberIncrement (number): Signifies increment of the target assigned number
        - TargetIncrementAs (number): Signifies increment as target
        - TargetIpIncrement (str): Signifies the increment of IP as target
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, DistinguishAssignedIncrement=None, DistinguishIpIncrement=None, DistinguishNumberIncrementAs=None, EnableBfdVccv=None, EnableCluster=None, EnableControlWord=None, EnableL2SiteAsTrafficEndpoint=None, EnableSequenceDelivery=None, EnableVccvPing=None, Enabled=None, Mtu=None, NoOfL2Site=None, RouteDistinguisherAs=None, RouteDistinguisherAssignedNum=None, RouteDistinguisherIp=None, RouteDistinguisherType=None, RouteTargetAs=None, RouteTargetAssignedNum=None, RouteTargetIp=None, RouteTargetType=None, SiteId=None, SiteIdIncrement=None, TargetAssignedNumberIncrement=None, TargetIncrementAs=None, TargetIpIncrement=None, TrafficGroupId=None):
        """Adds a new l2Site resource on the server and adds it to the container.

        Args
        ----
        - DistinguishAssignedIncrement (number): Distinguishes increment of the assigned value
        - DistinguishIpIncrement (str): Distinguishes the increment of the IP address
        - DistinguishNumberIncrementAs (number): Signifies the distinguished increment as number
        - EnableBfdVccv (bool): If true, enables BFD VCCV
        - EnableCluster (bool): Enables and controls the use of L2 VPN VPLS.
        - EnableControlWord (bool): Enables the use of a control word, as part of the extended community information.
        - EnableL2SiteAsTrafficEndpoint (bool): If true, enables L2 site as traffic endpoint
        - EnableSequenceDelivery (bool): Enables the use of sequenced delivery of frames, as part of the extended community information.
        - EnableVccvPing (bool): If true, enables the VCCV ping
        - Enabled (bool): Enables or disables use of the L2 VPN site.
        - Mtu (number): The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        - NoOfL2Site (number): Signifies the number of L2 sites
        - RouteDistinguisherAs (number): Available for use only if the route distinguish type is set to AS. The route distinguisher autonomous system (AS) number.
        - RouteDistinguisherAssignedNum (number): The assigned number for use with the distinguisher IP address or AS number, to create the route distinguisher.The default is 0.
        - RouteDistinguisherIp (str): Available for use only if the route Distinguish Type is set to IP. The route distinguisher IP address. A 4-byte IPv4 address.The default is 0.0.0.0.
        - RouteDistinguisherType (str(twoOctetAs | ip | fourOctetAs)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - RouteTargetAs (number): Autonomous system (AS) number. A 2-byte AS number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetAssignedNum (number): Autonomous system (AS) and assigned number. A 2-byte AS number and a 4-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetIp (str): IP address and assigned number. A 4-byte IPv4 address and a 2-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetType (str(as | ip)): The Admin part type is to the type of route target attribute
        - SiteId (number): The identifier for the L2 (CE) site. The default is 0.
        - SiteIdIncrement (number): Increments the site identifier
        - TargetAssignedNumberIncrement (number): Signifies increment of the target assigned number
        - TargetIncrementAs (number): Signifies increment as target
        - TargetIpIncrement (str): Signifies the increment of IP as target
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.

        Returns
        -------
        - self: This instance with all currently retrieved l2Site resources using find and the newly added l2Site resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained l2Site resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DistinguishAssignedIncrement=None, DistinguishIpIncrement=None, DistinguishNumberIncrementAs=None, EnableBfdVccv=None, EnableCluster=None, EnableControlWord=None, EnableL2SiteAsTrafficEndpoint=None, EnableSequenceDelivery=None, EnableVccvPing=None, Enabled=None, IsLearnedInfoRefreshed=None, Mtu=None, NoOfL2Site=None, RouteDistinguisherAs=None, RouteDistinguisherAssignedNum=None, RouteDistinguisherIp=None, RouteDistinguisherType=None, RouteTargetAs=None, RouteTargetAssignedNum=None, RouteTargetIp=None, RouteTargetType=None, SiteId=None, SiteIdIncrement=None, TargetAssignedNumberIncrement=None, TargetIncrementAs=None, TargetIpIncrement=None, TrafficGroupId=None):
        """Finds and retrieves l2Site resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l2Site resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l2Site resources from the server.

        Args
        ----
        - DistinguishAssignedIncrement (number): Distinguishes increment of the assigned value
        - DistinguishIpIncrement (str): Distinguishes the increment of the IP address
        - DistinguishNumberIncrementAs (number): Signifies the distinguished increment as number
        - EnableBfdVccv (bool): If true, enables BFD VCCV
        - EnableCluster (bool): Enables and controls the use of L2 VPN VPLS.
        - EnableControlWord (bool): Enables the use of a control word, as part of the extended community information.
        - EnableL2SiteAsTrafficEndpoint (bool): If true, enables L2 site as traffic endpoint
        - EnableSequenceDelivery (bool): Enables the use of sequenced delivery of frames, as part of the extended community information.
        - EnableVccvPing (bool): If true, enables the VCCV ping
        - Enabled (bool): Enables or disables use of the L2 VPN site.
        - IsLearnedInfoRefreshed (bool): If true, learned information is refreshed.
        - Mtu (number): The Maximum Transmission Unit (MTU) allowed on this link, in bytes. The valid range is 0 to 16777215. (default = 1,500 bytes)
        - NoOfL2Site (number): Signifies the number of L2 sites
        - RouteDistinguisherAs (number): Available for use only if the route distinguish type is set to AS. The route distinguisher autonomous system (AS) number.
        - RouteDistinguisherAssignedNum (number): The assigned number for use with the distinguisher IP address or AS number, to create the route distinguisher.The default is 0.
        - RouteDistinguisherIp (str): Available for use only if the route Distinguish Type is set to IP. The route distinguisher IP address. A 4-byte IPv4 address.The default is 0.0.0.0.
        - RouteDistinguisherType (str(twoOctetAs | ip | fourOctetAs)): Indicates the type of administrator field used in route distinguisher that will be included in the route announcements.
        - RouteTargetAs (number): Autonomous system (AS) number. A 2-byte AS number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetAssignedNum (number): Autonomous system (AS) and assigned number. A 2-byte AS number and a 4-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetIp (str): IP address and assigned number. A 4-byte IPv4 address and a 2-byte assigned number, used to create the route target extended community attribute associated with this L2 site.
        - RouteTargetType (str(as | ip)): The Admin part type is to the type of route target attribute
        - SiteId (number): The identifier for the L2 (CE) site. The default is 0.
        - SiteIdIncrement (number): Increments the site identifier
        - TargetAssignedNumberIncrement (number): Signifies increment of the target assigned number
        - TargetIncrementAs (number): Signifies increment as target
        - TargetIpIncrement (str): Signifies the increment of IP as target
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.

        Returns
        -------
        - self: This instance with matching l2Site resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of l2Site data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l2Site resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def RefreshLearnedInfo(self):
        """Executes the refreshLearnedInfo operation on the server.

        This function argument allows to refreshe the BGP learned information from the DUT.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshLearnedInfo', payload=payload, response_object=None)
