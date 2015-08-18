from django.contrib import admin
from .models import Entry, Comment
# Register your models here.
# admin.site.register(model)

@admin.register(Entry)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'tittle', 'created', 'updated')


@admin.register(Comment)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created', 'updated')