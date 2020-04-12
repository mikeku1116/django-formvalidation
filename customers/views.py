from django.shortcuts import render
from .forms import CustomerModelForm


def index(request):

    form = CustomerModelForm()

    context = {
        'form': form
    }

    return render(request, 'customers/index.html', context)
