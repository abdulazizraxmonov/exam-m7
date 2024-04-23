from rest_framework import viewsets, permissions
from .filters import InfoNATOFilter
from .models import InfoNATO
from .serializers import InfoNATOSerializer
from rest_framework import generics, filters


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.added_by == request.user


class InfoNATOViewSet(viewsets.ModelViewSet):
    queryset = InfoNATO.objects.all()
    serializer_class = InfoNATOSerializer
    filterset_class = InfoNATOFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny] 
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
