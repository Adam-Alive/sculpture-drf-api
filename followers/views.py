from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


# Use class from CI DRF-API walkthrough.
class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, ie. all instances of a user
    following another user'.
    Create a follower, ie. follow a user if logged in.
    Perform_create: associate the current logged in user with a follower.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Use class from CI DRF-API walkthrough.
class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower.
    No Update view, as we either follow or unfollow users.
    Destroy a follower, ie. unfollow someone if owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
