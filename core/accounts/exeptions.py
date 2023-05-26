"""
This module defines custom exception classes for a user authentication system.
"""


class EmailAlreadyExistsError(Exception):
    """
    Exception raised when a user tries to register with an email that already exists.
    """
    pass


class InvalidSuperuserError(Exception):
    """
    Exception raised when a superuser is created with is_staff=False or is_superuser=False.
    """
    pass
