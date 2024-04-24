from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet, UserViewSet 

router = DefaultRouter()
router.register(r'todos', TodoItemViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]