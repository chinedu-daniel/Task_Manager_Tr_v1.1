from django.shortcuts import render

def register(request):
    return render(request, 'register/register.html')

# Create your views here.
