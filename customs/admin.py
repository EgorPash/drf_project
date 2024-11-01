from django.contrib import admin
from customs.models import Customs


@admin.register(Customs)
class CustomsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'owner', 'place', 'time', 'action']