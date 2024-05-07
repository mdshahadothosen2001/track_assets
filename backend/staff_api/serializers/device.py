from rest_framework.serializers import ModelSerializer

from device.models import DeviceModel


class DeviceCreateSerializer(ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = ["company", "name", "model"]
