# -*- coding: utf-8 -*-
from .enums import ParticipantStatus
from . import models
from apps.utils import mail
from django.template.loader import render_to_string
from django.conf import settings


class ParticipantService(object):

    def __init__(self, participant):
        self.participant = participant

    def set_status_aprobado(self):
        status_aprobado = models.ParticipantStatus.objects.get(
            name=ParticipantStatus.aprobado)
        self.participant.status = status_aprobado
        self.participant.save()

    def send_invitation(self):
        subject = 'Django Rockstar Invitación'
        html = render_to_string("event/email/participant_invitation.html", {
                                'current_domain': settings.CURRENT_DOMAIN,
                                'participant': self.participant})

        mail.send_html_mail(subject, html, [self.participant.email])
