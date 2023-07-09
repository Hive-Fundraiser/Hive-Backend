from rest_framework.exceptions import APIException


class IncompleteProfileError(APIException):
    status_code = 400
    default_detail = "لطفا اطلاعات پروفایل خود را تکمیل کنید."
    default_code = "incomplete_profile"
