import re


def assert_valid_position(start=None, end=None):
    if start is not None and start < 1:
        raise ValueError(f"Start must be >= 1 ({start})")
    if end is not None and end < 1:
        raise ValueError(f"End must be >= 1 ({end})")

    if (start is not None and end is not None) and start > end:
        raise ValueError(f"Start ({start}) must be <= end ({end})")


def is_ensembl_id(feature):
    """String looks like an Ensembl Stable ID."""
    return bool(re.match(r"ENS[A-Z]+\d{11}(?:\.\d)?", feature.upper()))


def singleton(cls):
    """Wrapper that implements a class as a singleton."""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance
