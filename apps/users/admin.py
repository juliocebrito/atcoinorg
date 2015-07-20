from django.contrib import admin
from .models import Profile, Relationship
from django.contrib.auth.models import Group
# Register your models here.
# admin.site.register(model)
# admin.site.unregister(Group)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email')


admin.site.register(Relationship)
