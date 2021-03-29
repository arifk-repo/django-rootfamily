from django.shortcuts import render, redirect
from django.http import HttpResponse
from crudsederhana.models import Person,Root
from crudsederhana.forms import FormPerson, FormRoot
from django.contrib import messages


def home(request):
    persons = Person.objects.all()
    # persons = Person.objects.all().select_related('id')
    print(persons)
    data={
        'title':'Daftar Anggota',
        'persons':persons
    }
    return render(request, 'home.html',data)

def parent(request):
    roots= Root.objects.all()
    print(roots)
    data = {
        'title': 'Daftar Anggota',
        'roots': roots
    }
    return render(request, 'parent.html', data)
# Create your views here.

def add_person(request):
    if request.POST:
        form=FormPerson(request.POST)
        if form.is_valid():
            form.save()
            message = 'Data Sucessfull Added'
            data = {
                'title': 'Add Person',
                'form': form,
                'message':message
            }
            return render(request, 'addperson.html', data)
        else:
            warning = 'Data Failed Added'
            data = {
                'title': 'Add Person',
                'form': form,
                'warning':warning
            }
            return render(request, 'addperson.html', data)
    else:
        form=FormPerson()
        data={
            'title':'Add Person',
            'form':form
        }
    return render(request,'addperson.html',data)


def add_root(request):
    if request.POST:
        form = FormRoot(request.POST)
        if form.is_valid():
            form.save()
            message = 'Data Sucessfull Added'
            data = {
                'title': 'Add Root',
                'form': form,
                'message':message
            }
            return render(request, 'addroot.html', data)
        else:
            warning = 'Data Failed Added'
            data = {
                'title': 'Add Root',
                'form': form,
                'warning': warning
            }
            return render(request, 'addroot.html', data)
    else:
        form = FormRoot()
        data = {
            'title': 'Add Root',
            'form': form
        }
    return render(request, 'addroot.html', data)


def update_person(request, id_person):
    person=Person.objects.filter(id=id_person).first()
    template='updateperson.html'
    if request.POST:
        form=FormPerson(request.POST,instance=person)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diperbarui")
            return redirect('update_person',id_person)
        else:
            messages.error(request,"Data gagal diperbarui")
            return redirect('update_person', id_person)
    else:
        form=FormPerson(instance=person)
        data={
            'form':form,
            'person':person
        }
    return render(request,template,data)


def update_root(request, id):
    root = Root.objects.filter(id=id).first()
    print(root)
    if request.POST:
        form=FormRoot(request.POST, instance=root)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diperbarui")
            return redirect('update_root',id)
        else:
            messages.error(request,"Data gagal diperbarui")
            return redirect('update_root', id)
    else:
        form=FormRoot(instance=root)
        data={
            'form':form,
            'root':root
        }
    return render(request,"updateroot.html",data)


def delete_person(request,id_person):
    person = Person.objects.filter(id=id_person).first()
    print(person)
    person.delete()
    return redirect('home')


def delete_root(request,id):
    root = Root.objects.filter(id=id).first()
    root.delete()
    return redirect('parent')