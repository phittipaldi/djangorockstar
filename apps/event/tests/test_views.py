from django.test import TestCase
from django.test import override_settings
from . import factories
from apps.event import models


class ParticipantViewTest(TestCase):

    def setUp(self):
        self.portal = factories.PortalFactory()
        self.operatingSystem = factories.OperatingSystemFactory()
        self.sex = factories.SexFactory()
        self.level = factories.ProgramingLevelFactory()
        self.event = factories.EventFactory()

    @override_settings(
        EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend')
    def test_add_parsticipant(self):
        data = {'name': 'Peter Pan', 'email': 'peter@gmail.com',
                'phone_number': '809', 'sex': self.sex.pk,
                'programing_level': self.level.pk,
                'current_ocupation': 'Ing', 'city': 'sm',
                'reason_assistance': 'blah blah',
                'operation_system': self.operatingSystem.pk,
                'event': self.event.pk,
                }

        uuid = str(self.event.uuid)
        response = self.client.post('/event/' + uuid + '/participant/', data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Participant.objects.count(), 1)
        # self.assertTemplateUsed(response, "forms/participant_form.html")
