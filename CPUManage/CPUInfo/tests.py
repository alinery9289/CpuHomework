from django.test import TestCase

# Create your tests here.
import models

def query1():
    b = models.Setting().objects.all()
    return str(b)

setting = models.Setting()
setting.cpu_is_local= 'local'
setting.cpu_consum = False
setting.cpu_state_set = 0 


