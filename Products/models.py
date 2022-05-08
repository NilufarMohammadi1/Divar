from django.db import models
from Users.models import Users


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=100, blank=False)
    product_image = models.CharField(max_length=255, blank=False)
    product_description = models.TextField(blank=False)
    price = models.CharField(max_length=100, blank=False)
    lat_coordinate = models.FloatField(blank=False)
    long_coordinate = models.FloatField(blank=False)
    city = models.CharField(max_length=50, blank=False)
    region = models.CharField(max_length=100)
    is_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_forced = models.BooleanField(default=False)
    is_negotiable = models.BooleanField(default=True)
    confirmation_date = models.DateTimeField(auto_now_add=True)
    delete_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
