from django.db import models
from django.contrib.auth.models import User

class User(User):
    pass

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="TodoItems")
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

