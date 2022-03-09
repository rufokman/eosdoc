from django.shortcuts import render

from .forms import *


def parameters_view(request):
    form = AddPostForm(request.POST or None)
    if form.is_valid():
        print('form valid')
        form.save()
    else:
        print(form.errors)
    context = {
        'form': form
    }

    return render(request, 'param.html', context)
