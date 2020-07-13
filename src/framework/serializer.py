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


class FrameworkVoteSerializer(serializers.ModelSerializer):
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
    
    # def update(self, instance, validated_data):
    #     # instance.name = validated_data.get('email', instance.email)
    #     # instance.content = validated_data.get('content', instance.content)
    #     instance.vote = validated_data.get('user')
    #     return instance

