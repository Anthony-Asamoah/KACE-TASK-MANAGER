from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'priority',
            'due_date',
            'comments',
            'created_at',
            'updated_at',
            'assigned_to',
            'author',
        ]
