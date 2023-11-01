from django.shortcuts import render,get_object_or_404
from .models import Request

# Create your views here.
def ddd(request):
    return render(request, 'print.html',)

def request_invoice(request, id):
    # Retrieve a specific record by ID
    obj = get_object_or_404(Request, id=id)
    context={'obj':obj,}
    return render(request, 'invoice.html', context)