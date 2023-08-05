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


class CsvSnapshot(Base):
    """NOT DEFINED
    The CsvSnapshot class encapsulates a required csvSnapshot resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'csvSnapshot'

    def __init__(self, parent):
        super(CsvSnapshot, self).__init__(parent)

    @property
    def CsvDecimalPrecision(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('csvDecimalPrecision')
    @CsvDecimalPrecision.setter
    def CsvDecimalPrecision(self, value):
        self._set_attribute('csvDecimalPrecision', value)

    @property
    def CsvDumpTxPortLabelMap(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('csvDumpTxPortLabelMap')
    @CsvDumpTxPortLabelMap.setter
    def CsvDumpTxPortLabelMap(self, value):
        self._set_attribute('csvDumpTxPortLabelMap', value)

    @property
    def CsvFormatTimestamp(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('csvFormatTimestamp')
    @CsvFormatTimestamp.setter
    def CsvFormatTimestamp(self, value):
        self._set_attribute('csvFormatTimestamp', value)

    @property
    def CsvLocation(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('csvLocation')
    @CsvLocation.setter
    def CsvLocation(self, value):
        self._set_attribute('csvLocation', value)

    @property
    def CsvName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute('csvName')
    @CsvName.setter
    def CsvName(self, value):
        self._set_attribute('csvName', value)

    @property
    def CsvStringQuotes(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('csvStringQuotes')
    @CsvStringQuotes.setter
    def CsvStringQuotes(self, value):
        self._set_attribute('csvStringQuotes', value)

    @property
    def CsvSupportsCSVSorting(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('csvSupportsCSVSorting')
    @CsvSupportsCSVSorting.setter
    def CsvSupportsCSVSorting(self, value):
        self._set_attribute('csvSupportsCSVSorting', value)

    @property
    def NextGenRefreshBeforeSnapshot(self):
        """DEPRECATED 
        Returns
        -------
        - bool: nextGenRefreshBeforeSnapshot is deprecated and has no effect starting from IxNetwork 8.10.
        """
        return self._get_attribute('nextGenRefreshBeforeSnapshot')
    @NextGenRefreshBeforeSnapshot.setter
    def NextGenRefreshBeforeSnapshot(self, value):
        self._set_attribute('nextGenRefreshBeforeSnapshot', value)

    @property
    def OpenViewer(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute('openViewer')
    @OpenViewer.setter
    def OpenViewer(self, value):
        self._set_attribute('openViewer', value)

    @property
    def SnapshotSettingsName(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('snapshotSettingsName')

    @property
    def SnapshotViewContents(self):
        """
        Returns
        -------
        - str(allPages | currentPage): NOT DEFINED
        """
        return self._get_attribute('snapshotViewContents')
    @SnapshotViewContents.setter
    def SnapshotViewContents(self, value):
        self._set_attribute('snapshotViewContents', value)

    @property
    def SnapshotViewCsvGenerationMode(self):
        """
        Returns
        -------
        - str(appendCSVFile | newCSVFile | overwriteCSVFile): NOT DEFINED
        """
        return self._get_attribute('snapshotViewCsvGenerationMode')
    @SnapshotViewCsvGenerationMode.setter
    def SnapshotViewCsvGenerationMode(self, value):
        self._set_attribute('snapshotViewCsvGenerationMode', value)

    @property
    def Views(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../view]): NOT DEFINED
        """
        return self._get_attribute('views')
    @Views.setter
    def Views(self, value):
        self._set_attribute('views', value)

    def update(self, CsvDecimalPrecision=None, CsvDumpTxPortLabelMap=None, CsvFormatTimestamp=None, CsvLocation=None, CsvName=None, CsvStringQuotes=None, CsvSupportsCSVSorting=None, NextGenRefreshBeforeSnapshot=None, OpenViewer=None, SnapshotViewContents=None, SnapshotViewCsvGenerationMode=None, Views=None):
        """Updates csvSnapshot resource on the server.

        Args
        ----
        - CsvDecimalPrecision (number): NOT DEFINED
        - CsvDumpTxPortLabelMap (bool): NOT DEFINED
        - CsvFormatTimestamp (bool): NOT DEFINED
        - CsvLocation (str): NOT DEFINED
        - CsvName (str): 
        - CsvStringQuotes (bool): NOT DEFINED
        - CsvSupportsCSVSorting (bool): NOT DEFINED
        - NextGenRefreshBeforeSnapshot (bool): nextGenRefreshBeforeSnapshot is deprecated and has no effect starting from IxNetwork 8.10.
        - OpenViewer (bool): 
        - SnapshotViewContents (str(allPages | currentPage)): NOT DEFINED
        - SnapshotViewCsvGenerationMode (str(appendCSVFile | newCSVFile | overwriteCSVFile)): NOT DEFINED
        - Views (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../view])): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def ResetToDefaults(self):
        """Executes the resetToDefaults operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('resetToDefaults', payload=payload, response_object=None)

    def TakeCsvSnapshot(self):
        """Executes the takeCsvSnapshot operation on the server.

        Takes CSV Snapshot. The views and other settings must be set before the call using the /statistics/csvSnapshot attributes.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('takeCsvSnapshot', payload=payload, response_object=None)
