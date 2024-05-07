from django.urls import path

from .views.staff import StaffRegistrationView
from .views.token import CustomTokenObtainPairView

urlpatterns = [
    # http://localhost:8000/api/staff/register/
    path(
        route="register/",
        view=StaffRegistrationView.as_view(),
        name="staff_register",
    ),
    # http://localhost:8000/api/staff/token/
    path(
        route="token/",
        view=CustomTokenObtainPairView.as_view(),
        name="staff_token",
    ),
]
