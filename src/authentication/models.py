from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            username=username,
            email=email,
            password=password,
            **extra_fields,
        )
        user.save()
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):
    ROLE_CHOICES = (
        (1, 'CREATOR'),
        (2, 'AFFILIATED'),
    )
    email = models.EmailField('E-mail', max_length=60, unique=True, null=False, blank=False)
    email_verified = models.BooleanField("Email verified", default=False)
    username = models.CharField('Username', max_length=30, unique=True, null=False, blank=False)
    first_name = models.CharField('First Name', max_length=60, null=False, blank=False)
    last_name = models.CharField('Last Name', max_length=60, null=False, blank=False)
    role = models.PositiveSmallIntegerField('User Role', choices=ROLE_CHOICES, null=False, blank=False)
    password = models.CharField('Password', max_length=128, null=False, blank=False)
    created = models.DateTimeField('Created At', auto_now_add=True)
    is_staff = models.BooleanField('Is Staff', default=False)  # django user
    is_active = models.BooleanField('Is Active', default=True)  # django user
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']

    def __str__(self):
        return f'{self.last_name}, {self.first_name} <{self.email}>'

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()

        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)

        super(User, self).save(*args, **kwargs)
