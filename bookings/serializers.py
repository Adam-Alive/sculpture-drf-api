from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Booking
        fields = [
            'id', 'owner', 'talk', 'speaker', 'date', 'start_time',
            'end_time', 'summary', 'questions', 'suggestions', 'is_owner',
        ]
