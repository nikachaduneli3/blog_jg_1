from django.core.mail import send_mail
from django.template.context_processors import request
from rest_framework.decorators import api_view
from rest_framework.generics import (
    GenericAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView
)
from rest_framework.response import Response
from .models import User, FollowRequest
from .serializers import (
    UserRegisterSerializer,
    UserProfileSerializer,
    SendFollowRequestSerializer,
    ReceivedFollowRequestSerializer
)
from .helpers import TokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from posts.models import Post
from posts.serializers import PostListSerializer
from .permissions import CanReadFollowingsPosts


def generate_user_activation_url(request, user):
    current_site = get_current_site(request)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = TokenGenerator().make_token(user)
    return f'http://{current_site}/users/activate/{uid}/{token}'

class RegisterUser(GenericAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = []
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = User(username=serializer.data.get('username'),
                        email=serializer.data.get('email'),
                        is_active=False)
            user.set_password(serializer.data.get('password'))
            user.save()


            send_mail(subject='Registration',
                      message=f'welcome {user.username}, '
                              f'activate you account '
                              f'{generate_user_activation_url(request, user)}',
                      from_email='kanonieriqurdijemala@gmail.com',
                      recipient_list=[user.email])

            return Response({'message': 'success'})
        return Response(serializer.errors)


@api_view(['GET'])
def activate_user(request, uid, token):
    pk = force_str(urlsafe_base64_decode(uid))
    user = User.objects.get(id=pk)
    if TokenGenerator().check_token(user, token):
        user.is_active = True
        user.save()
        return Response({'message': "user activated successfully"})
    return Response({'message': 'invalid token'})

class ProfileApiView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        user = self.request.user
        self.check_object_permissions(self.request, user)
        return user

class UsersListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

class UsersDetailView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

class UsersPostsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [CanReadFollowingsPosts]

    def get_queryset(self):
        result = super().get_queryset()
        author_id = self.kwargs.get('author_id')
        return result.filter(author_id=author_id)



class SendRequestView(CreateAPIView):
    queryset = FollowRequest.objects.all()
    serializer_class = SendFollowRequestSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(sent_from=user)

class ReceivedRequestsView(ListAPIView):
    queryset = FollowRequest.objects.all()
    serializer_class = ReceivedFollowRequestSerializer

    def get_queryset(self):
        logged_in_user = self.request.user
        return self.queryset.filter(sent_to=logged_in_user)
