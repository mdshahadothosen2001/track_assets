from rest_framework import serializers

from user.models import UserAccount


class StaffRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserAccount
        fields = ["phone_number", "email", "first_name", "last_name", "company", "is_staff", "password",]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user


class EmployeeAddByStaffSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserAccount
        fields = ["phone_number", "email", "first_name", "last_name", "company", "is_employee", "password",]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user

