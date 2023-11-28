"""
URL configuration for Contabilidad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalog import views
from django.contrib.auth import views as auth_views
#import settings
from django.conf.urls.static import static

app_name="catalog"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',views.home, name="home"),
    path('',views.home,name="home"),
    path('zip/',views.Upload_zip),
    path('zip/reset/', views.reiniciarSistema, name='reiniciarSistema'),
    path('accounts/', include('django.contrib.auth.urls')),
]

# if settings.DEBUG:
#     urlpatterns += media(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
