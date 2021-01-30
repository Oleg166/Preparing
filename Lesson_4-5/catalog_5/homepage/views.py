from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from homepage.forms import AddForm
from homepage.models import Good_Item


def main(request):
    return render(request, 'homepage/index.html', {'itemslist': Good_Item.objects.all()})


def add(request):
    data = dict()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            itemslist = Good_Item.objects.all()
            data['products_html'] = render_to_string('homepage/list.html', {'itemslist': itemslist})
        else:
            data['form_html'] = render_to_string('homepage/form.html', {'form': form}, request=request)

    else:
        data['form_is_valid'] = False
        data['form_html'] = render_to_string('homepage/form.html', {'form': AddForm()}, request=request)

    return JsonResponse(data)
