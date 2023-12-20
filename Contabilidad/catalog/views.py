from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'registration/inicio.html')

@login_required
def Pagina2(request):

    return render(request, 'registration/Pagina2.html')

def clear(request):

    return render(request, "registration/sistemaReiniciado.html")

