from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from ..serializers.device import DeviceCreateSerializer


class DeviceCreateView(APIView):
    permission_classes = [AllowAny]

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
