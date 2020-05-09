from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

UserModel = get_user_model() # get a class User in core.models


class EmailAuthBackend(ModelBackend):
    """
    Authenticates with the user's username or email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            email = username
            query = (
                Q(username=username) |
                Q(email=email)
            )
            user = UserModel.objects.get(query)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None