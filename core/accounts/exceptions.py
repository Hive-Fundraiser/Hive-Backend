# exceptions.py

class EmailNotProvidedError(ValueError):
    def __init__(self, message="ابتدا ایمیل باید وارد شود."):
        super().__init__(message)


class InvalidSuperuserError(ValueError):
    def __init__(self, message="ایمیل وارد شده برای سوپر یوزر معتبر نیست."):
        super().__init__(message)

