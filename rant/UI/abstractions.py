from abc import ABC, abstractmethod

from rant.models import Message


class MessageDisplayerBase(ABC):
    @abstractmethod
    def display_message(self, message: Message):
        pass


class MessageComposerBase(ABC):
    def on_message_composed(self, message_body: str):
        pass
