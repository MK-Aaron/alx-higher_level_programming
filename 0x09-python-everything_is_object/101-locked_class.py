#!/usr/bin/python3
"""Class LockedClass with no class or attribute"""


class LockedClass:
    """Prevent user from creating other instance

    crete only for "firstname"""

    __slots__ = ["first_name"]
