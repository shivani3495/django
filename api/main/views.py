from django.shortcuts import render
from .serializers import WomenSerializer
from rest_framework.generics import ListAPIView
from .models import Women
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter



# Create your views here.
# Create your views here.
def index(request):
    return render(request,'index.html')

class WomenList(ListAPIView):
 queryset = Women.objects.all()
 #queryset = Women.objects.filter(passby='user1')
 #queryset = Women.objects.filter(passby='user2')

 serializer_class = WomenSerializer
 #filter_backends = [DjangoFilterBackend]
 #filterset_fields = ['name']
 #filterset_fields = ['name','age']


# ordering filtering
 filter_backends = [OrderingFilter]
 ordering_fields = ['name', 'age']



