from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate, login as auth_login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages

# Create your views here.

class RegisterAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            return Response({
                'message': 'Login successful'
            })

        return Response({
            'message': 'Invalid username or password'
        }, status=status.HTTP_401_UNAUTHORIZED)







def homepage(request):
    return render(request, "homepage.html")




# def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(
#             request,
#             username=username,
#             password=password
#         )

#         if user is not None:
#             auth_login(request, user)
#             return redirect("homepage")
#         else:
#             messages.error(request, "Invalid username or password")

#     return render(request, "login.html")






def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("Username:", username)
        print("Password:", password)

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("Authenticated user:", user)

        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            print("Login failed")

    return render(request, "login.html")











def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "register.html")




def home(request):
    return render(request, "home.html")