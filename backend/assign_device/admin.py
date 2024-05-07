from django.contrib import admin

from .models import AssignDeviceModel


class AssignDeviceAdmin(admin.ModelAdmin):
    def employee(self, obj):
        return obj.employee.first_name
    
    def device(self, obj):
        return obj.device.name
    
    readonly_fields = ("created_at", "updated_at", "is_active")
    list_display = (
        "employee",
        "device",
        "taken_at",
        "return_at",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "employee",
        "device",
        "taken_at",
        "return_at",
    )
    search_fields = ("employee", "device")
    list_per_page = 25


admin.site.register(AssignDeviceModel, AssignDeviceAdmin)
