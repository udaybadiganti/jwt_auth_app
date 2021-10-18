from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password = None):
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        #uday@Gmail.com --> uday@gmai.com
        email = email.lower()

        user = self.model(email = email, name = name)
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_owner(self, email, name, password=None):
        user = self.create_user(email, name, password)

        user.is_owner = True
        user.is_staff = True
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    is_owner = models.BooleanField(default = False)
    #is_customer = models.BooleanField(default = True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

