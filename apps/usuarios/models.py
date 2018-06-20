from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from apps.programas.models import *


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_director = models.BooleanField('director status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    is_dean = models.BooleanField('dean status', default=False)
    programa = models.ForeignKey(ProgramaAcademico, null=True, blank=False, on_delete=models.CASCADE)
    facultad = models.ForeignKey(Facultad, null=True, blank=False, on_delete=models.CASCADE)
    is_superuser = models.BooleanField(('superuser status'),default=False,)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def is_super(self):
        if self.is_superuser:
            return True
        else:
            return False

    def get_type(self):
        if self.is_teacher:
            return "Profesor"
        elif self.is_director:
            return "Director"
        elif self.is_dean:
            return "Decano"
        else:
            return "Admin"

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return "{0}".format(self.get_username())
