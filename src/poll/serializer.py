from rest_framework import serializers
from .models import Question, Choice


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
