from time import timezone
from django.db import models


class GenPass(models.Model):
    site = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.site