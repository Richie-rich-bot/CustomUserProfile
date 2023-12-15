from rest_framework import generics
from .models import CustomUserProfile
from .serializers import CustomUserProfileSerializer

# Create your views here.
class CustomUserProfileCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUserProfile.objects.all()
    serializer_class = CustomUserProfileSerializer

class CustomUserProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUserProfile.objects.all()
    serializer_class = CustomUserProfileSerializer