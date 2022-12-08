from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'task', views.TaskViewSet)


urlpatterns = [
   path('move_item/<int:task_id>/<int:new_order_no>/', views.move_item),
]

