from rest_framework import generics
from .models import CustomUserProfile
from .serializers import CustomUserProfileSerializer
from rest_framework.authentication import TokenAuthentication
from Projectapp import permission
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.
class CustomUserProfileCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUserProfile.objects.all()
    serializer_class = CustomUserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.OwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

class CustomUserProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUserProfile.objects.all()
    serializer_class = CustomUserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.OwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES