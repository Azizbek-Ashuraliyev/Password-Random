from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
import random
from random import sample
from .models import GenPass


def home(request):
    if request.method == "POST":
        site = request.POST.get('site')
        if site == "":
            return render(request, 'generator/home.html')
        password_lenght = int(request.POST.get('length'))
        characters = "!@#$%^&**()_+"
        numbers = '1234567890'
        small_letters = "qwertyuioplkjhgfdsazxcvbnm"
        upper_case = "QWERTYUIOPASDFGHJKLMNBVCXZ"
        prep = characters + numbers + small_letters + upper_case
        
        if password_lenght > 30:
            message = "can't generate password more than 30 characters"
            context = {
                'message':message
            }
            return render(request, 'generator/home.html', context)
        
        else:
            passwd = ''.join(random.sample(prep, k=password_lenght))
            print(passwd)
            p = GenPass.objects.create(site = site, password = passwd)
            p.save()
            
            context = {
                'password':passwd
            }
            return render(request, 'generator/success.html', context)
    return render(request, 'generator/home.html')

def list(request):
    context = {
        'items':GenPass.objects.all()
    }
    return render(request, 'generator/listall.html')

def search(request):
    if request.method == "POST":
        query = request.POST.get('site', None)
        if query:
            results = GenPass.objects.filter(site__conrains=query)
            return render(request, 'generator/search.html', {'results':results})
        
    return render(request, 'generator/search.html')

def deleterecord(request, id):
    obj = get_object_or_404(GenPass, id = id)
    obj.delete()
    return redirect('listall')