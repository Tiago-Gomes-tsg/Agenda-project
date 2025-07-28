from contacts.models import Contact, Category
from django.contrib import admin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'id',
    search_fields = 'name',

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'email', 'number', 'category', 'id', 'user', 'created_date'
    search_fields = 'first_name', 'last_name', 'email',
    list_filter = 'category', 'user',