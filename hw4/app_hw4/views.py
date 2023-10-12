from django.shortcuts import render
from app_hw4.models import Furniture, Book, Phone
# Create your views here.


def start_project(request):
    furnitures = Furniture.objects.all()[0]
    context = {'furniture_list': furnitures}

    return render(request, 'index.html', context=context)


def second_page(request):
    book = Book.objects.all()[0]
    context = {'book_list': book}

    return render(request, 'second_index.html', context=context)


def third_page(request):
    phones = Phone.objects.all()[0]
    context = {'phone_list': phones}

    return render(request, 'third_index.html', context=context)