from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class AppUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class RoleOptions(models.TextChoices):
        SUPERADMIN = 'SUPERADMIN', 'SuperAdmin'
        ADMIN = 'ADMIN', 'Admin'
        DOCTOR = 'DOCTOR', 'Doctor'
        NURSE = 'NURSE', 'Nurse'
        RECEPTION = 'RECEPTION', 'Reception'
        INTERN = 'INTERN', 'Intern'
        PATIENT = 'PATIENT', 'Patient'
        COLAB = 'COLAB', 'Colab'
        TRAINEE = 'TRAINEE', 'Trainee'
        EMPLOYEE = 'EMPLOYEE', 'Employee'


class Role(models.Model):    
    base_role = RoleOptions.EMPLOYEE

    role = models.CharField(choices=RoleOptions.choices, max_length=50, default=base_role, unique=True)

    def __str__(self):
        return self.role
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(role__in=RoleOptions.values),
                name="%(app_label)s_%(class)s_role_valid",
            )
        ]
    


class User(AbstractUser):
    roles = models.ManyToManyField(Role, verbose_name='Roles')
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    #objects = UserManager()
    #objects = AppUserManager()

    def __str__(self):
        return self.email
    

class Patient(models.Model):
    pass


class Doctor(models.Model):
    pass