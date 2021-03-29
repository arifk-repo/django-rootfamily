from django.contrib import admin
from crudsederhana.models import Person,Root
# Register your models here.


class Person_Admin(admin.ModelAdmin):
    list_display = ['id','name','gender']
    search_fields = ['id','name','gender']
    list_filter = ['gender']
    list_per_page = 6


class Root_Admin(admin.ModelAdmin):
    list_display = ['id_person','id_parent']
    search_fields = ['id_person','id_parent']
    list_filter = ['id_parent']
    list_per_page = 5


admin.site.register(Person, Person_Admin)
admin.site.register(Root, Root_Admin)