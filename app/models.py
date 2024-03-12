# app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def get_chat_user(self):
        return self.user



class add_profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profileimg = models.ImageField(upload_to='profiles', null=True, blank=True)
    vehicle_name = models.CharField(max_length=25, null=True, blank=True)
    vehicle_number = models.CharField(max_length=15, null=True, blank=True)
    vehicle_img = models.ImageField(upload_to='profiles', null=True, blank=True)
    new_field = models.CharField(max_length=50, null=True, blank=True)  # New field

    def __str__(self):
        return self.name
    
    def get_chat_user(self):
        return self.user


class vehicle_owner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Add a default value, you can change it as needed
    name = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profileimg = models.ImageField(upload_to='profiles', null=True, blank=True)
    vehicle_name = models.CharField(max_length=25, null=True, blank=True)
    vehicle_number = models.CharField(max_length=15, null=True, blank=True)
    vehicle_img = models.ImageField(upload_to='profiles', null=True, blank=True)
    start = models.CharField(max_length=55, null=True, blank=True)
    end = models.CharField(max_length=55, null=True, blank=True)
    seat_count =models.CharField(max_length=25, null=True, blank=True)
    def __str__(self):
        return self.name

class Booking(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=25, null=True, blank=True)
    user_phone = models.IntegerField(null=True, blank=True)
    passenger_count = models.IntegerField()
    driver_id = models.IntegerField(null=True, blank=True)
    driver_name = models.CharField(max_length=25, null=True, blank=True) 
    driver_number = models.CharField(max_length=15, null=True, blank=True) 
    pickup_point = models.CharField(max_length=255,null=True, blank=True)
    dropping_point = models.CharField(max_length=255,null=True, blank=True)
    date = models.DateField()
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user_name} booked {self.driver_name}"


class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat between {self.sender.username} and {self.receiver.username}"
    

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question    