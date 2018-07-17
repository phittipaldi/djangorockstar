# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
from . import models_utils

# Register your models here.
admin.site.register(models.Participant)
admin.site.register(models.Portal)
admin.site.register(models.Slider)
admin.site.register(models.Event)
admin.site.register(models_utils.Languages)
admin.site.register(models_utils.OperatingSystem)
admin.site.register(models_utils.ProgramingLevel)
