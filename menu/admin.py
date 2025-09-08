from django.contrib import admin
from .models import Restaurant, Menu, QRCode

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(QRCode)