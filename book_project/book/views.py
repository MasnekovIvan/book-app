from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'book/home.html', context)