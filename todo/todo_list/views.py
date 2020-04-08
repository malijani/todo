""" Views of todo app """
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import List
from .forms import ListForm

def index(request):
    """ Index view for todo app """
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Item Has Been Added To List!")

    template = 'todo_list/index.html'
    all_items = List.objects.order_by('completed')
    context = {
        'all_items': all_items,
    }
    return render(request, template, context)

def cross_off(request, list_id):
    """ Action for completed tasks """
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('todo_list:index')

def uncross(request, list_id):
    """ Action to uncross the crossed items! """
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('todo_list:index')

def delete(request, list_id):
    """ View to delete items of todo """
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, "Item Has Been Deleted!")
    return redirect('todo_list:index')

def edit(request, list_id):
    """ Update the choosen item """
    template = 'todo_list/edit.html'
    item = List.objects.get(pk=list_id)
    context = {
        'item': item,
    }
    if request.method == "POST":
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item Has Been Edited")
            return redirect("todo_list:index")
    else:
        return render(request, template, context)
