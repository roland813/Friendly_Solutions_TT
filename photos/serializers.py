from rest_framework import serializers
from photos.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['albumId', 'id', 'title', 'url']
