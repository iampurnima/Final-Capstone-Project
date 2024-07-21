from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Menu, Booking
from .serializers import  MenuSerializer, BookingSerializer


# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemsView(ListCreateAPIView):
    permission_classes ([IsAuthenticated])
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    permission_classes ([IsAuthenticated])
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer 
