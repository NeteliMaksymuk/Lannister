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

    def create_superuser(self, name, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(name=name, email=self.normalize_email(email), roles=['admin']
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    name = models.CharField(max_length=80, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=40, unique=True)
    roles = ArrayField(models.CharField(max_length=8), blank=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    objects = UserManager()
