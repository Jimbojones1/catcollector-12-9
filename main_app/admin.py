from django.contrib import admin

# Register your models here.
from .models import Cat, Feeding

# this creates a CRUD for a our cat model in the django admin app
admin.site.register(Cat)
admin.site.register(Feeding)