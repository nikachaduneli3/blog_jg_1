from rest_framework import serializers
from .models import User, FollowRequest


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

class SendFollowRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowRequest
        fields = ['sent_to']
        
class ReceivedFollowRequestSerializer(serializers.ModelSerializer):
    sent_from = serializers.StringRelatedField()
    class Meta:
        model = FollowRequest
        fields = ['id', 'sent_from']