from django.db import models
from rest_framework.fields import SlugField
from treebeard.mp_tree import MP_Node


# Create your models here.
class category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    descriptions = models.CharField(max_length=2048, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    slug = SlugField()

    class Meta:
        verbose_name= 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

