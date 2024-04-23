from rest_framework import viewsets, permissions, generics, filters
from .filters import NATO_MemberFilter
from .models import NATO_Member
from .serializers import NATO_MemberSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.added_by == request.user


class NATO_MemberViewSet(viewsets.ModelViewSet):
    queryset = NATO_Member.objects.all()
    serializer_class = NATO_MemberSerializer
    filterset_class = NATO_MemberFilter
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
