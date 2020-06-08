from rest_framework import serializers
from .models import Language


class LanguageSerializer(serializers.ModelSerializer):
    frameworks = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Language
        fields = [
            'id',
            'name',
            'frameworks',
            'created_at',
        ]
