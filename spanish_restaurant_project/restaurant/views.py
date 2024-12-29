from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Reservation


def home(request):
    return render(request, 'restaurant/home.html')


def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'restaurant/menu.html', {'items': items})


def reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        number_of_guests = request.POST.get('number_of_guests')
        Reservation.objects.create(
            name=name,
            phone=phone,
            date=date,
            time=time,
            number_of_guests=number_of_guests
        )
        return render(request, 'restaurant/reservation_success.html', {'name': name})
    return render(request, 'restaurant/reservation.html')
