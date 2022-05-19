from django.contrib import admin
from .models import Category, Audio, Dynamic, Comment

admin.site.register(Category)
admin.site.register(Audio)
admin.site.register(Dynamic)
admin.site.register(Comment)