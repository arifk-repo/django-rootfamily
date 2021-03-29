"""CRUDdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from crudsederhana.views import home, parent, add_person, add_root, update_person, update_root, delete_person, delete_root


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home,name='home'),
    path('parent/', parent,name='parent'),
    path('addperson/', add_person),
    path('addroot/', add_root),
    path('updateperson/<int:id_person>', update_person,name='update_person'),
    path('updateroot/<int:id>', update_root,name='update_root'),
    path('deleteperson/<int:id_person>',delete_person,name='deleteperson'),
    path('deleteroot/<int:id>',delete_root, name='deleteroot')

]
