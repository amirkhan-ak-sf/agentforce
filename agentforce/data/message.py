from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class MessageRequest:
    type: str
    sequenceId: int
    text: str

@dataclass
class MessagePayload:
    message: MessageRequest
    variables: List[Dict]

@dataclass
class Link:
    href: Optional[str] = None

@dataclass
class Links:
    self: Optional[Link] = None
    messages: Optional[Link] = None
    messagesStream: Optional[Link] = None
    session: Optional[Link] = None
    end: Optional[Link] = None

@dataclass
class MessageResponse:
    type: str
    id: str
    feedbackId: str
    planId: str
    isContentSafe: bool
    message: str
    result: List[Dict]
    citedReferences: List[Dict]

@dataclass
class SendMessageResponse:
    messages: List[MessageResponse]
    _links: Links 