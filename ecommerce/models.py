from django.urls import reverse
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from uuid import uuid4
import os

# Create your models here.
ADDRESS_TYPE = (
    ('B', 'Billing'),
    ('S', 'Shipping')
)

def path_and_rename(instance, filename):
    upload_to = 'ecommerce/media/items/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk,ext)
    else:
        filename = '{}.{}'.format(uuid4().hex,ext)
    return os.path.join(upload_to, filename)


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    trending = models.BooleanField(default=False)
    # count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    # count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')

    class Meta:
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("sub_cat_view", kwargs={"category": self.category.title, "sub_category": self.title})
    
    


class Items(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    count = models.PositiveIntegerField(default=0)
    description = models.TextField()
    no_of_stock = models.PositiveIntegerField()
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='items')
    featured = models.BooleanField(default=False)
    deal_of_day = models.BooleanField(default=False)
    deal_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to=path_and_rename)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return self.title

    def get_discounted_price(self):
        return (self.price - (self.price * self.discount_price/100))

    def get_absolute_url(self):
        return reverse(
            "detail_view", 
            kwargs={
                "category": self.category.category.slug, 
                "sub_category": self.category.slug,
                "slug": self.slug
                }
        ) 
    
    


class OrderedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, null=True, blank=True)
    Items = models.ManyToManyField(OrderedItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    # payment = models.ForeignKey(
    #     'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    # coupon = models.ForeignKey(
    #     'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = CountryField(multiple=False)
    address_type = models.CharField(max_length=1, choices=ADDRESS_TYPE)

    class Meta:
        verbose_name_plural = 'Addresses'
    




