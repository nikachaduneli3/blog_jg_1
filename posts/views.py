from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

