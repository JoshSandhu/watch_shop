from django.contrib import admin
from .models import Product, Review
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Product)

class ProductAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    summernote_fields = ('description')

@admin.register(Review)

class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'product', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)