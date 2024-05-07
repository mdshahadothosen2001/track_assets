from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from ..serializers.device import DeviceCreateSerializer, DeviceAssignToEmployeeSerializer
from utils.custom_permission import IsStaff
from device.models import DeviceModel


class DeviceCreateView(APIView):
    permission_classes = [IsStaff]

    def validate_parameter(self, company, name):
        if company and name:
            return True
        else:
            return False
        
    def post(self, request):
        company_id = request.data.get("company")
        name = request.data.get("name")
        if self.validate_parameter(company_id, name) is True:
            serializer = DeviceCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DeviceAssignToEmployeeView(APIView):
    permission_classes = [IsStaff]

    def validate_parameter(self, employee, device):
        if employee and device:
            return True
        else:
            return False
        
    def post(self, request):
        employee = request.data.get("employee")
        device = request.data.get("device")
        if self.validate_parameter(employee, device) is True:
            is_available = get_object_or_404(DeviceModel, id=device)
            if is_available.handed is False:
                serializer = DeviceAssignToEmployeeSerializer(data=request.data)
                if serializer.is_valid():
                    is_available.handed = True
                    is_available.save()
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)
