from django.core.mail import send_mail
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import User
from .serializers import UserRegisterSerializer


class RegisterUser(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = User(username=serializer.data.get('username'),
                        email=serializer.data.get('email'))
            user.set_password(serializer.data.get('password'))
            user.save()

            send_mail(subject='Registration',
                      message=f'welcome {user.username}',
                      from_email='kanonieriqurdijemala@gmail.com',
                      recipient_list=[user.email])

            return Response({'message': 'success'})
        return Response(serializer.errors)
