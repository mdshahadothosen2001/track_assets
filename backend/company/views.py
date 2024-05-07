from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from company.models import ComapanyModel
from .serializers import CompanyListSerializer


class CompanyListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        companies = ComapanyModel.objects.filter(is_active=True).order_by("name")
        serializer = CompanyListSerializer(companies, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
