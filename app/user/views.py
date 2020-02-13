from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer


class ChangePasswordView(generics.UpdateAPIView):
    pass


class RecoveryPasswordView(generics.UpdateAPIView):
    pass


class ResetPassword(APIView):
    pass


class Registration(CreateAPIView, UpdateAPIView):
    allowed_methods = {'POST'}
    serializer_class = UserSerializer

    @api_view(['POST'])
    def register(self):
        serialized = self.get_serializer()
        if serialized.is_valid():
            serialized.create(validated_data=serialized.validated_data)
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
