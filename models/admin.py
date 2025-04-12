from django.contrib import admin
from .models import Model, Comment, Like

admin.site.register(Model)
admin.site.register(Comment)
admin.site.register(Like)

