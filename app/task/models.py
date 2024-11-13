import logging

from django.db import models

from utils.model_validators import validate_no_null_chars

PRIORITY_CHOICES = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
]
STATUS_CHOICES = [
    ('todo', 'To Do'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
]


class Task(models.Model):
    title = models.CharField(max_length=255, validators=[validate_no_null_chars])
    description = models.TextField(validators=[validate_no_null_chars], null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    due_date = models.DateField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="assigned_tasks",
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="created_tasks"
    )

    class Meta:
        db_table = "task"

    def __str__(self):
        return self.title

    def notify_assignee(self):
        from django.core.mail import send_mail
        from django.conf import settings
        from django.template.loader import render_to_string
        from django.utils.html import strip_tags

        if self.assigned_to and self.assigned_to.email:
            subject = f"New Task Assigned: {self.title}"
            context = {
                'task': self.title,
                'due_date': self.due_date,
                'priority': self.get_priority_display(),
                'status': self.get_status_display(),
                'description': self.description,
            }

            html_message = render_to_string('task_assigned_email.html', context)
            plain_message = strip_tags(html_message)
            try:
                logging.info(f'sending email to {self.assigned_to.email}')
                send_mail(
                    subject,
                    plain_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [self.assigned_to.email],
                    html_message=html_message,
                    fail_silently=False,
                )
                logging.info(f'email sent')
            except Exception as e:
                logging.exception('failed to send email')
