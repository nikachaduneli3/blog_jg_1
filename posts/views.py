from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostListSerializer, PostDetailSerializer, CommentSerializer
from django.utils import timezone
from .permissions import AuthorOrReadOnly
from rest_framework.decorators import api_view

class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def perform_create(self, serializer):
        user = self.request.user
        publish_date = timezone.now()
        serializer.save(author=user, publish_date=publish_date)

class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        res = super().get(request, *args, **kwargs)

        # increase post views
        post = self.get_object()
        post.views += 1
        post.save()

        return res


class CommentsListApiView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        res = super().get_queryset()
        post_id = self.kwargs.get('post_id')
        return res.filter(post_id=post_id, parent_comment=None)

    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs.get('post_id')
        serializer.save(author=user, post_id=post_id)

@api_view(['POST'])
def like_post(request, pk):
    post = Post.objects.get(id=pk)
    post.likes +=1
    post.save()
    return Response({'message': 'success'})
