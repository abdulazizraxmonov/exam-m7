import django_filters
from .models import NATO_Member

class NATO_MemberFilter(django_filters.FilterSet):
    class Meta:
        model = NATO_Member
        fields = {
            'name': ['icontains'],
            'year_joined': ['exact', 'gte', 'lte'],
            'military_capability': ['icontains'],
            'budget_allocation': ['exact', 'gte', 'lte'],
        }