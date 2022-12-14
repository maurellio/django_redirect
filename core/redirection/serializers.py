from rest_framework import serializers
from .models import Links

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['name', 'url_link', 'shorted_link', 'url_link', 'counter']