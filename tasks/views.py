from .models import Task
from django.views.decorators.http import require_http_methods, require_GET,require_POST
from rest_framework import viewsets
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("-order_no")
    serializer_class = TaskSerializer
