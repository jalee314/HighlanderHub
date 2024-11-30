from django.contrib import admin
from .models import * # imports all models in tweets app

admin.site.register(Tweet)
