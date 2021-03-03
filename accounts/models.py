from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class User(AbstractUser):
    username = None
    first_name =models.CharField(_('First Name'), max_length=200)
    last_name =models.CharField(_('Last Name'), max_length=200)
    email = models.EmailField(_('Email'), unique=True, blank=True)
    verificate = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name +" "+self.last_name

    class Meta:
        ordering = ('-created', )
        verbose_name = _('User')
        verbose_name_plural = _('Users')

class Token(models.Model):
    user = models.OneToOneField(User, verbose_name='user',on_delete=models.CASCADE)
    token = models.CharField(('Token'), max_length=100)

    def __str__(self):
        return self.token
    
    class Meta:
        verbose_name = _('Token')
        verbose_name_plural = _('Tokens')
