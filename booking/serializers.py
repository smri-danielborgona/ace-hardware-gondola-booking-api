from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Store, Subdepartment, GondolaType, Gondola, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email'
        ]

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )

    class Meta:
        model = UserProfile
        fields = [
            'user', 
            'user_id',
            'profile_name', 
            'user_type', 
            'vendor_code'
        ]

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            'id', 
            'store_name'
        ]

class SubdepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdepartment
        fields = [ 
            'id', 
            'subdepartment_name'
        ]

class GondolaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GondolaType
        fields = [
            'id', 
            'gondola_type_name'
        ]

class GondolaSerializer(serializers.ModelSerializer):
    # Readable nested data
    store = StoreSerializer(read_only=True)
    gondola_type = GondolaTypeSerializer(read_only=True)
    subdepartment = SubdepartmentSerializer(read_only=True)

    # Writeable ID fields for creation/update
    store_id = serializers.PrimaryKeyRelatedField(
        queryset=Store.objects.all(),
        source='store',
        write_only=True
    )
    gondola_type_id = serializers.PrimaryKeyRelatedField(
        queryset=GondolaType.objects.all(),
        source='gondola_type',
        write_only=True
    )
    subdepartment_id = serializers.PrimaryKeyRelatedField(
        queryset=Subdepartment.objects.all(),
        source='subdepartment',
        write_only=True
    )

    class Meta:
        model = Gondola
        fields = [
            'id',
            'store', 'store_id',
            'gondola_type', 'gondola_type_id',
            'gondola_name',
            'subdepartment', 'subdepartment_id',
            'price',
            'status'
        ]


class BookingSerializer(serializers.ModelSerializer):
    gondola = GondolaSerializer(read_only=True)
    gondola_id = serializers.PrimaryKeyRelatedField(
        queryset=Gondola.objects.all(),
        source='gondola',
        write_only=True
    )

    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )

    modified_by = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 
            'gondola',
            'gondola_id', 
            'user', 
            'user_id',
            'booking_status', 
            'booking_date', 
            'modified_by'
        ]
