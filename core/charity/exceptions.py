# exceptions.py

class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidDonationAmountError(Error):
    """Raised when the donation amount is invalid"""
    pass


class InvalidCategoryError(Error):
    """Raised when the category is invalid"""
    pass


class InvalidAdvertisementError(Error):
    """Raised when the advertisement is invalid"""
    pass


class InvalidTitleError(Error):
    """Raised when the title is invalid"""
    pass


class InvalidContentError(Error):
    """Raised when the content is invalid"""
    pass


class ImageUploadError(Error):
    """Raised when the image is invalid"""
    pass
