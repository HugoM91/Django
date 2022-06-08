from django.db import models
from django.urls import reverse

# Create your models here.
class Registo(models.Model):

    username = models.CharField(max_length = 256)
    password = models.CharField(max_length = 256)
    usertype = models.CharField(max_length = 256)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('crud:crud', kwargs={'username':self.username})
