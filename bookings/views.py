from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Booking
from .serializers import BookingSerializer


class BookingList(generics.ListCreateAPIView):
    """
    List all talk event bookings made by user.
    """
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Booking.objects.all()
    filter_backends = [
         DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A user can retrieve, edit and delete a booking they own.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
