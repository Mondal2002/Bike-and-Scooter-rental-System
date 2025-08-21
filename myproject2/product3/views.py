from django.shortcuts import render,redirect
from .models import Category,Booking,User
from .form import BookingForm
from django.conf import settings

def show_vehicles(request):
    categories = Category.objects.all()
    form = BookingForm()
    print(categories)  # DEBUG
    return render(request, 'index.html', {'categories': categories ,'form': form})


from django.shortcuts import render, redirect
from .models import User, Booking
from .form import BookingForm  # This should include both user + booking fields

def book_vehicle(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            user, created = User.objects.get_or_create(
                email=form.cleaned_data['email'],
                defaults={
                    'name': form.cleaned_data['name'],
                    'phone': form.cleaned_data['phone']
                }
            )

            Booking.objects.create(
                user=user,
                vehicle_name=form.cleaned_data['vehicle_name'],
                pickup_date=form.cleaned_data['pickup_date'],
                return_date=form.cleaned_data['return_date']
            )

            return redirect('success')  # ✅ go to /success/ URL

        else:
            print("FORM ERRORS:", form.errors)

    else:
        form = BookingForm()

    return render(request, 'book_form.html', {'form': form})


 # success page after booking
    return redirect('success')
from .models import Booking, Category

def success_page(request):
    last_booking = Booking.objects.last()
    return render(request, 'success.html', {
        'vehicle_name': last_booking.vehicle_name
    })


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # optional: if CSRF is disabled for simplicity (not safe for production)
def delete_booking(request):
    if request.method == 'POST':
        vehicle_name = request.POST.get('vehicle_name')
        Booking.objects.filter(vehicle_name=vehicle_name).delete()
        return render(request, 'index.html')
import razorpay
from django.http import HttpResponse

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        # Optionally verify payment here
        return HttpResponse("Payment successful!")
def city_scooter_payment(request):
    return render(request, "City_Scooter.html")
def Premium_scooter_payment(request):
    return render(request, "Premium_scooter.html")
def Electric_scooter_payment(request):
    return render(request, "Electric_bike.html")
def Adventure_bike_payment(request):
    return render(request, "Adventure_bike.html")
def Sports_bike_payment(request):
    return render(request, "Sports_bike.html")
def Cruiser_bike_payment(request):
    return render(request, "Cruiser_bike.html")

def Cycle_payment(request):
    return render(request, "Cycle.html")
