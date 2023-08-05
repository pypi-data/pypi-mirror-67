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


class ApplyActions(Base):
    """Select the type of apply action capability that the table will support. The selected actions associated with a flow are applied immediately.
    The ApplyActions class encapsulates a required applyActions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'applyActions'

    def __init__(self, parent):
        super(ApplyActions, self).__init__(parent)

    @property
    def CopyTtlIn(self):
        """
        Returns
        -------
        - bool: If selected, table supports Copy TTL In Apply Actions.
        """
        return self._get_attribute('copyTtlIn')
    @CopyTtlIn.setter
    def CopyTtlIn(self, value):
        self._set_attribute('copyTtlIn', value)

    @property
    def CopyTtlOut(self):
        """
        Returns
        -------
        - bool: If selected, table supports Copy TTL Out Apply Actions.
        """
        return self._get_attribute('copyTtlOut')
    @CopyTtlOut.setter
    def CopyTtlOut(self, value):
        self._set_attribute('copyTtlOut', value)

    @property
    def DecrementMplsTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Decrement MPLS TTL Apply Actions.
        """
        return self._get_attribute('decrementMplsTtl')
    @DecrementMplsTtl.setter
    def DecrementMplsTtl(self, value):
        self._set_attribute('decrementMplsTtl', value)

    @property
    def DecrementNetworkTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Decrement Network TTL Apply Actions.
        """
        return self._get_attribute('decrementNetworkTtl')
    @DecrementNetworkTtl.setter
    def DecrementNetworkTtl(self, value):
        self._set_attribute('decrementNetworkTtl', value)

    @property
    def Group(self):
        """
        Returns
        -------
        - bool: If selected, table supports Group Apply Actions.
        """
        return self._get_attribute('group')
    @Group.setter
    def Group(self, value):
        self._set_attribute('group', value)

    @property
    def Output(self):
        """
        Returns
        -------
        - bool: If selected, table supports Output Apply Actions.
        """
        return self._get_attribute('output')
    @Output.setter
    def Output(self, value):
        self._set_attribute('output', value)

    @property
    def PopMpls(self):
        """
        Returns
        -------
        - bool: If selected, table supports Pop MPLS Apply Actions.
        """
        return self._get_attribute('popMpls')
    @PopMpls.setter
    def PopMpls(self, value):
        self._set_attribute('popMpls', value)

    @property
    def PopPbb(self):
        """
        Returns
        -------
        - bool: If selected, table supports Pop PBB Apply Actions.
        """
        return self._get_attribute('popPbb')
    @PopPbb.setter
    def PopPbb(self, value):
        self._set_attribute('popPbb', value)

    @property
    def PopVlan(self):
        """
        Returns
        -------
        - bool: If selected, table supports Pop VLAN Apply Actions.
        """
        return self._get_attribute('popVlan')
    @PopVlan.setter
    def PopVlan(self, value):
        self._set_attribute('popVlan', value)

    @property
    def PushMpls(self):
        """
        Returns
        -------
        - bool: If selected, table supports Push MPLS Apply Actions.
        """
        return self._get_attribute('pushMpls')
    @PushMpls.setter
    def PushMpls(self, value):
        self._set_attribute('pushMpls', value)

    @property
    def PushPbb(self):
        """
        Returns
        -------
        - bool: If selected, table supports Push PBB Apply Actions.
        """
        return self._get_attribute('pushPbb')
    @PushPbb.setter
    def PushPbb(self, value):
        self._set_attribute('pushPbb', value)

    @property
    def PushVlan(self):
        """
        Returns
        -------
        - bool: If selected, table supports Push VLAN Apply Actions.
        """
        return self._get_attribute('pushVlan')
    @PushVlan.setter
    def PushVlan(self, value):
        self._set_attribute('pushVlan', value)

    @property
    def SetField(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set Field Apply Actions.
        """
        return self._get_attribute('setField')
    @SetField.setter
    def SetField(self, value):
        self._set_attribute('setField', value)

    @property
    def SetMplsTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set MPLS TTL Apply Actions.
        """
        return self._get_attribute('setMplsTtl')
    @SetMplsTtl.setter
    def SetMplsTtl(self, value):
        self._set_attribute('setMplsTtl', value)

    @property
    def SetNetworkTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set Network TTL Apply Actions.
        """
        return self._get_attribute('setNetworkTtl')
    @SetNetworkTtl.setter
    def SetNetworkTtl(self, value):
        self._set_attribute('setNetworkTtl', value)

    @property
    def SetQueue(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set Queue Apply Actions.
        """
        return self._get_attribute('setQueue')
    @SetQueue.setter
    def SetQueue(self, value):
        self._set_attribute('setQueue', value)

    def update(self, CopyTtlIn=None, CopyTtlOut=None, DecrementMplsTtl=None, DecrementNetworkTtl=None, Group=None, Output=None, PopMpls=None, PopPbb=None, PopVlan=None, PushMpls=None, PushPbb=None, PushVlan=None, SetField=None, SetMplsTtl=None, SetNetworkTtl=None, SetQueue=None):
        """Updates applyActions resource on the server.

        Args
        ----
        - CopyTtlIn (bool): If selected, table supports Copy TTL In Apply Actions.
        - CopyTtlOut (bool): If selected, table supports Copy TTL Out Apply Actions.
        - DecrementMplsTtl (bool): If selected, table supports Decrement MPLS TTL Apply Actions.
        - DecrementNetworkTtl (bool): If selected, table supports Decrement Network TTL Apply Actions.
        - Group (bool): If selected, table supports Group Apply Actions.
        - Output (bool): If selected, table supports Output Apply Actions.
        - PopMpls (bool): If selected, table supports Pop MPLS Apply Actions.
        - PopPbb (bool): If selected, table supports Pop PBB Apply Actions.
        - PopVlan (bool): If selected, table supports Pop VLAN Apply Actions.
        - PushMpls (bool): If selected, table supports Push MPLS Apply Actions.
        - PushPbb (bool): If selected, table supports Push PBB Apply Actions.
        - PushVlan (bool): If selected, table supports Push VLAN Apply Actions.
        - SetField (bool): If selected, table supports Set Field Apply Actions.
        - SetMplsTtl (bool): If selected, table supports Set MPLS TTL Apply Actions.
        - SetNetworkTtl (bool): If selected, table supports Set Network TTL Apply Actions.
        - SetQueue (bool): If selected, table supports Set Queue Apply Actions.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
