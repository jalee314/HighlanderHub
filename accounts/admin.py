from django.contrib import admin

from .models import * # imports all models in accounts app

admin.site.register(Profile)
