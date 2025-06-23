from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password_confirm = serializers.CharField()
    email = serializers.EmailField(required=False)


    def validate(self, data):
        if data.get('password') != data.get('password_confirm'):
            raise serializers.ValidationError('passwords didn\'t match')
        return data

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'gender',
                  'age', 'address', 'bio', 'profile_picture']