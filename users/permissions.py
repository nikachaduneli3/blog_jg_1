from rest_framework.permissions import BasePermission
from .models import User
class CanReadFollowingsPosts(BasePermission):
    def has_permission(self, request, view):
        author_id = view.kwargs.get('author_id')
        author = User.objects.get(id=author_id)

        if author.is_public: return True

        if not request.user.is_active: return False
        followings = request.user.following.all().values_list('id', flat=True)
        return author_id in followings or request.user.is_superuser


