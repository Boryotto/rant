from dataclasses import dataclass
from datetime import datetime


@dataclass
class Peer:
    id: str
    name: str
    ip: str
    port: int


@dataclass
class Message:
    body: str
    author: Peer
    timestamp: datetime
