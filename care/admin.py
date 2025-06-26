from django.contrib import admin

# Register your models here.
from .models import Care
from .models import Details
admin.site.register(Care)
admin.site.register(Details)
