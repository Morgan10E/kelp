from django.db import models
from core.models.metadata.models import Metadata


class Item(Metadata):
    primary_name = models.CharField(max_length=255, unique=True)  # TODO: support alternative names, example: "red salmon", "sockeye salmon"
    description = models.TextField(blank=True, null=True)


class ItemRating(Metadata):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE)
    collection_type = models.CharField(max_length=255)  # example: "intensive farming", "wild, line-caught"; if blank, assume rating applies to all of 'item'
