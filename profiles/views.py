from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile

# Use class from CI DRF-API walkthrough.
class ProfileList(APIView):
    """
    List all profiles.
    There is no Create view (post method), as profile creation handled by django signals.
    """
    def get(self, request):
        profiles = Profile.objects.all()
        return Response(profiles)
