
# Create your models here.
from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager



class Cliente(AbstractBaseUser, PermissionsMixin):
    username = models.TextField()
    telefone = models.TextField()
    endereço = models.CharField(max_length=30, blank=True)
    data_de_nascimento = models.DateField(null=True, blank=True)
    nome = models.CharField(('first name'),max_length=90)
    date_joined = models.DateTimeField(('date joined'))

    objects = UserManager()
    
    USERNAME_FIELD = 'nome'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')