# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class List(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class MenuOption(models.Model):
    name = models.CharField(max_length=30)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    url = models.CharField(max_length=120)
    target = models.CharField(max_length=20)
    icono = models.CharField(max_length=30)
    order = models.IntegerField()

    def __str__(self):
        return "{}/{}/{}".format(self.name, self.list, self.url)


class MenuOptionStatusNotAllowed(models.Model):
    option = models.ForeignKey(
        'dashboard.MenuOption',
        related_name="status_not_alloweds",
        on_delete=models.CASCADE)
    status = models.CharField(max_length=90)

    def __str__(self):
        return '{}/{}/{}'.format(self.status, self.option, self.option.list)
