import django_filters
from .models import InfoNATO


class InfoNATOFilter(django_filters.FilterSet):
    class Meta:
        model = InfoNATO
        fields = {
            'name': ['icontains'],
        }