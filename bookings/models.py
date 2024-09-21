from django.db import models
from django.contrib.auth.models import User
from talks.models import Talk


class Booking(models.Model):
    """
    Booking model for user to register for talk events.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    questions = models.TextField(blank=True)
    suggestions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        List bookings by date in ascending order.
        """
        ordering = ['created_at']

    def __str__(self):
        return f'{self.title} on {self.date}'
