from django.contrib import admin
from django.urls import path ,include
from.import views
from .views import update_profile ,update_driver


urlpatterns = [
    path('',views.log,name='log'),
    path('login/',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('home',views.index,name='home'),
    path('logoutpage',views.logoutpage,name='logoutpage'),
    path("profile", views.profile, name='profile'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('dlogin',views.dlogin,name='dlogin'),
    path('dsignup',views.dsignup,name='dsignup'), 
    path('driver',views.driver,name='driver'), 
    path('dlogoutpage',views.dlogoutpage,name='dlogoutpage'),
    # path('profile_detail/<int:user_id>/', profile_detail, name='profile_detail'),
    path('update_profile/<int:user_id>/', update_profile, name='update_profile'),
    path('driver_profile',views.driver_profile,name='driver_profile'),
    path('view_driver/',views.view_driver, name='view_driver'),
    path('update_driver/', update_driver, name='update_driver'),
    path('adddriver_profile',views.adddriver_profile,name='adddriver_profile'),
    path('booking_dpro',views.booking_dpro,name='booking_dpro'),
    path('booking/<int:pk>/', views.booking, name='booking'),
    path('view_booking',views.view_booking,name='view_booking'),
    path('user_booking',views.user_booking,name='user_booking'),
    
    
    path('chat/<int:driver_id>/', views.chat, name='chat'),
    path('driverchat/<int:user_id>/', views.driverchat, name='driverchat'),
    path('payment', views.payment, name='payment'),
    
    path('update-driver-profile/', views.update_driver_profile, name='update_driver_profile'),
    path('delete-driver-profile/', views.delete_driver_profile, name='delete_driver_profile'),

    

]

