from django.shortcuts import render
from app_car.models import Cars

# Create your views here.


def start_page(request):
    car = Cars.objects.all()
    context = {'car_list': car}

    return render(request, 'index.html', context=context)


def side_page(request):
    car = Cars.objects.all()
    context = {'car_list': car}

    if request.method == 'POST':
        stamp_car = request.POST.get('car')
        year = request.POST.get('year')
        color = request.POST.get('color')
        mileage = request.POST.get('mileage')
        cost = request.POST.get('cost')

        Cars.objects.create(stamp_car=stamp_car, year=year,
                            color=color, mileage=mileage, cost=cost)

    return render(request, 'side_page.html', context=context)
