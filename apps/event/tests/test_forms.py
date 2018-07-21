from django.test import TestCase
from . import factories
from ..forms import ParticipantForm


class ParticipantFormTest(TestCase):

    def setUp(self):
        self.portal = factories.PortalFactory()
        self.operatingSystem = factories.OperatingSystemFactory()
        self.sex = factories.SexFactory()
        self.level = factories.ProgramingLevelFactory()
        self.event = factories.EventFactory()

    # Valid Form Data
    def test_form_participant_valid(self):
        form = ParticipantForm({'name': 'Peter Pan',
                                'email': 'peter@gmail.com',
                                'phone_number': '809', 'sex': self.sex.pk,
                                'programing_level': self.level.pk,
                                'current_ocupation': 'Ing', 'city': 'sm',
                                'reason_assistance': 'blah blah',
                                'operation_system': self.operatingSystem.pk,
                                'event': self.event.pk,
                                })

        self.assertTrue(form.is_valid())

    def test_form_participant_invalid(self):
        form = ParticipantForm({'name': 'Peter Pan',
                                'email': 'peter@gmail',
                                'phone_number': '809', 'sex': self.sex.pk,
                                'programing_level': self.level.pk,
                                'current_ocupation': 'Ing', 'city': 'sm',
                                'reason_assistance': 'blah blah',
                                'operation_system': self.operatingSystem.pk,
                                'event': self.event.pk,
                                })

        self.assertFalse(form.is_valid())
