# tasks/auth_backend.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class CaseSensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = User._default_manager.get_by_natural_key(username)
        except User.DoesNotExist:
            return
        if user.check_password(password) and self.user_can_authenticate(user):
            return user

