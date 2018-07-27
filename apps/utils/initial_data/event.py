# -*- coding: utf-8 -*-
from apps.event.models_utils import (OperatingSystem, ProgramingLevel,
                                     Languages, Sex)

from apps.event.models import ParticipantStatus
from apps.dashboard.models import MenuOption, List, MenuOptionStatusNotAllowed
from apps.event import enums


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

    ParticipantStatus.objects.get_or_create(name='Pendiente',
                                            color='warning', order='A')
    ParticipantStatus.objects.get_or_create(name='Aprobado',
                                            color='success', order='B')
    ParticipantStatus.objects.get_or_create(name='Desestimado',
                                            color='danger', order='C')


def data_default_menu_option():

    ParticipantList = List.objects.get_or_create(
        name='Listado Participante')[0]

    AprobarParticipante = MenuOption.objects.get_or_create(
        name='Aprobar',
        list=ParticipantList,
        url='dashboard:participant-approval',
        target='_self',
        icono='fa-pencil',
        order=1
    )[0]

    DesestimarParticipante = MenuOption.objects.get_or_create(
        name='Desestimar',
        list=ParticipantList,
        url='dashboard:participant-cancel',
        target='_self',
        icono='fa-trash',
        order=2
    )[0]

    ReenviarInvitacion = MenuOption.objects.get_or_create(
        name='Reenviar Invitación',
        list=ParticipantList,
        url='event:resend-invitation',
        target='_self',
        icono='fa-envelope-o send-by-mail',
        order=3
    )[0]

    VistaPrelimarFormulario = MenuOption.objects.get_or_create(
        name='Ver Formulario',
        list=ParticipantList,
        url='event:participant-formpreview',
        target='_blank',
        icono='fa-eye',
        order=4
    )[0]

    VistaPrelimarInvitacion = MenuOption.objects.get_or_create(
        name='Ver Invitación',
        list=ParticipantList,
        url='event:participant-invitation',
        target='_blank',
        icono='fa-eye',
        order=5
    )[0]

    MenuOptionStatusNotAllowed.objects.get_or_create(
        option=ReenviarInvitacion,
        status=enums.ParticipantStatus.pendiente,
    )

    MenuOptionStatusNotAllowed.objects.get_or_create(
        option=ReenviarInvitacion,
        status=enums.ParticipantStatus.desestimado,
    )

    MenuOptionStatusNotAllowed.objects.get_or_create(
        option=VistaPrelimarInvitacion,
        status=enums.ParticipantStatus.pendiente,
    )

    MenuOptionStatusNotAllowed.objects.get_or_create(
        option=VistaPrelimarInvitacion,
        status=enums.ParticipantStatus.desestimado,
    )

    MenuOptionStatusNotAllowed.objects.get_or_create(
        option=AprobarParticipante,
        status=enums.ParticipantStatus.aprobado,
    )

    MenuOptionStatusNotAllowed.objects.get_or_create(
        option=AprobarParticipante,
        status=enums.ParticipantStatus.desestimado,
    )

    MenuOptionStatusNotAllowed.objects.get_or_create(
        option=DesestimarParticipante,
        status=enums.ParticipantStatus.aprobado,
    )

    MenuOptionStatusNotAllowed.objects.get_or_create(
        option=DesestimarParticipante,
        status=enums.ParticipantStatus.desestimado,
    )
