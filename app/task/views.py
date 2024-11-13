from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets

from task.models import Task
from task.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.save()
        # Send notification email if an assignee is set
        if task.assigned_to:
            task.notify_assignee()

    def perform_update(self, serializer):
        # Check if 'assigned_to' is set or updated, then send the notification
        task = serializer.save()
        if 'assigned_to' in serializer.validated_data:
            task.notify_assignee()
