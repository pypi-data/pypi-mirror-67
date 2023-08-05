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


class BwProfile(Base):
    """Bandwidth profile for the EVC.
    The BwProfile class encapsulates a list of bwProfile resources that are managed by the user.
    A list of resources can be retrieved from the server using the BwProfile.find() method.
    The list can be managed by using the BwProfile.add() and BwProfile.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'bwProfile'

    def __init__(self, parent):
        super(BwProfile, self).__init__(parent)

    @property
    def CbsMagnitude(self):
        """
        Returns
        -------
        - number: It signifies one octet field. Default is 1.
        """
        return self._get_attribute('cbsMagnitude')
    @CbsMagnitude.setter
    def CbsMagnitude(self, value):
        self._set_attribute('cbsMagnitude', value)

    @property
    def CbsMultiplier(self):
        """
        Returns
        -------
        - number: It signifies one octet field. Default is 1.
        """
        return self._get_attribute('cbsMultiplier')
    @CbsMultiplier.setter
    def CbsMultiplier(self, value):
        self._set_attribute('cbsMultiplier', value)

    @property
    def Cf(self):
        """
        Returns
        -------
        - bool: If enabled, Coupling Flag is set to 1. Default is 0.
        """
        return self._get_attribute('cf')
    @Cf.setter
    def Cf(self, value):
        self._set_attribute('cf', value)

    @property
    def CirMagnitude(self):
        """
        Returns
        -------
        - number: It signifies one octet field. Default is 1.
        """
        return self._get_attribute('cirMagnitude')
    @CirMagnitude.setter
    def CirMagnitude(self, value):
        self._set_attribute('cirMagnitude', value)

    @property
    def CirMultiplier(self):
        """
        Returns
        -------
        - number: It signifies two octet field. Default is 1.
        """
        return self._get_attribute('cirMultiplier')
    @CirMultiplier.setter
    def CirMultiplier(self, value):
        self._set_attribute('cirMultiplier', value)

    @property
    def Cm(self):
        """
        Returns
        -------
        - bool: If enabled, Colored Mode Flag is 1. Default is false.
        """
        return self._get_attribute('cm')
    @Cm.setter
    def Cm(self, value):
        self._set_attribute('cm', value)

    @property
    def EbsMagnitude(self):
        """
        Returns
        -------
        - number: It signifies one octet field. Default is 1.
        """
        return self._get_attribute('ebsMagnitude')
    @EbsMagnitude.setter
    def EbsMagnitude(self, value):
        self._set_attribute('ebsMagnitude', value)

    @property
    def EbsMultiplier(self):
        """
        Returns
        -------
        - number: It signifies one octet field. Default is 1.
        """
        return self._get_attribute('ebsMultiplier')
    @EbsMultiplier.setter
    def EbsMultiplier(self, value):
        self._set_attribute('ebsMultiplier', value)

    @property
    def EirMagnitude(self):
        """
        Returns
        -------
        - number: It signifies one octet field. Default is 1.
        """
        return self._get_attribute('eirMagnitude')
    @EirMagnitude.setter
    def EirMagnitude(self, value):
        self._set_attribute('eirMagnitude', value)

    @property
    def EirMultiplier(self):
        """
        Returns
        -------
        - number: It signifies two octet field. Default is 1.
        """
        return self._get_attribute('eirMultiplier')
    @EirMultiplier.setter
    def EirMultiplier(self, value):
        self._set_attribute('eirMultiplier', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If enabled, bandwidth profile is in effect for the EVC.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def PerCos(self):
        """
        Returns
        -------
        - bool: If enabled, Per CoS Flag shows user_priority bit values as significant and the value is set to 1. If the value is set to 0, the user_priority bit values as ignored and not processed. Default is 0.
        """
        return self._get_attribute('perCos')
    @PerCos.setter
    def PerCos(self, value):
        self._set_attribute('perCos', value)

    @property
    def UserPriorityBits000(self):
        """
        Returns
        -------
        - bool: If enabled, Bandwidth Profile applies to frames with user_priority as 000 and the value is set to 1. Default is 0.
        """
        return self._get_attribute('userPriorityBits000')
    @UserPriorityBits000.setter
    def UserPriorityBits000(self, value):
        self._set_attribute('userPriorityBits000', value)

    @property
    def UserPriorityBits001(self):
        """
        Returns
        -------
        - bool: If enabled, Bandwidth Profile applies to frames with user_priority as 001 and the value is set to 1. Default is 0.
        """
        return self._get_attribute('userPriorityBits001')
    @UserPriorityBits001.setter
    def UserPriorityBits001(self, value):
        self._set_attribute('userPriorityBits001', value)

    @property
    def UserPriorityBits010(self):
        """
        Returns
        -------
        - bool: If enabled, Bandwidth Profile applies to frames with user_priority as 010 and the value is set to 1. Default is 0.
        """
        return self._get_attribute('userPriorityBits010')
    @UserPriorityBits010.setter
    def UserPriorityBits010(self, value):
        self._set_attribute('userPriorityBits010', value)

    @property
    def UserPriorityBits011(self):
        """
        Returns
        -------
        - bool: If enabled, Bandwidth Profile applies to frames with user_priority as 011 and the value is set to 1. Default is 0.
        """
        return self._get_attribute('userPriorityBits011')
    @UserPriorityBits011.setter
    def UserPriorityBits011(self, value):
        self._set_attribute('userPriorityBits011', value)

    @property
    def UserPriorityBits100(self):
        """
        Returns
        -------
        - bool: If enabled, Bandwidth Profile applies to frames with user_priority as 100 and the value is set to 1. Default is 0.
        """
        return self._get_attribute('userPriorityBits100')
    @UserPriorityBits100.setter
    def UserPriorityBits100(self, value):
        self._set_attribute('userPriorityBits100', value)

    @property
    def UserPriorityBits101(self):
        """
        Returns
        -------
        - bool: If enabled, Bandwidth Profile applies to frames with user_priority as 101 and the value is set to 1. Default is 0.
        """
        return self._get_attribute('userPriorityBits101')
    @UserPriorityBits101.setter
    def UserPriorityBits101(self, value):
        self._set_attribute('userPriorityBits101', value)

    @property
    def UserPriorityBits110(self):
        """
        Returns
        -------
        - bool: If enabled, Bandwidth Profile applies to frames with user_priority as 110 and the value is set to 1. Default is 0.
        """
        return self._get_attribute('userPriorityBits110')
    @UserPriorityBits110.setter
    def UserPriorityBits110(self, value):
        self._set_attribute('userPriorityBits110', value)

    @property
    def UserPriorityBits111(self):
        """
        Returns
        -------
        - bool: If enabled, Bandwidth Profile applies to frames with user_priority as 111 and the value is set to 1. Default is 0.
        """
        return self._get_attribute('userPriorityBits111')
    @UserPriorityBits111.setter
    def UserPriorityBits111(self, value):
        self._set_attribute('userPriorityBits111', value)

    def update(self, CbsMagnitude=None, CbsMultiplier=None, Cf=None, CirMagnitude=None, CirMultiplier=None, Cm=None, EbsMagnitude=None, EbsMultiplier=None, EirMagnitude=None, EirMultiplier=None, Enabled=None, PerCos=None, UserPriorityBits000=None, UserPriorityBits001=None, UserPriorityBits010=None, UserPriorityBits011=None, UserPriorityBits100=None, UserPriorityBits101=None, UserPriorityBits110=None, UserPriorityBits111=None):
        """Updates bwProfile resource on the server.

        Args
        ----
        - CbsMagnitude (number): It signifies one octet field. Default is 1.
        - CbsMultiplier (number): It signifies one octet field. Default is 1.
        - Cf (bool): If enabled, Coupling Flag is set to 1. Default is 0.
        - CirMagnitude (number): It signifies one octet field. Default is 1.
        - CirMultiplier (number): It signifies two octet field. Default is 1.
        - Cm (bool): If enabled, Colored Mode Flag is 1. Default is false.
        - EbsMagnitude (number): It signifies one octet field. Default is 1.
        - EbsMultiplier (number): It signifies one octet field. Default is 1.
        - EirMagnitude (number): It signifies one octet field. Default is 1.
        - EirMultiplier (number): It signifies two octet field. Default is 1.
        - Enabled (bool): If enabled, bandwidth profile is in effect for the EVC.
        - PerCos (bool): If enabled, Per CoS Flag shows user_priority bit values as significant and the value is set to 1. If the value is set to 0, the user_priority bit values as ignored and not processed. Default is 0.
        - UserPriorityBits000 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 000 and the value is set to 1. Default is 0.
        - UserPriorityBits001 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 001 and the value is set to 1. Default is 0.
        - UserPriorityBits010 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 010 and the value is set to 1. Default is 0.
        - UserPriorityBits011 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 011 and the value is set to 1. Default is 0.
        - UserPriorityBits100 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 100 and the value is set to 1. Default is 0.
        - UserPriorityBits101 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 101 and the value is set to 1. Default is 0.
        - UserPriorityBits110 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 110 and the value is set to 1. Default is 0.
        - UserPriorityBits111 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 111 and the value is set to 1. Default is 0.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, CbsMagnitude=None, CbsMultiplier=None, Cf=None, CirMagnitude=None, CirMultiplier=None, Cm=None, EbsMagnitude=None, EbsMultiplier=None, EirMagnitude=None, EirMultiplier=None, Enabled=None, PerCos=None, UserPriorityBits000=None, UserPriorityBits001=None, UserPriorityBits010=None, UserPriorityBits011=None, UserPriorityBits100=None, UserPriorityBits101=None, UserPriorityBits110=None, UserPriorityBits111=None):
        """Adds a new bwProfile resource on the server and adds it to the container.

        Args
        ----
        - CbsMagnitude (number): It signifies one octet field. Default is 1.
        - CbsMultiplier (number): It signifies one octet field. Default is 1.
        - Cf (bool): If enabled, Coupling Flag is set to 1. Default is 0.
        - CirMagnitude (number): It signifies one octet field. Default is 1.
        - CirMultiplier (number): It signifies two octet field. Default is 1.
        - Cm (bool): If enabled, Colored Mode Flag is 1. Default is false.
        - EbsMagnitude (number): It signifies one octet field. Default is 1.
        - EbsMultiplier (number): It signifies one octet field. Default is 1.
        - EirMagnitude (number): It signifies one octet field. Default is 1.
        - EirMultiplier (number): It signifies two octet field. Default is 1.
        - Enabled (bool): If enabled, bandwidth profile is in effect for the EVC.
        - PerCos (bool): If enabled, Per CoS Flag shows user_priority bit values as significant and the value is set to 1. If the value is set to 0, the user_priority bit values as ignored and not processed. Default is 0.
        - UserPriorityBits000 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 000 and the value is set to 1. Default is 0.
        - UserPriorityBits001 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 001 and the value is set to 1. Default is 0.
        - UserPriorityBits010 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 010 and the value is set to 1. Default is 0.
        - UserPriorityBits011 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 011 and the value is set to 1. Default is 0.
        - UserPriorityBits100 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 100 and the value is set to 1. Default is 0.
        - UserPriorityBits101 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 101 and the value is set to 1. Default is 0.
        - UserPriorityBits110 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 110 and the value is set to 1. Default is 0.
        - UserPriorityBits111 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 111 and the value is set to 1. Default is 0.

        Returns
        -------
        - self: This instance with all currently retrieved bwProfile resources using find and the newly added bwProfile resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained bwProfile resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CbsMagnitude=None, CbsMultiplier=None, Cf=None, CirMagnitude=None, CirMultiplier=None, Cm=None, EbsMagnitude=None, EbsMultiplier=None, EirMagnitude=None, EirMultiplier=None, Enabled=None, PerCos=None, UserPriorityBits000=None, UserPriorityBits001=None, UserPriorityBits010=None, UserPriorityBits011=None, UserPriorityBits100=None, UserPriorityBits101=None, UserPriorityBits110=None, UserPriorityBits111=None):
        """Finds and retrieves bwProfile resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve bwProfile resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all bwProfile resources from the server.

        Args
        ----
        - CbsMagnitude (number): It signifies one octet field. Default is 1.
        - CbsMultiplier (number): It signifies one octet field. Default is 1.
        - Cf (bool): If enabled, Coupling Flag is set to 1. Default is 0.
        - CirMagnitude (number): It signifies one octet field. Default is 1.
        - CirMultiplier (number): It signifies two octet field. Default is 1.
        - Cm (bool): If enabled, Colored Mode Flag is 1. Default is false.
        - EbsMagnitude (number): It signifies one octet field. Default is 1.
        - EbsMultiplier (number): It signifies one octet field. Default is 1.
        - EirMagnitude (number): It signifies one octet field. Default is 1.
        - EirMultiplier (number): It signifies two octet field. Default is 1.
        - Enabled (bool): If enabled, bandwidth profile is in effect for the EVC.
        - PerCos (bool): If enabled, Per CoS Flag shows user_priority bit values as significant and the value is set to 1. If the value is set to 0, the user_priority bit values as ignored and not processed. Default is 0.
        - UserPriorityBits000 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 000 and the value is set to 1. Default is 0.
        - UserPriorityBits001 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 001 and the value is set to 1. Default is 0.
        - UserPriorityBits010 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 010 and the value is set to 1. Default is 0.
        - UserPriorityBits011 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 011 and the value is set to 1. Default is 0.
        - UserPriorityBits100 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 100 and the value is set to 1. Default is 0.
        - UserPriorityBits101 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 101 and the value is set to 1. Default is 0.
        - UserPriorityBits110 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 110 and the value is set to 1. Default is 0.
        - UserPriorityBits111 (bool): If enabled, Bandwidth Profile applies to frames with user_priority as 111 and the value is set to 1. Default is 0.

        Returns
        -------
        - self: This instance with matching bwProfile resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of bwProfile data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the bwProfile resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
