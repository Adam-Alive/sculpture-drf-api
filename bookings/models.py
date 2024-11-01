from django.db import models
from django.contrib.auth.models import User
from talks.models import Talk
import logging
logger = logging.getLogger('django.server')


class Booking(models.Model):
    """
    Booking model for user to register for talk events.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE, default=14)
    title = models.CharField(max_length=200, null=False, blank=False)
    speaker = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    summary = models.TextField(blank=True)
    questions = models.TextField(blank=True)
    suggestions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    logger.error('some important infos')
    class Meta:
        """
        List bookings by date in ascending order.
        """
        ordering = ['date']
        unique_together = (('owner', 'talk'),)

    def __str__(self):
        return f"{self.owner}'s booking for {self.title}"
