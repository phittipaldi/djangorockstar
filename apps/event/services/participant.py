# -*- coding: utf-8 -*-
import qrcode
from io import BytesIO as StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from apps.event.enums import ParticipantStatus
from apps.event import models
from apps.utils import mail
from django.template.loader import render_to_string
from django.conf import settings
from apps.utils.views import BarcodeGuest
import random
import string
from apps.event import enums


def rand_key(size):
    return ''.join(
        [random.choice(
            string.ascii_uppercase + string.digits) for i in range(size)])


class ParticipantService(object):

    def set_status_aprobado(self):
        status_aprobado = models.ParticipantStatus.objects.get(
            name=ParticipantStatus.aprobado)
        self.status = status_aprobado
        self.save()

        if not self.barcode:
            self.generate_barcode()
            self.generate_qrcode()

    def send_invitation(self, email):
        subject = 'Django Rockstar Invitación'
        html = render_to_string("event/email/participant_invitation.html", {
                                'current_domain': settings.CURRENT_DOMAIN,
                                'participant': self})

        mail.send_html_mail(subject, html, [email])

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=0,
        )
        url_qr = settings.CURRENT_DOMAIN + self.get_success_url()
        qr.add_data(url_qr)
        qr.make(fit=True)

        img = qr.make_image()

        buffer = StringIO()
        img.save(buffer)
        filename = 'participant-qr-{}.png'.format(self.uuid)
        filebuffer = InMemoryUploadedFile(
            buffer, None, filename, 'image/png', buffer.tell(), None)
        self.qrcode.save(filename, filebuffer)

    def generate_barcode(self):
        barcode_guest = BarcodeGuest()
        codigo = str(self.id).zfill(6)
        token = rand_key(7) + codigo
        self.barcode_value = token.upper()
        buffer = barcode_guest.generar_barcode_buffer(self)
        filename = 'guest-{}.svg'.format(self.id)
        filebuffer = InMemoryUploadedFile(
            buffer, None, filename, 'image/svg', buffer.tell(), None)
        self.barcode.save(filename, filebuffer)
        self.save()

    @property
    def get_options_menu_list(self):
        from apps.dashboard.models import MenuOption

        options_to_display = []
        options = MenuOption.objects.filter(
            list__name=enums.MenuOptionList.listado_participante)

        for option in options:
            found_status = any(
                self.status.name == r.status for r in option.status_not_alloweds.all())
            if found_status is False:
                options_to_display.append(option)
        return options_to_display
