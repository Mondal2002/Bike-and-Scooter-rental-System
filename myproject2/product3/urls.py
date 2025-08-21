from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_vehicles, name='home'),
    path('book/', views.book_vehicle, name='book'),
    path('success/', views.success_page, name='success'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payments/city-scooter/', views.city_scooter_payment),
    path('payments/sport-bike/', views.Sports_bike_payment),
    path('payments/Premium-scooter/', views.Premium_scooter_payment),
    path('payments/Adventure-bike/', views.Adventure_bike_payment),
    path('payments/Electric-scooter/', views.Electric_scooter_payment),
    path('payments/Cruiser-bike/', views.Cruiser_bike_payment),
    path('payments/Cycle/', views.Cycle_payment),
]
