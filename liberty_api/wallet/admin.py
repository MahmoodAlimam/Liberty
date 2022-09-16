from django.contrib import admin
from .models import Client, Password

# Register your models here.
admin.site.register(Client)
admin.site.register(Password)