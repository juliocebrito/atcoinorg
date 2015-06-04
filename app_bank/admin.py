from django.contrib import admin
from .models import Account, Pay, Charge
# Register your models here.
# admin.site.register(model)

@admin.register(Account)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'created', 'updated')

admin.site.register(Pay)
admin.site.register(Charge)