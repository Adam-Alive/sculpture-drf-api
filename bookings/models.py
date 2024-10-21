from django.db import models
from django.contrib.auth.models import User
from talks.models import Talk


class Booking(models.Model):
    """
    Booking model for user to register for talk events.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    speaker = models.CharField(max_length=100, default="")
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True) 
    questions = models.TextField(blank=True)
    suggestions = models.TextField(blank=True)

    class Meta:
        """
        List bookings by date in ascending order.
        """
        ordering = ['date']      

    def __str__(self):
        return f"{self.owner}'s booking for {self.talk}"
