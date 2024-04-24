from .models import User, TodoItem
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'is_complete', 'user', 'created']


class TodoItemDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'


class TodoItemCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['title', 'description']