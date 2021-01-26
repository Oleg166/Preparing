from django.http import HttpResponseRedirect
from django.shortcuts import render
from homepage.forms import AddForm
from homepage.models import Good_Item


def main(request):
    return render(request, 'homepage/index.html', {'itemslist': Good_Item.objects.all()})


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AddForm()
    return render(request, 'homepage/add.html', {'form': form})
