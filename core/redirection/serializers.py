from rest_framework import serializers
from .models import Links
from rest_framework.fields import CurrentUserDefault

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['name', 'url_link', 'shorted_link', 'counter']

    def save(self, user):
        user = user  # <= magic!
        name = self.validated_data['name']
        url_link = self.validated_data['url_link']
        return Links.objects.create(name=name, url_link=url_link, user=user)

    def update(self, instance):
        print(self.validated_data)
        if self.validated_data.get('name') is not None:
            instance.name = self.validated_data['name']
        if self.validated_data.get('url_link') is not None:
            instance.url_link = self.validated_data['url_link']
        if self.validated_data.get('counter') is not None:
            instance.counter = self.validated_data['counter']
        return instance.save()