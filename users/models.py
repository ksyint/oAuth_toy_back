# from django.db import models

# # Create your models here.
# class User(models.Model):
#     pass




from __future__ import absolute_import

from django.contrib.auth import authenticate
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import allauth.app_settings
from allauth.account.models import EmailAddress
from allauth.account.utils import get_next_redirect_url, setup_user_email
from allauth.utils import get_user_model
from .settings import oauth2_settings

from ..utils import get_request_param
from . import app_settings, providers
from .adapter import get_adapter
from .fields import JSONField
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.management.utils import get_random_secret_key
from .settings import oauth2_settings

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, db_index=True)
    secret_key = models.CharField(max_length=255, default=get_random_secret_key)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        
class AbstractRefreshToken(models.Model):
   

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s"
    )
    token = models.CharField(max_length=255)
    application = models.ForeignKey(oauth2_settings.APPLICATION_MODEL, on_delete=models.CASCADE)
    access_token = models.OneToOneField(
        oauth2_settings.ACCESS_TOKEN_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="refresh_token",
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    revoked = models.DateTimeField(null=True)
    
    
    class Meta:
           abstract = True
           unique_together = (
            "token",
            "revoked",
        )
        
class RefreshToken(AbstractRefreshToken):
        class Meta(AbstractRefreshToken.Meta):
           swappable = "OAUTH2_PROVIDER_REFRESH_TOKEN_MODEL"
