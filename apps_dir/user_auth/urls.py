from rest_framework_simplejwt.views import (
  TokenRefreshView
)
from django.urls import path

from .views import *

urlpatterns = [
  path(
    'register/', 
    RegistrationView.as_view(), 
    name="register"
  ),
  path(
    'login/', 
    LoginView.as_view(), 
    name='login'
  ),
  path(
    'refresh/', 
    TokenRefreshView.as_view(), 
    name='token_refresh'
  ),
  path(
    'reset-password/', 
    PasswordResetView.as_view(), 
    name='password_reset'
  ),
  path(
    'reset-password/<str:uuid>/<str:token>/', 
    PasswordResetConfirmView.as_view(), 
    name='password_reset_confirm'
  ),
]
