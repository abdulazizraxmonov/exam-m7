import django_filters
from .models import Operation

class OperationFilter(django_filters.FilterSet):
    class Meta:
        model = Operation
        fields = {
            'name': ['icontains'],
            'start_date': ['exact', 'gte', 'lte'],
            'end_date': ['exact', 'gte', 'lte'],
            'location': ['icontains'],
        }