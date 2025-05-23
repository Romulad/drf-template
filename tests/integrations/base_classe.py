from rest_framework.test import APIClient, APITestCase
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.core import mail
from django.urls import reverse

from apps_dir.users.models import User

class BaseTestClass(APITestCase):
  """Add common behavior needed across test classes"""
  url_name: str
  fake_token = "co43bu-d6272225128184b0b8107dffba6e8564"

  def __init__(self, methodName = "runTest"):
    super().__init__(methodName)
    self.client = APIClient()
    self.user_model : User = get_user_model()
  
  def get_mailbox(self):
    return mail.outbox
  
  def create_user(
      self, 
      email="myemail@gmail.com", 
      password="testpassword",
      **kwargs
  ) -> User :
    created_user = self.user_model.objects.create_user(
      email=email, password=password, is_active=False, **kwargs
    )
    return created_user
  
  def create_and_active_user(
      self, 
      email="myemail@gmail.com", 
      password="testpassword",
      **kwargs
  ) -> User :
    created_user = self.create_user(email, password, **kwargs)
    created_user.is_active = True
    created_user.save()
    return created_user

  def get(self, args: list | None = None) -> Response:
    path = reverse(self.url_name, args=args)
    return self.client.get(path)

  def post(self, data: dict, args: list | None = None) -> Response:
    path = reverse(self.url_name, args=args)
    return self.client.post(path, data)
  