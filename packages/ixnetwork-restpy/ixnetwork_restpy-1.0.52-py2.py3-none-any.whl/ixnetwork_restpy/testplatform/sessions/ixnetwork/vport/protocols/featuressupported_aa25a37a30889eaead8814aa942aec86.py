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


class FeaturesSupported(Base):
    """Select the table feature properties to enable them. These describe various capabilities of the table.
    The FeaturesSupported class encapsulates a required featuresSupported resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'featuresSupported'

    def __init__(self, parent):
        super(FeaturesSupported, self).__init__(parent)

    @property
    def ApplyActions(self):
        """
        Returns
        -------
        - bool: Select the type of apply action capability that the table will support. The selected actions associated with a flow are applied immediately.
        """
        return self._get_attribute('applyActions')
    @ApplyActions.setter
    def ApplyActions(self, value):
        self._set_attribute('applyActions', value)

    @property
    def ApplyActionsMiss(self):
        """
        Returns
        -------
        - bool: Select the type of apply action miss capability that the table miss flow entry will support.
        """
        return self._get_attribute('applyActionsMiss')
    @ApplyActionsMiss.setter
    def ApplyActionsMiss(self, value):
        self._set_attribute('applyActionsMiss', value)

    @property
    def ApplySetField(self):
        """
        Returns
        -------
        - bool: Apply set field property.
        """
        return self._get_attribute('applySetField')
    @ApplySetField.setter
    def ApplySetField(self, value):
        self._set_attribute('applySetField', value)

    @property
    def ApplySetFieldMiss(self):
        """
        Returns
        -------
        - bool: Apply set field for table-miss.
        """
        return self._get_attribute('applySetFieldMiss')
    @ApplySetFieldMiss.setter
    def ApplySetFieldMiss(self, value):
        self._set_attribute('applySetFieldMiss', value)

    @property
    def Instruction(self):
        """
        Returns
        -------
        - bool: Select the type of instructions that the table flow entry will support.
        """
        return self._get_attribute('instruction')
    @Instruction.setter
    def Instruction(self, value):
        self._set_attribute('instruction', value)

    @property
    def InstructionMiss(self):
        """
        Returns
        -------
        - bool: Select the type of instruction miss capabilities that the table miss flow entry will support.
        """
        return self._get_attribute('instructionMiss')
    @InstructionMiss.setter
    def InstructionMiss(self, value):
        self._set_attribute('instructionMiss', value)

    @property
    def Match(self):
        """
        Returns
        -------
        - bool: Select the type of match capability that the table will support.
        """
        return self._get_attribute('match')
    @Match.setter
    def Match(self, value):
        self._set_attribute('match', value)

    @property
    def NextTable(self):
        """
        Returns
        -------
        - bool: Specify the next table property.
        """
        return self._get_attribute('nextTable')
    @NextTable.setter
    def NextTable(self, value):
        self._set_attribute('nextTable', value)

    @property
    def NextTableMiss(self):
        """
        Returns
        -------
        - bool: Specify the next table-miss property.
        """
        return self._get_attribute('nextTableMiss')
    @NextTableMiss.setter
    def NextTableMiss(self, value):
        self._set_attribute('nextTableMiss', value)

    @property
    def Wildcards(self):
        """
        Returns
        -------
        - bool: Select the type of wildcard capability that the table will support.
        """
        return self._get_attribute('wildcards')
    @Wildcards.setter
    def Wildcards(self, value):
        self._set_attribute('wildcards', value)

    @property
    def WriteActions(self):
        """
        Returns
        -------
        - bool: Select the type of write action capability that the table will support. The selected actions are appended to the existing action set of the packet.
        """
        return self._get_attribute('writeActions')
    @WriteActions.setter
    def WriteActions(self, value):
        self._set_attribute('writeActions', value)

    @property
    def WriteActionsMiss(self):
        """
        Returns
        -------
        - bool: Select the type of write action miss capability that the table miss flow entry will support.
        """
        return self._get_attribute('writeActionsMiss')
    @WriteActionsMiss.setter
    def WriteActionsMiss(self, value):
        self._set_attribute('writeActionsMiss', value)

    @property
    def WriteSetField(self):
        """
        Returns
        -------
        - bool: Write set field property.
        """
        return self._get_attribute('writeSetField')
    @WriteSetField.setter
    def WriteSetField(self, value):
        self._set_attribute('writeSetField', value)

    @property
    def WriteSetFieldMiss(self):
        """
        Returns
        -------
        - bool: Write set field for table-miss.
        """
        return self._get_attribute('writeSetFieldMiss')
    @WriteSetFieldMiss.setter
    def WriteSetFieldMiss(self, value):
        self._set_attribute('writeSetFieldMiss', value)

    def update(self, ApplyActions=None, ApplyActionsMiss=None, ApplySetField=None, ApplySetFieldMiss=None, Instruction=None, InstructionMiss=None, Match=None, NextTable=None, NextTableMiss=None, Wildcards=None, WriteActions=None, WriteActionsMiss=None, WriteSetField=None, WriteSetFieldMiss=None):
        """Updates featuresSupported resource on the server.

        Args
        ----
        - ApplyActions (bool): Select the type of apply action capability that the table will support. The selected actions associated with a flow are applied immediately.
        - ApplyActionsMiss (bool): Select the type of apply action miss capability that the table miss flow entry will support.
        - ApplySetField (bool): Apply set field property.
        - ApplySetFieldMiss (bool): Apply set field for table-miss.
        - Instruction (bool): Select the type of instructions that the table flow entry will support.
        - InstructionMiss (bool): Select the type of instruction miss capabilities that the table miss flow entry will support.
        - Match (bool): Select the type of match capability that the table will support.
        - NextTable (bool): Specify the next table property.
        - NextTableMiss (bool): Specify the next table-miss property.
        - Wildcards (bool): Select the type of wildcard capability that the table will support.
        - WriteActions (bool): Select the type of write action capability that the table will support. The selected actions are appended to the existing action set of the packet.
        - WriteActionsMiss (bool): Select the type of write action miss capability that the table miss flow entry will support.
        - WriteSetField (bool): Write set field property.
        - WriteSetFieldMiss (bool): Write set field for table-miss.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
