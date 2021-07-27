from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),
    path('customer_list/', views.Customer_List.as_view(), name="customer_list"),
    path('add_customer_list/', views.add_Customer_List.as_view(), name="add_customer_list"),
    path('update_customer_list/', views.update_customer_list.as_view(), name="update_customer_list"),
    path('vehicle_list/', views.Vehicle_List.as_view(), name="vehicle_list"),
    path('add_vehicle_list/', views.add_Vehicle_List.as_view(), name="add_vehicle_list"),
    path('update_vehicle_list/', views.update_vehicle_list.as_view(), name="update_vehicle_list"),
    path('test_list/', views.Test_List.as_view(), name="test_list"),
    path('vehicle_info/', views.vehicle_info.as_view(), name="vehicle_info"),
]
