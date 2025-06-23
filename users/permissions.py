from rest_framework.permissions import BasePermission

class CanReadFollowingsPosts(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_active: return False
        followings = request.user.following.all().values_list('id', flat=True)
        author_id = view.kwargs.get('author_id')
        return author_id in followings


