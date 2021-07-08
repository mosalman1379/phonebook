from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext as _

phone_regex = RegexValidator(regex='^0[0-9]{2,}[0-9]{7,}$', message='invalid pone number')


class Entry(models.Model):
    surname = models.CharField(max_length=30, help_text=_('surname'))
    family_name = models.CharField(max_length=30, help_text=_('family_name'))
    phone_number = models.CharField(max_length=11, validators=[phone_regex], unique=True,
                                    help_text=_('phone_number'))

    def __str__(self):
        return self.surname
