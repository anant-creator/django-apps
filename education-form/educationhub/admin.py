from django.contrib import admin
from .models import all_courses, details

# Register your models here.
admin.site.register(all_courses)
admin.site.register(details)