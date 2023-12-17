from django.db import models
from django.utils import timezone


class Metadata(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Django 5 is timezone-aware by default
        now = timezone.now()
        if self._state.adding:
            self.created_at = now
        self.updated_at = now
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        abstract = True



