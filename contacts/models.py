from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name', 'id',]
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=20)
    
    class Meta:
        ordering = ['first_name', 'last_name',]
        unique_together = ('user', 'email',)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name if self.last_name else ''} ({self.user.username})"