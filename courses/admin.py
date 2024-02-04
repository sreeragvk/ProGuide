from django.contrib import admin
from courses.models import category
from courses.models import course

admin.site.register(category)
admin.site.register(course)