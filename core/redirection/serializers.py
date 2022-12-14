from rest_framework import serializers
from .models import Links
from rest_framework.fields import CurrentUserDefault

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['name', 'url_link', 'shorted_link', 'counter']

    #def create(self, validated_data):
    #    name = validated_data['name']
    #    url_link = validated_data['url_link']
    #    user = None
    #    return Links.objects.create(name=name, url_link=url_link)

    def save(self, user):
        user = user  # <= magic!
        name = self.validated_data['name']
        url_link = self.validated_data['url_link']
        return Links.objects.create(name=name, url_link=url_link, user=user)