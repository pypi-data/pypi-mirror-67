class InvalidKeyFormatError(Exception):
    """Error for when the key is not a hex string."""

    pass


class InvalidKeyLengthError(Exception):
    """Error for when the key is not the right amount of characters."""

    pass


class InvalidAccountFormatError(Exception):
    """Error for when the account is not a hex string."""

    pass


class InvalidAccountLengthError(Exception):
    """Error for when the key is not the right amount of characters."""

    pass


class PortInUseError(Exception):
    """Error for when the chosen port is in use."""

    pass


class EventFormatError(Exception):
    """Error for when a event is incorrectly formatted."""

    pass


class CodeNotFoundError(Exception):
    """Error for when a event is incorrectly formatted."""

    pass


class CRCMismatchError(Exception):
    """Error for when a event does not have matched CRC's."""

    pass

class ReceivedAccountUnknownError(Exception):
    """Error for when a event is received but cannot be matched to accounts."""

    pass
