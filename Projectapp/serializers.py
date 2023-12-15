from rest_framework import serializers
from Projectapp import models

class CustomUserProfileSerializer(serializers.ModelSerializer):
    """Serilizes a Custom user profile object"""
    class Meta:
        model = models.CustomUserProfile
        fields = ['id', 'Username', 'email', 'password']
        read_only_field = ['password']

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.CustomUserProfile.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user
