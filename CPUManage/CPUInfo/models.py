from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Setting(models.Model):
    cpu_is_local = models.CharField(max_length=45,primary_key=True,unique=True )
    cpu_consum = models.BooleanField()
    cpu_state_set = models.IntegerField()