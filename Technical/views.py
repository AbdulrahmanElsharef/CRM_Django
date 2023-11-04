from django.shortcuts import render,get_object_or_404
from .models import Request

# Create your views here.
def print(request):
    requests=Request.objects.all()
    return render(request, "print.html",{"objects":requests})

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