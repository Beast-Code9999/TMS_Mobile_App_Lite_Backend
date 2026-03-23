from rest_framework import serializers
from .models import User

# Read-only serializer and returns user data in response
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", 'username', 'email', 'role']

# Write serializer used for sign up 
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    # overrides default save behaviour and hashes password using create_user
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'student')
        )
        return user