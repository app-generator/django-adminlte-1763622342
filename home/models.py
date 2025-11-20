# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    role = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    sku = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    stock_quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Order(models.Model):

    #__Order_FIELDS__
    customer_email = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    order_number = models.CharField(max_length=255, null=True, blank=True)
    customer_name = models.CharField(max_length=255, null=True, blank=True)

    #__Order_FIELDS__END

    class Meta:
        verbose_name        = _("Order")
        verbose_name_plural = _("Order")


class Orderitem(models.Model):

    #__Orderitem_FIELDS__
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)
    line_total = models.IntegerField(null=True, blank=True)

    #__Orderitem_FIELDS__END

    class Meta:
        verbose_name        = _("Orderitem")
        verbose_name_plural = _("Orderitem")



#__MODELS__END
