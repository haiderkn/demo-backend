"""
Views for the user api
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from user.serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
)


class CreateUserView(APIView):
    """Please Create a new user in the system."""

    serializer_class = UserSerializer

    def post(self, request):
        """Create a new user."""
        complex_data = request.data
        serializer = self.serializer_class(data=complex_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ManageUserView(APIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Retrieve the authenticated user."""
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

    def put(self, request):
        """Update the authenticated user."""
        serializer = self.serializer_class(
            request.user,
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request):
        """Update the authenticated user."""
        serializer = self.serializer_class(
            request.user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def health_check(request):
    """Returns successful response."""
    return Response({'healthy': True})
