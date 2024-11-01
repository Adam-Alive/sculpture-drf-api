
# from django.db import IntegrityError
from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Booking
        fields = [
            'id', 'owner', 'title', 'speaker', 'date', 'start_time',
            'end_time', 'summary', 'questions', 'suggestions',
            'created_at', 'updated_at', 'is_owner', 'profile_id',
        ]

    # def create(self, validated_data):
    #     try:
    #         return super().create(validated_data)
    #     except IntegrityError:
    #         raise serializers.ValidationError({
    #             'detail': 'possible duplicate'
    #         })
