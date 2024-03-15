from django.contrib import admin
from .models import Students, Teachers, Kurses, Price, Branch, Lessons, Level

admin.site.register([Students, Teachers, Kurses, Price, Branch, Lessons, Level])

