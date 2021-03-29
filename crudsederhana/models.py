from django.db import models


class Person(models.Model):
    gender_male = 0
    gender_female = 1
    gender_choice = [(gender_male,'Laki-laki'), (gender_female,'Perempuan')]
    name = models.CharField(max_length=30,unique=True)
    gender = models.IntegerField(choices=gender_choice)

    def __str__(self):
        return self.name


class Root(models.Model):
    id_person=models.ForeignKey(Person,related_name='related_primary_person', on_delete=models.CASCADE,null=True,unique=True)
    id_parent=models.ForeignKey(Person,related_name='related_secondary_person', on_delete=models.CASCADE,null=True)