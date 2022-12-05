from django.contrib import admin
from django.urls import path, include
from tasks import views 
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('tasks/',include('rest_framework.urls',namespace='rest_framework'))
]
