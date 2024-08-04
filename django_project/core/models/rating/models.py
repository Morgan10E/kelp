from django.db import models
from core.models.metadata.models import Metadata


class Rating(Metadata):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=6) # hex color
    description = models.TextField()
    relative_score = models.IntegerField() # 'goodness' relative to other ratings; lower is better
