{% extends "mail_templated/base.tpl" %}

{% block subject %}
Reset Your Password
{% endblock %}

{% block html %}
<p>Hello,</p>
<p>You have requested to reset your password. Please click the link below to reset your password:</p>
<p><a href="{{ reset_password_url }}">Reset Password</a></p>
<p>If you did not request this password reset, please ignore this email.</p>
<p>Thank you!</p>
{% endblock %}
