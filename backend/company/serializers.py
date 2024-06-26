from rest_framework.serializers import ModelSerializer

from company.models import ComapanyModel


class CompanyListSerializer(ModelSerializer):
    class Meta:
        model = ComapanyModel
        fields = ["id", "name", "title", "about", "located"]


class CompanyCreateSerializer(ModelSerializer):
    class Meta:
        model = ComapanyModel
        fields = ["name", "title", "about", "located"]
