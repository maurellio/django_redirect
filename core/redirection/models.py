from django.db import models
from django.contrib.auth.models import User

class Links(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url_link = models.URLField(max_length=500)
    counter = models.IntegerField(default=0)
