from django.db import models
from django.contrib.auth.models import User


class Talk(models.Model):
    """
    Talk model for administrator to add talk events.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    speaker = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        List talks by date in ascending order.
        """
        ordering = ['date']

    def __str__(self):
        return f'{self.title} on {self.date}'
