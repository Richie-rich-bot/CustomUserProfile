from .views import UserLoginApiView
from django.urls import path
from .views import CustomUserProfileCreateAPIView,CustomUserProfileRetrieveUpdateDestroyView

urlpatterns = [
    path('create/', CustomUserProfileCreateAPIView.as_view(), name='customuserprofile-create'),
    path('create/<int:pk>/',CustomUserProfileRetrieveUpdateDestroyView.as_view(), name='customuserprofile-retrieve-update-destroy'),
    path('login/',UserLoginApiView.as_view()),
    # Add other URL patterns if needed
]
