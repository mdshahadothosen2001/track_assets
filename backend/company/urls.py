from django.urls import path

from company.views import CompanyListView, CompanyCreateView

urlpatterns = [
    # http://localhost:8000/api/company/list/
    path(
        route="list/",
        view=CompanyListView.as_view(),
        name="company_list",
    ),
    # http://localhost:8000/api/company/create/
    path(
        route="create/",
        view=CompanyCreateView.as_view(),
        name="company_create",
    ),
]
