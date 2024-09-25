from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Talk


class TalkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Talk
        fields = [
            'id', 'owner', 'title', 'speaker', 'date', 'start_time',
            'end_time', 'summary', 'created_at', 'updated_at',
        ]
