from django.contrib import admin
from .models import UserProfile, Store, GondolaType, Gondola, Booking, Subdepartment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_name','user_type','vendor_code')

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'store_name')

@admin.register(Subdepartment)
class SubdepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'subdepartment_name')

@admin.register(GondolaType)
class GondolaTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'gondola_type_name')

@admin.register(Gondola)
class GondolaAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'gondola_type', 'subdepartment', 'price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'gondola', 'booking_date', 'booking_status')
