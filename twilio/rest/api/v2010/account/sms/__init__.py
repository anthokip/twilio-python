# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.api.v2010.account.sms.short_code import ShortCodeList
from twilio.rest.api.v2010.account.sms.sms_message import SmsMessageList
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class SmsList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the SmsList
        
        :param Version version: Version that contains the resource
        :param account_sid: A 34 character string that uniquely identifies this resource.
        
        :returns: SmsList
        :rtype: SmsList
        """
        super(SmsList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        
        # Components
        self._messages = None
        self._short_codes = None

    @property
    def messages(self):
        """
        Access the messages
        
        :returns: SmsMessageList
        :rtype: SmsMessageList
        """
        if self._messages is None:
            self._messages = SmsMessageList(self._version, **self._kwargs)
        return self._messages

    @property
    def short_codes(self):
        """
        Access the short_codes
        
        :returns: ShortCodeList
        :rtype: ShortCodeList
        """
        if self._short_codes is None:
            self._short_codes = ShortCodeList(self._version, **self._kwargs)
        return self._short_codes

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.SmsList>'


class SmsInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the SmsInstance
        
        :returns: SmsInstance
        :rtype: SmsInstance
        """
        super(SmsInstance, self).__init__(version)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.SmsInstance>'
