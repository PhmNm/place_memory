from django.db import models
from django.contrib.auth.models import User
import uuid

class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    place_name = models.CharField(max_length=255, null=False)
    comments = models.TextField(blank=True)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + '|' + self.place_name