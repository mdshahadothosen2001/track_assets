from django.urls import path

from .views.staff import StaffRegistrationView, EmployeeAddByStaffView
from .views.token import CustomTokenObtainPairView
from .views.device import DeviceCreateView, DeviceAssignToEmployeeView, DeviceListView


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
    # http://localhost:8000/api/staff/device-add/
    path(
        route="device-add/",
        view=DeviceCreateView.as_view(),
        name="staff_device_add",
    ),
    # http://localhost:8000/api/staff/employee-add-by-staff/
    path(
        route="employee-add-by-staff/",
        view=EmployeeAddByStaffView.as_view(),
        name="staff_add_employee",
    ),
    # http://localhost:8000/api/staff/device-assign-to-employee-by-staff/
    path(
        route="device-assign-to-employee-by-staff/",
        view=DeviceAssignToEmployeeView.as_view(),
        name="staff_assign_device",
    ),
    # http://localhost:8000/api/staff/device-list/
    path(
        route="device-list/",
        view=DeviceListView.as_view(),
        name="staff_device_list",
    ),
]
