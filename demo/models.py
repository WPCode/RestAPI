from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Object(models.Model):

    firstName = models.CharField(max_length=100, blank=True, default='')
    lastName = models.CharField(max_length=100, blank=True, default='')
    dob = models.CharField(max_length=100, blank=True, default='')
    dod = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.firstName + " " + self.lastName + _(' dob%s dod %s') %(self.dob, self.dod)
