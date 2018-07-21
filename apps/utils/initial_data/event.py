# -*- coding: utf-8 -*-
from apps.event.models_utils import (OperatingSystem, ProgramingLevel,
                                     Languages, Sex)


def data_default_event():

    OperatingSystem.objects.get_or_create(name="Windows")
    OperatingSystem.objects.get_or_create(name="Mac OS")
    OperatingSystem.objects.get_or_create(name="Linux")

    ProgramingLevel.objects.get_or_create(name="Principiante")
    ProgramingLevel.objects.get_or_create(name="Intermedio")
    ProgramingLevel.objects.get_or_create(name="Avanzado")

    Languages.objects.get_or_create(name='Español')
    Languages.objects.get_or_create(name='Ingles')

    Sex.objects.get_or_create(name='Masculino')
    Sex.objects.get_or_create(name='Femenino')
