from collections import namedtuple
from enum import Enum
from typing import List

from ..encoder import Encoder
from .errors import InvalidStateError


class StateNamesEnum(Enum):
    """
    Contains the possible states that can have a message:
    """

    Started = "Started"  # a `Message` that has not been processed
    Pending = "Pending"  # a `Message` that has been enqueued
    Skipped = "Skipped"  # a `Message` that has been skipped
    Canceled = "Canceled"  # a `Message` that has been canceled
    Failure = "Failure"  # a `Message` that has been processed and raised an Exception
    Success = "Success"  # a `Message` that has been processed and does not raise an Exception


#: A type alias representing states in the database
class State(namedtuple("State", ("message_id", "name", "args", "kwargs"))):
    """Catalog Class, it storages the state
        Parameters:
            name: Name of the state
            args: List of arguments in the state(name)
    """

    def __new__(cls, message_id, name, args, kwargs):
        if name not in list(StateNamesEnum):
            raise InvalidStateError("The {} State is not defined".format(name))
        return super().__new__(cls, message_id, name, args, kwargs)

    @classmethod
    def from_dict(cls, dict):
        dict["name"] = StateNamesEnum(dict["name"])
        return cls(**dict)

    def asdict(self):
        return {**self._asdict(), "name": self.name.value}


class StateBackend:
    """ABC for  state backends.

    Parameters:
      namespace(str): The logical namespace under which the data
        should be stored.
      encoder(Encoder): The encoder to use when storing and retrieving
        result data.  Defaults to :class:`.JSONEncoder`.
    """

    namespace = "remoulade-state*"

    def __init__(self, *, namespace: str = "remoulade-state", encoder: Encoder = None):
        from ..message import get_encoder

        self.namespace = namespace
        self.encoder = encoder or get_encoder()

    def _build_message_key(self, message_id: str) -> str:  # noqa: F821
        """Given a message id, return its globally-unique key.

        Parameters:
          message_id(str)

        Returns:
          str
        """
        return "{}:{}".format(self.namespace, message_id)

    def get_state(self, message_id: str) -> State:
        """ Get the state with a message_id from the backend.

         Parameters:
             message_id(str)

         """
        raise NotImplementedError("%(classname)r does not implement get_state" % {"classname": type(self).__name__})

    def set_state(self, state: State, ttl: int) -> None:
        """ Save a message in the backend.

        Parameters:
            state(State)
            ttl(seconds): The time to keep that state in the backend
             default is one hour(3600 seconds)
        """
        raise NotImplementedError("%(classname)r does not implement set_state" % {"classname": type(self).__name__})

    def get_states(self) -> List[State]:
        """ Return all the states in the backend

        """
        raise NotImplementedError(
            "%(classname)r does not implement get_all_messages" % {"classname": type(self).__name__}
        )
