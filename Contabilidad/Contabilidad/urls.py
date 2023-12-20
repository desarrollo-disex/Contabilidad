from django.contrib import admin
from django.urls import path, include
from catalog import views

app_name="catalog"

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('inicio/',views.home, name="home"),
    path('',views.home,name="home"),
    path('dashboard/',views.Pagina2),
    path('dashboard/reset/', views.clear),
    path('accounts/', include('django.contrib.auth.urls')),
]