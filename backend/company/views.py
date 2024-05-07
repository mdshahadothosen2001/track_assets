from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from company.models import ComapanyModel
from .serializers import CompanyListSerializer, CompanyCreateSerializer


class CompanyListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        companies = ComapanyModel.objects.filter(is_active=True).order_by("name")
        serializer = CompanyListSerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyCreateView(APIView):
    permission_classes = [AllowAny]

    def validate_parameter(self, name, title):
        if name and title:
            return True
        else:
            return False
        
    def post(self, request):
        name = request.data.get("name")
        title = request.data.get("title")
        if self.validate_parameter(name, title) is True:
            serializer = CompanyCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)
