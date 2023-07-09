from rest_framework.exceptions import APIException


class EmailAlreadyVerified(APIException):
    status_code = 400
    default_detail = "Email is already verified."
    default_code = "email_already_verified"


class InvalidOrExpiredToken(APIException):
    status_code = 400
    default_detail = "Invalid or expired token."
    default_code = "invalid_or_expired_token"


class UserNotFound(APIException):
    status_code = 404
    default_detail = "User not found."
    default_code = "user_not_found"
