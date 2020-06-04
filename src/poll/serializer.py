from rest_framework import serializers
from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.all(), many=True)
    class Meta:
        model = Question
        fields = [
            'id',
            'text',
            'choices',
            'created_at',
        ]
