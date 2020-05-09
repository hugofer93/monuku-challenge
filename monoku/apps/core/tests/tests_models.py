from django.contrib.auth import get_user_model
from django.test import TestCase
import pytest

from ..models import Role

pytestmark = pytest.mark.django_db

UserModel = get_user_model()


@pytest.mark.django_db
class TestModels(TestCase):
    fixtures = ['test_roles.json', 'test_users.json']
    pytestmark = pytest.mark.django_db

    def setUp(self):
        self.role_admin = Role.objects.get(name='admin')
        self.role_reader = Role.objects.get(name='reader')
        self.role_editor = Role.objects.get(name='editor')

    def test_create_role(self):
        self.assertEqual(self.role_admin.id, 1)
        self.assertEqual(self.role_reader.id, 2)
        self.assertEqual(self.role_editor.id, 3)

    def test_create_user(self):
        user_admin = UserModel.objects.get(username='admin')
        user_reader = UserModel.objects.get(username='reader')
        user_editor = UserModel.objects.get(username='editor')

        self.assertEqual(user_admin.id, 1)
        self.assertEqual(user_admin.role.get(), self.role_admin)

        self.assertEqual(user_reader.id, 2)
        self.assertEqual(user_reader.role.get(), self.role_reader)

        self.assertEqual(user_editor.id, 3)
        self.assertEqual(user_editor.role.get(), self.role_editor)
