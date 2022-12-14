from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from time import time
from rest_framework.authtoken.models import Token

host_url = 'http://127.0.0.1:8000/'

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

def gen_link(s):
    return host_url + 'link/' + s

class API_token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=300, blank=True)

class Links(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    url_link = models.URLField(max_length=500)
    shorted_link = models.URLField(max_length=500, blank=True)
    counter = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
            self.shorted_link = gen_link(self.slug)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_creation']