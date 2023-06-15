from django.contrib import admin

# Register your models here.
from .models import Request, Schedule

admin.site.register(Request)
admin.site.register(Schedule)