from rest_framework import serializers
from .models import Talk


class TalkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Talk
        fields = [
            'id', 'owner', 'title', 'speaker', 'date', 'time',
            'summary', 'created_at', 'updated_at',
        ]
