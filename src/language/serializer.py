from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            'id',
            'text',
            'choices',
            'created_at',
        ]
