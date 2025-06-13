from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    USER_TYPES = (
        ('vendor', 'Vendor'),
        ('merchandising', 'Merchandising'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    vendor_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.profile_name} ({self.user.username})"


class Store(models.Model):
    store_name = models.CharField(max_length=100)

    def __str__(self):
        return self.store_name
    
class Subdepartment(models.Model):
    subdepartment_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subdepartment_name

class GondolaType(models.Model):
    gondola_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.gondola_type_name


class Gondola(models.Model):
    STATUS_CHOICES = (
        ('AVAILABLE', 'Available'),
        ('PENDING', 'Pending'),
        ('RESERVED', 'Reserved'),
    )

    gondola_name = models.CharField(max_length=100, null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='gondolas')
    gondola_type = models.ForeignKey(GondolaType, on_delete=models.SET_NULL, null=True)
    subdepartment = models.ForeignKey(Subdepartment, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.gondola_name} ({self.store.store_name})"


class Booking(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )

    gondola = models.ForeignKey(Gondola, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_bookings')
    booking_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    booking_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.user.username}"

    def save(self, *args, **kwargs):
        if self.booking_status == 'REJECTED':
            self.gondola.status = 'AVAILABLE'
        elif self.booking_status == 'APPROVED':
            self.gondola.status = 'RESERVED'
        else: 
            self.gondola.status = 'PENDING'

        self.gondola.save()
        super().save(*args, **kwargs)
