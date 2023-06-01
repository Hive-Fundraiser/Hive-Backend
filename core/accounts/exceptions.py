# exceptions.py

class EmailNotProvidedError(ValueError):
    def __init__(self, message="The email must be set."):
        super().__init__(message)


class InvalidSuperuserError(ValueError):
    def __init__(self, message="Superuser must have is_staff=True."):
        super().__init__(message)

