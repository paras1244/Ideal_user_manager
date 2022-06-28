
from django.db import models
from .custom_user import User


class Events(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    event_title = models.CharField(max_length=50)
    location  = models.CharField(max_length=100)
    
    start_time = models.DateTimeField(blank=False, null=False)
    end_time = models.DateTimeField(blank=False, null=False)
    
    def __str__(self):
        return self.event_title
