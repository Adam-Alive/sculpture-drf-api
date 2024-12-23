from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    """
    Booking model for user to register for talk events.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    speaker = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    summary = models.TextField(blank=True)
    questions = models.TextField(blank=True)
    suggestions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        List bookings by date in ascending order.
        """
        ordering = ['date']

    def __str__(self):
        return f"{self.owner}'s booking for {self.title}"
