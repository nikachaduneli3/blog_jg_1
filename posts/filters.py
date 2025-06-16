import django_filters
from .models import  Post


class PostFilterSet(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    publish_date = django_filters.DateFilter()
    content = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Post
        fields = ['title', 'publish_date',
                  'content']