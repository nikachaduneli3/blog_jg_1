from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer
from django.utils import timezone
from .permissions import AuthorOrReadOnly

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
