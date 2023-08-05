import datetime
import json
from collections import namedtuple
from uuid import uuid4


class TopicalEventPayload:
    """
    This is the standard payload object to pass to topical event handlers.

    Attributes:
        idempotency_token (str): A token that does not change once created. Used by event handlers to skip already processed events.
        audit_log (list[tuple(datetime, str)]): A log of the functions that handled this event.
    """
    def __init__(self):
        self.__idempotency_token = uuid4()

        self.__created = datetime.datetime.now()
        self.__access_log = []

        self.__metadata = {}

    #region Properties
    @property
    def idempotency_token(self):
        return self.__idempotency_token

    @property
    def audit_log(self):
        return [f'[{l[0]}] {l[1]}' for l in self.__access_log]
    #endregion

    #region Public Methods
    def set_metadata(self, key, value):
        """
        Sets metadata values to the provided key.

        Parameters:
            key (str): the key to update
            value (Any): the value to use

        Returns:
            None
        """
        self.__metadata[key] = value

    def get_metadata(self, key, default=None):
        """
        Gets the specified metadata value.

        Parameters:
            key (str): The key to use for retrieval
            default (Any): The default value to return if the key is not found.

        Returns:
            Any
        """
        return self.__metadata.get(key, default)

    def delete_metadata(self, key):
        """
        Deletes the specified metadata field.
        Useful for clearing data that doesn't encode properly.

        Parameters:
            key (str): The key to delete

        Returns:
            None
        """
        if key in self.__metadata:
            del self.__metadata[key]

    def access_by(self, target):
        """
        Updates the access log

        Parameters:
            target (str): the name of the calling event handler

        Returns:
            None
        """
        self.__access_log.append((datetime.datetime.now().strftime('%Y-%d-%m %H:%M:%S'), target))

    def todict(self):
        """
        Helper method that returns a simplified dictionary

        Parameters:
            None

        Returns:
            dict[str, any]
        """
        return {
            'idempotency_token': str(self.idempotency_token),
            'created_on': str(self.__created),
            'audit_log': self.audit_log,
            'metadata': self.__metadata,
        }
    #endregion

class TopicalEventPayloadEncoder(json.JSONEncoder):
    """
    Custom encoder for use with json.dump[s]()

    Usage:
        obj = TopicalEventPayload()
        serialized_string = json.dumps(obj, cls=TopicalEventPayloadEncoder)
    """
    #pylint: disable=method-hidden
    def default(self, o:TopicalEventPayload):
        return o.todict()
    #pylint: enable=method-hidden
