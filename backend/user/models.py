from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from utils.utils import PHONE_REGEX
from company.models import ComapanyModel


class UserAccountManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if phone_number is None or password is None:
            raise ValueError("Phone Number & Password is required")

        user = self.model(
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        validators=[PHONE_REGEX], max_length=11, unique=True
    )
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)

    class Gender(models.TextChoices):
        male = "male"
        female = "female"
        others = "others"

    gender = models.CharField(
        max_length=10, choices=Gender.choices, null=True, blank=True
    )
    religion = models.CharField(max_length=64, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class MaritalStatus(models.TextChoices):
        single = "single"
        married = "married"
        divorced = "divorced"
        widowed = "widowed"
        separated = "separated"
        others = "others"

    marital_status = models.CharField(
        max_length=10, choices=MaritalStatus.choices, null=True, blank=True
    )
    profile_picture = models.URLField(null=True, blank=True)
    company = models.ForeignKey(ComapanyModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_employee = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone_number"

    objects = UserAccountManager()

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "User Account"
        verbose_name_plural = "User Accounts"
        db_table = "user_account"
