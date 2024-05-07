from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from ..serializers.staff import StaffRegistrationSerializer, EmployeeAddByStaffSerializer
from utils.custom_permission import IsStaff


class StaffRegistrationView(APIView):
    """Users can register their account by phone number, email, frist_name, last_name, compnay id and password."""

    permission_classes = [AllowAny]

    def validate_parameter(self, phone_number, email, company_id, password):
        if phone_number and email and password and company_id:
            return True
        else:
            return False

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")
        password = request.data.get("password")
        company_id = request.data.get("company_id")

        if self.validate_parameter(phone_number, email, company_id, password) is True:
            user_data = {
                "phone_number": phone_number,
                "email": email,
                "first_name": request.data.get("first_name"),
                "last_name": request.data.get("last_name"),
                "company": company_id,
                "password": password,
                "is_staff":True,
            }

            serializer = StaffRegistrationSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()

                return Response({"message":"Completed your registration process!"}, status=status.HTTP_201_CREATED)

        return Response({"message":"Incompleted registration! Please provide valid data"}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeAddByStaffView(APIView):
    """Staff can add employee' account by phone number, email, frist_name, last_name, compnay id and password."""

    permission_classes = [IsStaff]

    def validate_parameter(self, phone_number, email, company_id, password):
        if phone_number and email and password and company_id:
            return True
        else:
            return False

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")
        password = request.data.get("password")
        company_id = request.data.get("company_id")

        if self.validate_parameter(phone_number, email, company_id, password) is True:
            user_data = {
                "phone_number": phone_number,
                "email": email,
                "first_name": request.data.get("first_name"),
                "last_name": request.data.get("last_name"),
                "company": company_id,
                "password": password,
                "is_employee":True,
            }

            serializer = EmployeeAddByStaffSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()

                return Response({"message":"Completed your registration process!"}, status=status.HTTP_201_CREATED)

        return Response({"message":"Incompleted registration! Please provide valid data"}, status=status.HTTP_400_BAD_REQUEST)
