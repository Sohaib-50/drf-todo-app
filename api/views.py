from rest_framework import viewsets, permissions
from .serializers import UserSerializer, TodoItemSerializer, TodoItemCreateSerializer, TodoItemDetailSerializer
from .models import TodoItem, User

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return TodoItemCreateSerializer
        elif self.action == 'retrieve':
            return TodoItemDetailSerializer
        else:  
            return TodoItemSerializer
    
    def get_queryset(self):

        selected_user_id = self.request.query_params.get("user_id")
        
        if selected_user_id:
            queryset = TodoItem.objects.filter(user_id=selected_user_id)
        else:
            queryset = TodoItem.objects.all()

        return queryset
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]