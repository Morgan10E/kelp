from django.db import models
from core.models.metadata.models import Metadata


class CollectionType(Metadata):
    name = models.CharField(max_length=128)  # 'farmed', 'wild-caught', etc.

    def __str__(self):
        return self.name


class CollectionMethod(Metadata):
    name = models.CharField(max_length=128)  # 'gillnets', 'longline', 'recirculating tanks', etc.

    def __str__(self):
        return self.name
