from django.shortcuts import render, redirect
from .models import List
from .forms import  ListForm
from django.contrib import messages

def home(request):

    
    if request.method == 'POST':
        item = request.POST.get('Item')
        list = ListForm({'item':item})
        print(list.is_valid())
        if list.is_valid():
            list.save()
            all_items = List.objects.all()
            messages.success(request,('Item Has Been Added To List!'))
            return render(request, 'home.html', {'all_items': all_items})        
    else:
        all_items = List.objects.all()
    return render(request, 'home.html', {'all_items': all_items })
