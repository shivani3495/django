from django.shortcuts import render
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.utils import timezone
print(timezone.now())

# Create your views here.

class Notification1API(ListAPIView):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request, pk=None, format=None):
        
        id = pk
        if id is not None:
            stu = Notification.objects.get(id=id)
            serializer = NotificationSerializer(stu)
            return Response(serializer.data)

        else:
            stu = Notification.objects.all()
            serializer = NotificationSerializer(stu,many=True)
            return Response(serializer.data)

    

class Notification2API(ListAPIView):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
  # permission_classes=[AllowAny]
  # permission_classes=[IsAdminUser]

class Notification3API(ListAPIView):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    
    def put(self, request, pk, format=None):
        id = pk
        stu = Notification.objects.get(pk=id)
        serializer = NotificationSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Notification4API(ListAPIView):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
   



    def delete(self, request, pk, format=None):
        id = pk
        stu = Notification.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

