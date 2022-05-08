from django.db import models
from django.utils.translation import gettext_lazy as _

from Products.models import Products


class Fields(models.Model):
    class FieldType(models.TextChoices):
        STRING = 'SR', _('String')
        INTEGER = 'IN', _('Integer')
        FLOAT = 'FL', _('Float')

    field_id = models.AutoField(primary_key=True)
    field_title = models.CharField(max_length=50, blank=False)
    field_type = models.CharField(max_length=2, choices=FieldType.choices)
    field_hint = models.CharField(max_length=100, blank=True)


class Cats(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=100, blank=False)
    parent_id = models.IntegerField(null=True)
    cat_icon = models.CharField(max_length=255)
    cat_fields = models.ManyToManyField(Fields)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)


class ProductExtraFields(models.Model):
    product_id = models.ManyToManyField(Products)
    field_id = models.ManyToManyField(Fields)
    field_value = models.CharField(max_length=50, blank=False)