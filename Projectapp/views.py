from rest_framework import generics
from .models import CustomUserProfile
from .serializers import CustomUserProfileSerializer
from rest_framework.authentication import TokenAuthentication
from Projectapp import permission
# Create your views here.
class CustomUserProfileCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUserProfile.objects.all()
    serializer_class = CustomUserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.OwnProfile,)

class CustomUserProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUserProfile.objects.all()
    serializer_class = CustomUserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.OwnProfile,)