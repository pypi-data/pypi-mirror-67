"""Errors for SIA Server."""


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


class EventFormatError(Exception):
    """Error for when a event is incorrectly formatted."""

    pass


class ReceivedAccountUnknownError(Exception):
    """Error for when a event is received but cannot be matched to accounts."""

    pass


class CRCMismatchError(Exception):
    """Error for when a event has mismatched CRCs."""

    pass


class TimestampError(Exception):
    """Error for when a event has timestamp outside of the timeband."""

    pass


class CodeNotFoundError(Exception):
    """Error for when a event has a unknown code."""

    pass
