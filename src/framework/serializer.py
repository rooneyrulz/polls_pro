from rest_framework import serializers
from .models import Framework


class FrameworkSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()

    class Meta:
        model   = Framework
        fields  = [
            'id',
            'name',
            'vote',
            'language',
            'created_at',
        ]
