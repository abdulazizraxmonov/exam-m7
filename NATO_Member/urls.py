from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'nato-members', views.NATO_MemberViewSet)
urlpatterns = [
    path('', include(router.urls)),
]