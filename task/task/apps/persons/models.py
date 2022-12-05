from django.db import models

class persons(models.Model):
    name = models.CharField('ФИО', max_length=50)
    job = models.CharField('Должность', max_length=50)
    salary = models.IntegerField()
    department = models.CharField('Название отдела', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Данные работника'
        verbose_name_plural = 'Данные работников'

class depatments(models.Model):
    #persons = models.ForeignKey(persons, on_delete=CASCADE)
    depatment = models.CharField('Название отдела', max_length=50)

    class Meta:
        verbose_name = 'Название отдела'
        verbose_name_plural = 'Названия отделов'

    def __str__(self):
        return self.depatment

