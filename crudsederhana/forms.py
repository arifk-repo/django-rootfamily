from django.forms import ModelForm
from django import forms
from crudsederhana.models import Person,Root


class FormPerson(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

        widgets={
            'name':forms.TextInput({'class':'form-control'}),
            'gender':forms.Select({'class':'form-control'})
        }


class FormRoot(ModelForm):
    class Meta:
        model = Root
        fields = '__all__'

        widgets={
            'id_person':forms.Select({'class':'form-control'}),
            'id_parent':forms.Select({'class':'form-control'})
        }