# -*- coding: utf-8 -*-
from django.test import TestCase
from apps.event.tests import factories
from apps.event import enums
from apps.security.tests.factories import GroupFactory
from apps.dashboard.tests.factories import (ListFactory, MenuOptionFactory,
                                            MenuOptionStatusNotAllowedFactory)


class UnitTest(TestCase):

    def setUp(self):

        self.event = factories.EventFactory()

        self.setStatusParticipant()
        self.setAuth()
        self.setOptionsDisplay()

        self.organizer = factories.OrganizerFactory(
            user=self.user, event=self.event)

    def setAuth(self):
        self.group = GroupFactory(name='Organizer')
        self.user = factories.UserFactory(
            username='djangorockstar',
            password='12345678',
            groups=([self.group]))

        self.client.login(username='djangorockstar', password='12345678')

    def setStatusParticipant(self):
        self.status_pendiente = factories.ParticipantStatusFactory(
            name=enums.ParticipantStatus.pendiente)
        self.status_aprobado = factories.ParticipantStatusFactory(
            name=enums.ParticipantStatus.aprobado)
        self.status_desestimado = factories.ParticipantStatusFactory(
            name=enums.ParticipantStatus.desestimado)

    def setOptionsDisplay(self):
        self.lista = ListFactory(
            name=enums.MenuOptionList.listado_participante)

        self.aprobar_option = MenuOptionFactory(
            name='Aprobar', list=self.lista)
        self.desestimar_option = MenuOptionFactory(
            name='Desestimar', list=self.lista)
        self.reenviar_option = MenuOptionFactory(
            name='Reenviar Invitación', list=self.lista)
        self.ver_invitacion_option = MenuOptionFactory(
            name='Ver Invitación', list=self.lista)
        self.ver_formulario = MenuOptionFactory(
            name='Ver Formulario', list=self.lista)

        MenuOptionStatusNotAllowedFactory(
            option=self.reenviar_option,
            status=enums.ParticipantStatus.pendiente)
        MenuOptionStatusNotAllowedFactory(
            option=self.reenviar_option,
            status=enums.ParticipantStatus.desestimado)
        MenuOptionStatusNotAllowedFactory(
            option=self.ver_invitacion_option,
            status=enums.ParticipantStatus.pendiente)
        MenuOptionStatusNotAllowedFactory(
            option=self.ver_invitacion_option,
            status=enums.ParticipantStatus.desestimado)

        MenuOptionStatusNotAllowedFactory(
            option=self.aprobar_option,
            status=enums.ParticipantStatus.desestimado)
        MenuOptionStatusNotAllowedFactory(
            option=self.aprobar_option,
            status=enums.ParticipantStatus.aprobado)

        MenuOptionStatusNotAllowedFactory(
            option=self.desestimar_option,
            status=enums.ParticipantStatus.desestimado)
        MenuOptionStatusNotAllowedFactory(
            option=self.desestimar_option,
            status=enums.ParticipantStatus.aprobado)
