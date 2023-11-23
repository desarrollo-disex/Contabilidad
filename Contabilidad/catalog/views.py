from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'registration/inicio.html')

def homeout(request):
    return HttpResponse("HASTA LUEGO!")

# @login_required(login_url='inicio/')
# def home(request):
#     if not request.user.is_staff:
#         return render(request, 'accountsfin.html')  # Reemplaza 'tupagina.html' con la ruta correcta a tu página personalizada
#     return render(request, 'accounts/inicio.html')

# # def fin(request):
# #     return HttpResponse("Bienvenido a la página FIN")

