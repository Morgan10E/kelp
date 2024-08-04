from django.db import models
from core.models.metadata.models import Metadata


NAME_COLOR_DELIMITER = ';'


class Rating(Metadata):
    name_and_color = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    relative_score = models.IntegerField() # 'goodness' relative to other ratings; lower is better
