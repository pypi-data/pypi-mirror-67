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


class FramePreemption(Base):
    """
    The FramePreemption class encapsulates a required framePreemption resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'framePreemption'

    def __init__(self, parent):
        super(FramePreemption, self).__init__(parent)

    @property
    def AutoFragmentCount(self):
        """
        Returns
        -------
        - bool: Let the fragments be auto counted
        """
        return self._get_attribute('autoFragmentCount')
    @AutoFragmentCount.setter
    def AutoFragmentCount(self, value):
        self._set_attribute('autoFragmentCount', value)

    @property
    def Enable(self):
        """
        Returns
        -------
        - bool: Enable frame preemption on the given stream. Disabled indicates an express frame
        """
        return self._get_attribute('enable')
    @Enable.setter
    def Enable(self, value):
        self._set_attribute('enable', value)

    @property
    def FragmentCount(self):
        """
        Returns
        -------
        - number: Set the fragment count (a value between 0 and 3)
        """
        return self._get_attribute('fragmentCount')
    @FragmentCount.setter
    def FragmentCount(self, value):
        self._set_attribute('fragmentCount', value)

    @property
    def FrameType(self):
        """
        Returns
        -------
        - str(control | fragment | invalid | wholeFrame): Select the frame type
        """
        return self._get_attribute('frameType')
    @FrameType.setter
    def FrameType(self, value):
        self._set_attribute('frameType', value)

    @property
    def LastFragment(self):
        """
        Returns
        -------
        - bool: Indicates if this is the last fragment of the preemptable packet
        """
        return self._get_attribute('lastFragment')
    @LastFragment.setter
    def LastFragment(self, value):
        self._set_attribute('lastFragment', value)

    @property
    def SmdType(self):
        """
        Returns
        -------
        - str(autoSMDC | autoSMDS | invalidSMD | smdC0 | smdC1 | smdC2 | smdC3 | smdE | smdR | smdS0 | smdS1 | smdS2 | smdS3 | smdV): Select the SMD type
        """
        return self._get_attribute('smdType')
    @SmdType.setter
    def SmdType(self, value):
        self._set_attribute('smdType', value)

    def update(self, AutoFragmentCount=None, Enable=None, FragmentCount=None, FrameType=None, LastFragment=None, SmdType=None):
        """Updates framePreemption resource on the server.

        Args
        ----
        - AutoFragmentCount (bool): Let the fragments be auto counted
        - Enable (bool): Enable frame preemption on the given stream. Disabled indicates an express frame
        - FragmentCount (number): Set the fragment count (a value between 0 and 3)
        - FrameType (str(control | fragment | invalid | wholeFrame)): Select the frame type
        - LastFragment (bool): Indicates if this is the last fragment of the preemptable packet
        - SmdType (str(autoSMDC | autoSMDS | invalidSMD | smdC0 | smdC1 | smdC2 | smdC3 | smdE | smdR | smdS0 | smdS1 | smdS2 | smdS3 | smdV)): Select the SMD type

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
