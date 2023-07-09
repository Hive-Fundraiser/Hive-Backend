from rest_framework.exceptions import APIException


class IncompleteProfileError(APIException):
    status_code = 400
    default_detail = "Please complete your profile before proceeding."
    default_code = "incomplete_profile"
