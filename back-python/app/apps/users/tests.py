import pytest
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from .models import Role, RoleOptions

@pytest.mark.django_db
def test_user_create():
    User = get_user_model()
    User.objects.create(email='sistemia@gmail.com', password='mypassword')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_role_create():
    role = Role.objects.create()
    assert Role.objects.count() == 1
    assert role.role == 'EMPLOYEE'


@pytest.mark.django_db
def test_role_specific_create():
    role = Role.objects.create(role=RoleOptions.ADMIN)
    assert Role.objects.count() == 1
    assert role.role == 'ADMIN'

@pytest.mark.django_db
def test_role_specific_create():
    with pytest.raises(IntegrityError):
        role = Role.objects.create(role='ADMINsdgdfgfdgdfg')
    


@pytest.mark.django_db
def test_role_get_or_create():
    role1 = Role.objects.create(role=RoleOptions.ADMIN)
    role2, created = Role.objects.get_or_create(role=RoleOptions.ADMIN)
    assert created is False


@pytest.mark.django_db
def test_role_already_exist_create():
    with pytest.raises(IntegrityError):
        role1 = Role.objects.create(role=RoleOptions.ADMIN)
        role2 = Role.objects.create(role=RoleOptions.ADMIN)

@pytest.mark.django_db
def test_user_with_role():
    User = get_user_model()
    user = User.objects.create(email='sistemia@gmail.com', password='mypassword')
    role1 = Role.objects.create(role=RoleOptions.ADMIN)
    user.roles.add(role1)

    assert role1 in user.roles.all()


@pytest.mark.django_db
def test_user_with_wrong_role():
    User = get_user_model()
    user = User.objects.create(email='sistemia@gmail.com', password='mypassword')
    role1 = Role.objects.create(role=RoleOptions.ADMIN)
    role2 = Role.objects.create(role=RoleOptions.EMPLOYEE)
    user.roles.add(role1)

    assert role2 not in user.roles.all()