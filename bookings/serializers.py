from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # talk = serializers.ReadOnlyField(source='talk.title')

    class Meta:
        model = Booking
        fields = [
            'id', 'owner', 'talk', 'speaker', 'date', 'start_time', 'end_time', 'name', 'email', 'questions',
            'suggestions', 'created_at', 'updated_at',
        ]
