from django.shortcuts import render, redirect, get_object_or_404
from .models import Metals,Plastics,Composites
from .forms import *


def index(request):
    return render(request, 'index.html')

#TO BE DISPLAYED ON INDEX--------------------------------------------------------
def display_metals(request):
    items = Metals.objects.all()
    context = {
        'items': items,
        'header': 'Metals',
    }
    return render(request, 'index.html', context)


def display_plastics(request):
    items = Plastics.objects.all()
    context = {
        'items': items,
        'header': 'Plastics',
    }
    return render(request, 'index.html', context)


def display_composites(request):
    items = Composites.objects.all()
    context = {
        'items': items,
        'header': 'Composites',
    }
    return render(request, 'index.html', context)

#ADDING NEW ENTRIES INTO FIELDS--------------------------------------------------------------
def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})


def add_metals(request):
    return add_item(request, MetalForm)


def add_plastics(request):
    return add_item(request, PlasticForm)


def add_composites(request):
    return add_item(request, CompositeForm)


#EDIT/ UPDATE THE FIELDS-------------------------------------------------------------------

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})



def edit_metals(request, pk):
    return edit_item(request, pk, Metals,MetalForm)


def edit_plastics(request, pk):
    return edit_item(request, pk, Plastics,PlasticForm)


def edit_composites(request, pk):
    return edit_item(request, pk, Composites,CompositeForm)



# DELETING FIELD ENTRIES-------------------------------------------------
def delete_metals(request, pk):

    template = 'index.html'
    Metals.objects.filter(id=pk).delete()

    items = Metals.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_plastics(request, pk):

    template = 'index.html'
    Plastics.objects.filter(id=pk).delete()

    items = Plastics.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_composites(request, pk):

    template = 'index.html'
    Composites.objects.filter(id=pk).delete()

    items = Composites.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)