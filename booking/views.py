from django.shortcuts import render
from rest_framework import viewsets
from .models import Booking, Gondola, GondolaType, Store, Subdepartment, UserProfile
from .serializers import BookingSerializer, GondolaSerializer, GondolaTypeSerializer, StoreSerializer,SubdepartmentSerializer,UserProfileSerializer

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class SubdepartmentViewSet(viewsets.ModelViewSet):
    queryset = Subdepartment.objects.all()
    serializer_class = SubdepartmentSerializer

class GondolaTypeViewSet(viewsets.ModelViewSet):
    queryset = GondolaType.objects.all()
    serializer_class = GondolaTypeSerializer

class GondolaViewSet(viewsets.ModelViewSet):
    queryset = Gondola.objects.all()
    serializer_class = GondolaSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_staff or user.is_superuser:
    #         return Booking.objects.all()
    #     else:
    #         return Booking.objects.filter(user=user)

    