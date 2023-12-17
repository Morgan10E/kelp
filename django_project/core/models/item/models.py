from django.db import models
from core.models.metadata.models import Metadata


class Item(Metadata):
    primary_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)


class ItemRating(Metadata):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE)
    # region = models.ForeignKey('Region', on_delete=models.CASCADE)
    collection_type = models.ForeignKey('CollectionType', on_delete=models.CASCADE)  # if blank, assume rating applies to all of 'item'
    collection_method = models.ForeignKey('CollectionMethod', blank=True, null=True, on_delete=models.CASCADE)  # if blank, assume rating applies to all of 'collection_type'; if 'collection_type' is blank, this must also be blank


# class AlternativeName(Metadata):
#     name = models.CharField(max_length=255)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = 'Alternative Names'


# class Region(Metadata):
#     name = models.CharField(max_length=255)  # 'Northwest Pacific', 'New Zealand', etc.

#     def __str__(self):
#         return self.name


class CollectionType(Metadata):
    name = models.CharField(max_length=128)  # 'farmed', 'wild-caught', etc.

    def __str__(self):
        return self.name


class CollectionMethod(Metadata):
    name = models.CharField(max_length=128)  # 'gillnets', 'longline', 'recirculating tanks', etc.

    def __str__(self):
        return self.name
