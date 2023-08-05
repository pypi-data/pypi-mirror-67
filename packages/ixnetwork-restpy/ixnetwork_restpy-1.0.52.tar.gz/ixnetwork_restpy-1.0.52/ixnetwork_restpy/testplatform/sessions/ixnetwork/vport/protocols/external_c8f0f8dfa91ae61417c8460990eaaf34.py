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


class External(Base):
    """
    The External class encapsulates a list of external resources that are managed by the system.
    A list of resources can be retrieved from the server using the External.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'external'

    def __init__(self, parent):
        super(External, self).__init__(parent)

    @property
    def EBit(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('eBit')
    @EBit.setter
    def EBit(self, value):
        self._set_attribute('eBit', value)

    @property
    def ForwardingAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute('forwardingAddress')
    @ForwardingAddress.setter
    def ForwardingAddress(self, value):
        self._set_attribute('forwardingAddress', value)

    @property
    def IncrementLinkStateIdBy(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute('incrementLinkStateIdBy')
    @IncrementLinkStateIdBy.setter
    def IncrementLinkStateIdBy(self, value):
        self._set_attribute('incrementLinkStateIdBy', value)

    @property
    def Metric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute('metric')
    @Metric.setter
    def Metric(self, value):
        self._set_attribute('metric', value)

    @property
    def NetworkMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute('networkMask')
    @NetworkMask.setter
    def NetworkMask(self, value):
        self._set_attribute('networkMask', value)

    @property
    def NumberOfLsa(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute('numberOfLsa')
    @NumberOfLsa.setter
    def NumberOfLsa(self, value):
        self._set_attribute('numberOfLsa', value)

    @property
    def RouteTag(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute('routeTag')
    @RouteTag.setter
    def RouteTag(self, value):
        self._set_attribute('routeTag', value)

    def update(self, EBit=None, ForwardingAddress=None, IncrementLinkStateIdBy=None, Metric=None, NetworkMask=None, NumberOfLsa=None, RouteTag=None):
        """Updates external resource on the server.

        Args
        ----
        - EBit (bool): 
        - ForwardingAddress (str): 
        - IncrementLinkStateIdBy (str): 
        - Metric (number): 
        - NetworkMask (str): 
        - NumberOfLsa (number): 
        - RouteTag (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def find(self, EBit=None, ForwardingAddress=None, IncrementLinkStateIdBy=None, Metric=None, NetworkMask=None, NumberOfLsa=None, RouteTag=None):
        """Finds and retrieves external resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve external resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all external resources from the server.

        Args
        ----
        - EBit (bool): 
        - ForwardingAddress (str): 
        - IncrementLinkStateIdBy (str): 
        - Metric (number): 
        - NetworkMask (str): 
        - NumberOfLsa (number): 
        - RouteTag (str): 

        Returns
        -------
        - self: This instance with matching external resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of external data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the external resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
