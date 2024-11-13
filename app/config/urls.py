from django.urls import include, path
from rest_framework import routers

from user import views as user_views
from task import views as task_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'groups', user_views.GroupViewSet)

router.register(r'tasks', task_views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]