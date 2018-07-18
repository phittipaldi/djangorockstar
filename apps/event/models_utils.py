# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class OperatingSystem(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.name


class ProgramingLevel(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return u'%s' % self.name


class Languages(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return u'%s' % self.name


class Sex(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return u'%s' % self.name
