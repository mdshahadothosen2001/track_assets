from django.urls import path

from .views.staff import StaffRegistrationView

urlpatterns = [
    # http://localhost:8000/api/staff/register/
    path(
        route="register/",
        view=StaffRegistrationView.as_view(),
        name="staff_register",
    ),
]
