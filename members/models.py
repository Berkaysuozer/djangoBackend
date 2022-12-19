from django.db import models

class Members(models.Model):
  username = models.CharField(max_length=30)
  tweet = models.CharField(max_length=140)