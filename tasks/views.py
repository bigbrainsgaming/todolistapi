from .models import Task
from django.views.decorators.http import require_http_methods, require_GET,require_POST
from rest_framework import viewsets
from .serializers import TaskSerializer
from rest_framework.decorators import action

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("order_no")
    serializer_class = TaskSerializer

    @action(detail=False,methods=['POST'],name='move_todo_item')
    def move_item(self, request, pk=None, new_order_no=None):
        todoitem = self.get_object()
        todoitem.new_order_no = new_order_no
        todoitem.current_order_no = self.order_no
        todoitem.save()
        return todoitem
