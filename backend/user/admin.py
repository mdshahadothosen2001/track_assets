from django.contrib import admin

from user.models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    def company(self, obj):
        return obj.company.name
    
    list_display = (
        "phone_number",
        "email",
        "gender",
        "company",
        "is_employee",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_display_links = (
        "phone_number",
        "email",
        "company",
    )
    search_fields = (
        "phone_number",
        "email",
    )
    list_filter = [
        "is_staff",
        "is_employee",
        "is_active",
    ]
    list_per_page = 25


admin.site.register(UserAccount, UserAccountAdmin)
