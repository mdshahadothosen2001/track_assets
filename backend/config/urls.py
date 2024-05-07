from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        route="admin/",
        view=admin.site.urls,
        name="admin",
    ),
    path(
        route="api/company/",
        view=include("company.urls"),
        name="company",
    ),
    path(
        route="api/staff/",
        view=include("staff_api.urls"),
        name="staff",
    ),
]
