from rest_framework import serializers

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password_confirm = serializers.CharField()
    email = serializers.EmailField(required=False)


    def validate(self, data):
        if data.get('password') != data.get('password_confirm'):
            raise serializers.ValidationError('passwords didn\'t match')
        return data