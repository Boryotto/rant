from abc import ABC, abstractmethod

from rant.models import Peer, Message


class MessageSenderBase(ABC):
    @abstractmethod
    def send_message(self, message: Message, peer: Peer):
        pass

    def on_message_received(self, message: Message):
        pass

    @abstractmethod
    def on_peer_connected(self, peer: Peer):
        pass
