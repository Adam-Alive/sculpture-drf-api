from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Talk
from .serializers import TalkSerializer


class TalkList(generics.ListCreateAPIView):
    """
    List all talk events and create event if an administrator.    
    """       
    serializer_class = TalkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Talk.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
