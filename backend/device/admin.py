from django.contrib import admin
from .models import DeviceModel


class DeviceAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "is_active")
    list_display = (
        "name",
        "model",
        "handed",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "name",
        "model",
    )
    search_fields = ("name", "model",)
    list_filter = [
        "handed",
        "is_active",
    ]
    list_per_page = 25


admin.site.register(DeviceModel, DeviceAdmin)
