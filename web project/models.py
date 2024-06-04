# models.py

from django.db import models
import uuid

class SecretMessage(models.Model):
    """
    A model to store secret messages with a unique identifier.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SecretMessage {self.id}"
