from django.shortcuts import render,get_object_or_404
from .models import Request
from .filter import RequesttFilter
from django.core.paginator import Paginator


# Create your views here.
def print(request):
    requests=Request.objects.all()
    # myfilter = RequesttFilter(request.GET, queryset=requests)
    context={"objects":requests,}
    # orders = myfilter.qs
    # paginator = Paginator(orders, 100)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    # # Render a template with the records
    # context = {"objects":requests,'page_obj': page_obj,
    #            'myfilter': myfilter,}
    return render(request, "print.html",context)

def invoice(request, id):
    # Retrieve a specific record by ID
    obj = get_object_or_404(Request, id=id)
    context={'obj':obj,}
    return render(request, 'invoice.html', context)

def technical(request, id):
    # Retrieve a specific record by ID
    obj = get_object_or_404(Request, id=id)
    context={'obj':obj,}
    return render(request, 'technical.html', context)

def credit_note(request, id):
    # Retrieve a specific record by ID
    obj = get_object_or_404(Request, id=id)
    context={'obj':obj,}
    return render(request, 'credit_note.html', context)

def replacement(request, id):
    # Retrieve a specific record by ID
    obj = get_object_or_404(Request, id=id)
    context={'obj':obj,}
    return render(request, 'replacement.html', context)