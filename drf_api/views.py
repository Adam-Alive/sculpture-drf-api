from rest_framework.decorators import api_view
from rest_framework.response import Response


# Use code from CI DRF-API walkthrough.
@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to the London Outdoor Sculpture API"
    })
