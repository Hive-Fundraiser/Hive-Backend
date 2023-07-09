from rest_framework.exceptions import APIException


class EmailAlreadyVerified(APIException):
    status_code = 400
    default_detail = "ایمیل قبلا تایید شده است."
    default_code = "email_already_verified"


class InvalidOrExpiredToken(APIException):
    status_code = 400
    default_detail = "توکن نامعتبر یا منقضی شده است."
    default_code = "invalid_or_expired_token"


class UserNotFound(APIException):
    status_code = 404
    default_detail = "کاربری با این مشخصات یافت نشد."
    default_code = "user_not_found"
