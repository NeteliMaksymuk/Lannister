from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.postgres.fields import ArrayField


class UserManager(BaseUserManager):
    def create_user(self, name, email, roles, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(name=name, email=self.normalize_email(email), roles=roles)
        user.set_password(password)
        user.save(using=self._db)

        return user


class UserModel(AbstractBaseUser):
    name = models.CharField(max_length=80, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=40, unique=True)
    roles = ArrayField(models.CharField(max_length=8), blank=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    objects = UserManager()
