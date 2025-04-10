from dataclasses import dataclass
from typing import List, Optional
from .message import Link, Links

@dataclass
class EndSessionMessage:
    type: str
    id: str
    reason: str
    feedbackId: str

@dataclass
class EndSessionResponse:
    messages: List[EndSessionMessage]
    _links: Links 