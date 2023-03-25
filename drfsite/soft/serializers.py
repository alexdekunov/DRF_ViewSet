from rest_framework import serializers
from .models import Soft

class SoftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soft
        fields = ['title', 'content', 'url']


