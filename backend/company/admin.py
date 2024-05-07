from django.contrib import admin
from .models import ComapanyModel


class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "is_active")
    list_display = (
        "name",
        "title",
        "about",
        "located",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "name",
        "title",
        "located",
    )
    search_fields = ("name",)
    list_per_page = 25


admin.site.register(ComapanyModel, CompanyAdmin)
