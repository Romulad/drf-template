from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

from rest_framework.request import Request

from apps_dir.users.models import User
from app_lib.urls import get_client_reset_password_url

def send_html_email(
    title: str,
    template_name: str, 
    email: str | list[str],
    context: str | None = None
):
  mail_to = email
  if isinstance(email, str):
    mail_to = [email]

  body = render_to_string(template_name, context)
  msg = EmailMessage(
    title,
    body,
    None, 
    mail_to
  )
  msg.content_subtype = 'html'
  msg.send()


def send_password_reset_email(
    user: User, 
    request: Request,
):
    user_email = user.email
    first_name = user.first_name
    uuid = urlsafe_base64_encode(force_bytes(user_email))
    token = default_token_generator.make_token(user)
    context = {
      "first_name": first_name,
      "url": get_client_reset_password_url(request, uuid, token),
    }
    send_html_email(
      f"Reset your password",
      "email/password_reset_email.html",
      user_email,
      context
    )


def send_password_reset_confirm_email(
    user: User, 
):
    user_email = user.email
    first_name = user.first_name
    context = {
      "first_name": first_name,
    }
    send_html_email(
      f"Password reset successfully",
      "email/password_reset_confirm.html",
      user_email,
      context
    )