from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            return Response({"message": "Login successful"})
        return Response({"error": "Invalid credentials"}, status=401)


class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Missing fields"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "User already exists"}, status=400)

        User.objects.create_user(username=username, password=password)
        return Response({"message": "User registered successfully"})