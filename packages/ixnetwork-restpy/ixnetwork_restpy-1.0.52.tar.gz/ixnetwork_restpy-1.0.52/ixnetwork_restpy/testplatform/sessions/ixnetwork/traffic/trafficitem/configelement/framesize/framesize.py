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


class FrameSize(Base):
    """This object provides different options for the Frame Size.
    The FrameSize class encapsulates a required frameSize resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'frameSize'

    def __init__(self, parent):
        super(FrameSize, self).__init__(parent)

    @property
    def FixedSize(self):
        """
        Returns
        -------
        - number: Sets all frames to a constant specified size.
        """
        return self._get_attribute('fixedSize')
    @FixedSize.setter
    def FixedSize(self, value):
        self._set_attribute('fixedSize', value)

    @property
    def IncrementFrom(self):
        """
        Returns
        -------
        - number: Specifies the Start Value if the Frame Size is incremented.
        """
        return self._get_attribute('incrementFrom')
    @IncrementFrom.setter
    def IncrementFrom(self, value):
        self._set_attribute('incrementFrom', value)

    @property
    def IncrementStep(self):
        """
        Returns
        -------
        - number: Specifies the Step Value if the Frame Size is Increment.
        """
        return self._get_attribute('incrementStep')
    @IncrementStep.setter
    def IncrementStep(self, value):
        self._set_attribute('incrementStep', value)

    @property
    def IncrementTo(self):
        """
        Returns
        -------
        - number: Specifies the Final Value if the Frame Size is Increment.
        """
        return self._get_attribute('incrementTo')
    @IncrementTo.setter
    def IncrementTo(self, value):
        self._set_attribute('incrementTo', value)

    @property
    def PresetDistribution(self):
        """
        Returns
        -------
        - str(cisco | imix | ipSecImix | ipV6Imix | rprQuar | rprTri | standardImix | tcpImix | tolly): If set, Frame Size is set to IMIX.
        """
        return self._get_attribute('presetDistribution')
    @PresetDistribution.setter
    def PresetDistribution(self, value):
        self._set_attribute('presetDistribution', value)

    @property
    def QuadGaussian(self):
        """
        Returns
        -------
        - list(number): This option allows to set frames to use a calculated distribution of Frame sizes. Quad Gaussian is the superposition of four Gaussian distributions. The user can specify the center (or mean), width of half maximum, and weight of each Gaussian distribution. The distribution is then normalized to a single distribution and generates the random numbers according to the normalized distribution.
        """
        return self._get_attribute('quadGaussian')
    @QuadGaussian.setter
    def QuadGaussian(self, value):
        self._set_attribute('quadGaussian', value)

    @property
    def RandomMax(self):
        """
        Returns
        -------
        - number: Sets frame size to maximum length in bytes. The maximum length is 65536 bytes.
        """
        return self._get_attribute('randomMax')
    @RandomMax.setter
    def RandomMax(self, value):
        self._set_attribute('randomMax', value)

    @property
    def RandomMin(self):
        """
        Returns
        -------
        - number: Sets frame size to minimum length in bytes. The minimum length is 12 bytes.
        """
        return self._get_attribute('randomMin')
    @RandomMin.setter
    def RandomMin(self, value):
        self._set_attribute('randomMin', value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(auto | fixed | increment | presetDistribution | quadGaussian | random | weightedPairs): Sets the type of Frame Size.
        """
        return self._get_attribute('type')
    @Type.setter
    def Type(self, value):
        self._set_attribute('type', value)

    @property
    def WeightedPairs(self):
        """
        Returns
        -------
        - list(number): Defines the values for the weight pairs.
        """
        return self._get_attribute('weightedPairs')
    @WeightedPairs.setter
    def WeightedPairs(self, value):
        self._set_attribute('weightedPairs', value)

    @property
    def WeightedRangePairs(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:number)): A list of structures that define the weighted range.
        """
        return self._get_attribute('weightedRangePairs')
    @WeightedRangePairs.setter
    def WeightedRangePairs(self, value):
        self._set_attribute('weightedRangePairs', value)

    def update(self, FixedSize=None, IncrementFrom=None, IncrementStep=None, IncrementTo=None, PresetDistribution=None, QuadGaussian=None, RandomMax=None, RandomMin=None, Type=None, WeightedPairs=None, WeightedRangePairs=None):
        """Updates frameSize resource on the server.

        Args
        ----
        - FixedSize (number): Sets all frames to a constant specified size.
        - IncrementFrom (number): Specifies the Start Value if the Frame Size is incremented.
        - IncrementStep (number): Specifies the Step Value if the Frame Size is Increment.
        - IncrementTo (number): Specifies the Final Value if the Frame Size is Increment.
        - PresetDistribution (str(cisco | imix | ipSecImix | ipV6Imix | rprQuar | rprTri | standardImix | tcpImix | tolly)): If set, Frame Size is set to IMIX.
        - QuadGaussian (list(number)): This option allows to set frames to use a calculated distribution of Frame sizes. Quad Gaussian is the superposition of four Gaussian distributions. The user can specify the center (or mean), width of half maximum, and weight of each Gaussian distribution. The distribution is then normalized to a single distribution and generates the random numbers according to the normalized distribution.
        - RandomMax (number): Sets frame size to maximum length in bytes. The maximum length is 65536 bytes.
        - RandomMin (number): Sets frame size to minimum length in bytes. The minimum length is 12 bytes.
        - Type (str(auto | fixed | increment | presetDistribution | quadGaussian | random | weightedPairs)): Sets the type of Frame Size.
        - WeightedPairs (list(number)): Defines the values for the weight pairs.
        - WeightedRangePairs (list(dict(arg1:number,arg2:number,arg3:number))): A list of structures that define the weighted range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
