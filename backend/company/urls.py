from django.urls import path

from company.views import CompanyListView

urlpatterns = [
    # http://localhost:8000/api/company/list/
    path(
        route="list/",
        view=CompanyListView.as_view(),
        name="company_list",
    ),
]
