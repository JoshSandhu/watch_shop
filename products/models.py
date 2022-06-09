from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    MinLengthValidator,
)
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Available"))

class Product(models.Model):
    title = models.CharField(max_length=200)
    ean_code = models.CharField(max_length=13, validators=[MinLengthValidator(13)], null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    brand = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='product_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.body} by {self.name}"