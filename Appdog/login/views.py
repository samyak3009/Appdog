from django.shortcuts import render
from random import randint
import string 
import random 
from datetime import datetime
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, permissions, filters
from django.contrib.auth import authenticate, login

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.



class RegisterUser(APIView):

    # token_obtain_pair = TokenObtainPairView.as_view()

    def post(self, request):
        #validation to check whether mobile already exists
        if User.objects.filter(mobile=request.data.get('mobile')).exists():
            return Response(responsedata(False, "User mobile already present"), status=status.HTTP_400_BAD_REQUEST)
        #validation if confirm password and password does not match
        if request.data.get("confirm_password") != request.data.get("password"):
            return Response(responsedata(False, "Password Does Not Match!!"), status=status.HTTP_400_BAD_REQUEST)
        if request.data:
            data = request.data
            serializer = UserSerializer(data=data)        
            if serializer.is_valid(raise_exception=True):
                serializer.save()  
            user_data = serializer.data
            return Response(responsedata(True, "Data Inserted",user_data), status=status.HTTP_200_OK)
        return Response(responsedata(False, "No Data provided"), status=status.HTTP_400_BAD_REQUEST)

class UserProfile(APIView):
    #DB table to be used
    model_class = User
    #serializer to use
    serializer_class = UserSerializer
    #permissions
    permission_classes = [permissions.AllowAny]
    instance_name = 'User'
    # print("Sasas")
    #to get the user object according to PK
    def get_object(self, pk):
        print("sasa")
        try:
            return self.model_class.objects.get(pk=pk)
        except self.model_class.DoesNotExist:
            raise ValidationError({
                'status': False,
                'message': "failed to find {self.instance_name}",
                "data": {}
            })

    def get(self, request, pk=None, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj)
        return Response(
            data={
                "status": True,
                "message":f"{self.instance_name} reterived sucessfully",
                "data": serializer.data
            })

class LoginUser(TokenObtainPairView):
    """To login user using email/mobile and password"""

    token_obtain_pair = TokenObtainPairView.as_view() 

    def post(self, request, *args, **kwargs):
        #validation for password is required
        if not request.data.get("password"):
            return Response(responsedata(False, "Password is required"), status=status.HTTP_400_BAD_REQUEST)
        #validation if user with given email id does not exists
        if not User.objects.filter(mobile=request.data.get('mobile')).exists():
            return Response(responsedata(False, "No user found"), status=status.HTTP_400_BAD_REQUEST)
        #validation to check password
        if not User.objects.get(mobile=request.data.get('mobile')).check_password(request.data.get("password")):
            return Response(responsedata(False, "Incorrect Password"), status=status.HTTP_400_BAD_REQUEST)
        #to login user
        if request.data.get('mobile'):
            user = User.objects.get(mobile=request.data.get('mobile'))
            request.data['uuid'] = user.uuid
            user = authenticate(mobile=request.data.get('mobile'), password=request.data.get('password'))
            login(request,user)
        serializer = TokenObtainPairSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            data = serializer.validate(request.data)
            #to get user data
            data['user'] = User.objects.filter(uuid=request.data.get('uuid')).values()
            return Response(responsedata(True, "Sign in Successful", data), status=status.HTTP_200_OK)
        return Response(responsedata(False, "Something went wrong"), status=status.HTTP_400_BAD_REQUEST)

def responsedata(status, message, data=None):
    if status:
        return {"status":status,"message":message,"data":data}
    else:
        return {"status":status,"message":message}

