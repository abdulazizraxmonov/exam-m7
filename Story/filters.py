import django_filters
from .models import Story


class StoryFilter(django_filters.FilterSet):
    class Meta:
        model = Story
        fields = {
            'title': ['icontains'],
            'created_at': ['exact', 'gte', 'lte'],
        }