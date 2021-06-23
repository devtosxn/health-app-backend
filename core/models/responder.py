from django.db import models
from .user import User
from django.core.validators import MinLengthValidator
import uuid


class ResponderProfile(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=225, null=True, blank=True)
    account_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)], null=True, blank=True)
    bank_name = models.CharField(max_length=225, null=True, blank=True)
    avatar = models.URLField(max_length=255, blank=False)
    city = models.CharField(max_length=225, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id
