from django.db import models
import qrcode
from django.conf import settings
import uuid
from django.core.files import File
from io import BytesIO
import qrcode
import os

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class QRCode(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    qr_image = models.ImageField(upload_to='qr_codes/')

    def save(self, *args, **kwargs):
        if not self.qr_image:
            self.qr_image = self.generate_qr_code()
        super().save(*args, **kwargs)

    def generate_qr_code(self):
        qr = qrcode.make(f"http://example.com/restaurant/{self.restaurant.id}/menu")
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        return File(buffer, name=f"{self.restaurant.name}_qr.png")
    