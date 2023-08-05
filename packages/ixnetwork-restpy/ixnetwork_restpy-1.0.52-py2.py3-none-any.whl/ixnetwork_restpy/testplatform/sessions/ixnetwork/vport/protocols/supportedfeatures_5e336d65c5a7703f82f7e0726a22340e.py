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


class SupportedFeatures(Base):
    """An object that allows to select the features (link modes, link types, and link features) from the list that will be supported by the port.
    The SupportedFeatures class encapsulates a required supportedFeatures resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'supportedFeatures'

    def __init__(self, parent):
        super(SupportedFeatures, self).__init__(parent)

    @property
    def HundredGbFd(self):
        """
        Returns
        -------
        - bool: If selected, 100 GB full-duplex rate support is available.
        """
        return self._get_attribute('100GbFd')
    @HundredGbFd.setter
    def HundredGbFd(self, value):
        self._set_attribute('100GbFd', value)

    @property
    def HundredMbFd(self):
        """
        Returns
        -------
        - bool: If selected, 100 MB full-duplex rate support is available.
        """
        return self._get_attribute('100MbFd')
    @HundredMbFd.setter
    def HundredMbFd(self, value):
        self._set_attribute('100MbFd', value)

    @property
    def HundredMbHd(self):
        """
        Returns
        -------
        - bool: If selected, 100 MB half-duplex rate support is available.
        """
        return self._get_attribute('100MbHd')
    @HundredMbHd.setter
    def HundredMbHd(self, value):
        self._set_attribute('100MbHd', value)

    @property
    def TenGbFd(self):
        """
        Returns
        -------
        - bool: If selected, 10 GB full-duplex rate support is available.
        """
        return self._get_attribute('10GbFd')
    @TenGbFd.setter
    def TenGbFd(self, value):
        self._set_attribute('10GbFd', value)

    @property
    def TenMbFd(self):
        """
        Returns
        -------
        - bool: If selected, 10 MB full-duplex rate support is available.
        """
        return self._get_attribute('10MbFd')
    @TenMbFd.setter
    def TenMbFd(self, value):
        self._set_attribute('10MbFd', value)

    @property
    def TenMbHd(self):
        """
        Returns
        -------
        - bool: If selected, 10 MB half-duplex rate support is available.
        """
        return self._get_attribute('10MbHd')
    @TenMbHd.setter
    def TenMbHd(self, value):
        self._set_attribute('10MbHd', value)

    @property
    def OneGbFd(self):
        """
        Returns
        -------
        - bool: If selected, 1 GB full-duplex rate support is available.
        """
        return self._get_attribute('1GbFd')
    @OneGbFd.setter
    def OneGbFd(self, value):
        self._set_attribute('1GbFd', value)

    @property
    def OneGbHd(self):
        """
        Returns
        -------
        - bool: If selected, 1 GB half-duplex rate support is available.
        """
        return self._get_attribute('1GbHd')
    @OneGbHd.setter
    def OneGbHd(self, value):
        self._set_attribute('1GbHd', value)

    @property
    def OneTbFd(self):
        """
        Returns
        -------
        - bool: If selected, 1 TB full-duplex rate support is available.
        """
        return self._get_attribute('1TbFd')
    @OneTbFd.setter
    def OneTbFd(self, value):
        self._set_attribute('1TbFd', value)

    @property
    def FortyGbFd(self):
        """
        Returns
        -------
        - bool: If selected, 40 GB full-duplex rate support is available.
        """
        return self._get_attribute('40GbFd')
    @FortyGbFd.setter
    def FortyGbFd(self, value):
        self._set_attribute('40GbFd', value)

    @property
    def AsymmetricPause(self):
        """
        Returns
        -------
        - bool: If selected, asymmetric pause of ports feature is available.
        """
        return self._get_attribute('asymmetricPause')
    @AsymmetricPause.setter
    def AsymmetricPause(self, value):
        self._set_attribute('asymmetricPause', value)

    @property
    def AutoNegotiation(self):
        """
        Returns
        -------
        - bool: If selected, auto negotiation of ports is available.
        """
        return self._get_attribute('autoNegotiation')
    @AutoNegotiation.setter
    def AutoNegotiation(self, value):
        self._set_attribute('autoNegotiation', value)

    @property
    def CopperMedium(self):
        """
        Returns
        -------
        - bool: If selected, copper medium link type is available.
        """
        return self._get_attribute('copperMedium')
    @CopperMedium.setter
    def CopperMedium(self, value):
        self._set_attribute('copperMedium', value)

    @property
    def FiberMedium(self):
        """
        Returns
        -------
        - bool: If selected, fiber medium link type is available.
        """
        return self._get_attribute('fiberMedium')
    @FiberMedium.setter
    def FiberMedium(self, value):
        self._set_attribute('fiberMedium', value)

    @property
    def OtherRate(self):
        """
        Returns
        -------
        - bool: If true, supports other rate, not in the list.
        """
        return self._get_attribute('otherRate')
    @OtherRate.setter
    def OtherRate(self, value):
        self._set_attribute('otherRate', value)

    @property
    def Pause(self):
        """
        Returns
        -------
        - bool: If selected, pause ports feature is available.
        """
        return self._get_attribute('pause')
    @Pause.setter
    def Pause(self, value):
        self._set_attribute('pause', value)

    def update(self, HundredGbFd=None, HundredMbFd=None, HundredMbHd=None, TenGbFd=None, TenMbFd=None, TenMbHd=None, OneGbFd=None, OneGbHd=None, OneTbFd=None, FortyGbFd=None, AsymmetricPause=None, AutoNegotiation=None, CopperMedium=None, FiberMedium=None, OtherRate=None, Pause=None):
        """Updates supportedFeatures resource on the server.

        Args
        ----
        - HundredGbFd (bool): If selected, 100 GB full-duplex rate support is available.
        - HundredMbFd (bool): If selected, 100 MB full-duplex rate support is available.
        - HundredMbHd (bool): If selected, 100 MB half-duplex rate support is available.
        - TenGbFd (bool): If selected, 10 GB full-duplex rate support is available.
        - TenMbFd (bool): If selected, 10 MB full-duplex rate support is available.
        - TenMbHd (bool): If selected, 10 MB half-duplex rate support is available.
        - OneGbFd (bool): If selected, 1 GB full-duplex rate support is available.
        - OneGbHd (bool): If selected, 1 GB half-duplex rate support is available.
        - OneTbFd (bool): If selected, 1 TB full-duplex rate support is available.
        - FortyGbFd (bool): If selected, 40 GB full-duplex rate support is available.
        - AsymmetricPause (bool): If selected, asymmetric pause of ports feature is available.
        - AutoNegotiation (bool): If selected, auto negotiation of ports is available.
        - CopperMedium (bool): If selected, copper medium link type is available.
        - FiberMedium (bool): If selected, fiber medium link type is available.
        - OtherRate (bool): If true, supports other rate, not in the list.
        - Pause (bool): If selected, pause ports feature is available.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
