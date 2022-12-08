from .models import Task
from django.views.decorators.http import require_http_methods, require_GET,require_POST
from rest_framework import viewsets
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("order_no")
    serializer_class = TaskSerializer

    @action(detail=True,methods=['POST'],name='move_todo_item',url_path=r'move/(?P<new_order_no>\d)')
    def move_item(self, request, pk=None, new_order_no=None):
        try:
                
            t = Task.objects.filter(id=pk).get()
            t.move(new_order_no=new_order_no)
            return Response({'status':'success', 'task_id':t.id,'new_order_no':t.order_no})
        except Exception:
            return Response({'status':'fail'})
