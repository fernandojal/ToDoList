from django.shortcuts import get_object_or_404, render, redirect
from django.utils import html
from .models import List
from .forms import  ListForm
from django.contrib import messages

def home(request):  
    if request.method == 'POST':
        item = request.POST.get('Item')
        list = ListForm({'item': item})
        print(list.is_valid())
        if list.is_valid():
            list.save()
            all_items = List.objects.all()
            messages.success(request,('Item Has Been Added To List!'))
            return render(request, 'home.html', {'all_items': all_items})        
    else:
        all_items = List.objects.all()
        return render(request, 'home.html', {'all_items': all_items })

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Has Been Removed!'))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    item = List.objects.get(pk=list_id)
    if request.method == 'POST':
        
        form = ListForm(request.POST, instance=item)
        
        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html' , {'item': item} )
    
