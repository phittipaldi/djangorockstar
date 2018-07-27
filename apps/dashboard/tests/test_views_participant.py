from . import base
from apps.event.tests import factories
from apps.dashboard.models import MenuOption


class ParticipantListViewTest(base.UnitTest):

    def test_with_several_participant_with_different_status(self):

        participant1 = factories.ParticipantFactory(
            status=self.status_pendiente, event=self.event)
        participant2 = factories.ParticipantFactory(
            status=self.status_aprobado, event=self.event)
        participant3 = factories.ParticipantFactory(
            status=self.status_desestimado, event=self.event)

        response = self.client.get(self.url_participant_list)

        self.assertEqual(200, response.status_code)

        self.assertContains(response, participant1.status.name)
        self.assertContains(response, participant2.status.name)
        self.assertContains(response, participant3.status.name)

    def test_view_only_participants_event_organizer(self):
        self.other_event = factories.EventFactory(name='RockStar Santiago')
        participant1 = factories.ParticipantFactory(
            status=self.status_pendiente, event=self.other_event)

        response = self.client.get(self.url_participant_list)

        self.assertEqual(200, response.status_code)

        self.assertNotContains(response, participant1.status.name)

    def test_options_display_by_status_pendiente(self):
        participant1 = factories.ParticipantFactory(
            status=self.status_pendiente, event=self.event)

        display_options = {'Aprobar': 'Aprobar', 'Desestimar': 'Desestimar',
                           'Ver Formulario': 'Ver Formulario'}

        for current in participant1.get_options_menu_list:
            self.assertEqual(current.name, display_options[current.name])

    def test_options_display_by_status_aprobado(self):
        participant1 = factories.ParticipantFactory(
            status=self.status_aprobado, event=self.event)

        display_options = {'Reenviar Invitación': 'Reenviar Invitación',
                           'Ver Formulario': 'Ver Formulario',
                           'Ver Invitación': 'Ver Invitación'}

        for current in participant1.get_options_menu_list:
            self.assertEqual(current.name, display_options[current.name])

    def test_options_display_by_status_desestimado(self):
        participant1 = factories.ParticipantFactory(
            status=self.status_desestimado, event=self.event)

        display_options = {'Ver Formulario': 'Ver Formulario'}

        for current in participant1.get_options_menu_list:
            self.assertEqual(current.name, display_options[current.name])
