from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):

    class Status(models.TextChoices):
        LOST = 'LT', 'Lost'
        FOUND = 'FD', 'Found'

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    phone_or_email = models.CharField(max_length=150)
    upload_image = models.ImageField(upload_to='items/%Y/%m/%d/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.LOST, blank=False)


    class Meta:
        ordering = ['status']
        indexes = [
            models.Index(fields=['-status']),]


    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"id": self.id})