# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource
from twilio.rest.conversations.v1.conversation.completed import CompletedList
from twilio.rest.conversations.v1.conversation.in_progress import InProgressList
from twilio.rest.conversations.v1.conversation.participant import ParticipantList


class ConversationList(ListResource):

    def __init__(self, version):
        """
        Initialize the ConversationList
        
        :param Version version: Version that contains the resource
        
        :returns: ConversationList
        :rtype: ConversationList
        """
        super(ConversationList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        
        # Components
        self._in_progress = None
        self._completed = None

    @property
    def in_progress(self):
        """
        Access the in_progress
        
        :returns: InProgressList
        :rtype: InProgressList
        """
        if self._in_progress is None:
            self._in_progress = InProgressList(self._version, **self._kwargs)
        return self._in_progress

    @property
    def completed(self):
        """
        Access the completed
        
        :returns: CompletedList
        :rtype: CompletedList
        """
        if self._completed is None:
            self._completed = CompletedList(self._version, **self._kwargs)
        return self._completed

    def get(self, sid):
        """
        Constructs a ConversationContext
        
        :param sid: The sid
        
        :returns: ConversationContext
        :rtype: ConversationContext
        """
        return ConversationContext(self._version, sid=sid, **self._kwargs)

    def __call__(self, sid):
        """
        Constructs a ConversationContext
        
        :param sid: The sid
        
        :returns: ConversationContext
        :rtype: ConversationContext
        """
        return ConversationContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ConversationList>'


class ConversationContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the ConversationContext
        
        :param Version version
        :param sid: The sid
        
        :returns: ConversationContext
        :rtype: ConversationContext
        """
        super(ConversationContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'sid': sid,
        }
        self._uri = '/Conversations/{sid}'.format(**self._kwargs)
        
        # Dependents
        self._participants = None

    def fetch(self):
        """
        Fetch a ConversationInstance
        
        :returns: Fetched ConversationInstance
        :rtype: ConversationInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            ConversationInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    @property
    def participants(self):
        """
        Access the participants
        
        :returns: ParticipantList
        :rtype: ParticipantList
        """
        if self._participants is None:
            self._participants = ParticipantList(
                self._version,
                conversation_sid=self._kwargs['sid'],
            )
        return self._participants

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Conversations.V1.ConversationContext {}>'.format(context)


class ConversationInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the ConversationInstance
        
        :returns: ConversationInstance
        :rtype: ConversationInstance
        """
        super(ConversationInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'status': payload['status'],
            'duration': deserialize.integer(payload['duration']),
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'start_time': deserialize.iso8601_datetime(payload['start_time']),
            'end_time': deserialize.iso8601_datetime(payload['end_time']),
            'account_sid': payload['account_sid'],
            'url': payload['url'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: ConversationContext for this ConversationInstance
        :rtype: ConversationContext
        """
        if self._instance_context is None:
            self._instance_context = ConversationContext(
                self._version,
                self._kwargs['sid'],
            )
        return self._instance_context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: str
        """
        return self._properties['sid']

    @property
    def status(self):
        """
        :returns: The status
        :rtype: conversation.status
        """
        return self._properties['status']

    @property
    def duration(self):
        """
        :returns: The duration
        :rtype: str
        """
        return self._properties['duration']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def start_time(self):
        """
        :returns: The start_time
        :rtype: datetime
        """
        return self._properties['start_time']

    @property
    def end_time(self):
        """
        :returns: The end_time
        :rtype: datetime
        """
        return self._properties['end_time']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: str
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a ConversationInstance
        
        :returns: Fetched ConversationInstance
        :rtype: ConversationInstance
        """
        return self._context.fetch()

    @property
    def participants(self):
        """
        Access the participants
        
        :returns: participants
        :rtype: participants
        """
        return self._context.participants

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Conversations.V1.ConversationInstance {}>'.format(context)
