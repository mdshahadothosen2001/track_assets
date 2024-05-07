from rest_framework.serializers import ModelSerializer

from device.models import DeviceModel
from assign_device.models import AssignDeviceModel


class DeviceCreateSerializer(ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = ["company", "name", "model"]


class DeviceAssignToEmployeeSerializer(ModelSerializer):
    class Meta:
        model = AssignDeviceModel
        fields = ["employee", "device"]