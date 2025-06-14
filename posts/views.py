from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView)
from rest_framework.response import Response
from .models import (
    Post,
    Comment,
    Tag, Category)
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    CommentSerializer,
    TagSerializer, CategorySerializer)
from django.utils import timezone
from .permissions import AuthorOrReadOnly
from rest_framework.decorators import api_view
from .filters import  PostFilterSet
import django_filters


class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = PostFilterSet

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


class TagListApiView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagPostsListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        tag = Tag.objects.get(id=tag_id)
        return tag.posts.all()

class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryPostsListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(id=category_id)
        return category.posts.all()


@api_view(['POST'])
def like_post(request, pk):
    post = Post.objects.get(id=pk)
    post.likes +=1
    post.save()
    return Response({'message': 'success'})

@api_view(['POST'])
def dislike_post(request, pk):
    post = Post.objects.get(id=pk)
    post.dislikes +=1
    post.save()
    return Response({'message': 'success'})

@api_view(['POST'])
def like_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.likes +=1
    comment.save()
    return Response({'message': 'success'})


@api_view(['POST'])
def dislike_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.dislikes +=1
    comment.save()
    return Response({'message': 'success'})

