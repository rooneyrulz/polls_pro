from rest_framework import serializers
from .models import Choice


class ChoiceSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()

    class Meta:
        model = Choice
        fields = [
            'id',
            'text',
            'vote',
            'question',
            'created_at',
        ]
