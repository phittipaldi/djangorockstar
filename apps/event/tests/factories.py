import factory
from datetime import datetime
from faker import Factory
from apps.security.tests.factories import UserFactory

faker = Factory.create()


class SexFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'event.Sex'
        django_get_or_create = ('name',)

    name = 'Masculino'


class OperatingSystemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'event.OperatingSystem'
        django_get_or_create = ('name',)

    name = 'Windows'


class ProgramingLevelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'event.ProgramingLevel'
        django_get_or_create = ('name',)

    name = 'Intermedio'


class LanguagesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'event.Languages'
        django_get_or_create = ('name',)

    name = 'Ingles'


class PortalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'event.Portal'
        django_get_or_create = (
            'name',)

    name = 'Python Dominicana'


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'event.Event'

    name = faker.name()
    portal = factory.SubFactory(PortalFactory)
    begin_date = datetime.now().replace(hour=23, minute=59)
    end_date = datetime.now().replace(hour=23, minute=59)


class PortalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'event.Portal'
        django_get_or_create = (
            'name',)

    name = 'Python Dominicana'


class ParticipantStatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'event.ParticipantStatus'
        django_get_or_create = (
            'name',)

    name = 'Pendiente'


class ParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'event.Participant'

    name = faker.name()
    email = faker.email()
    phone_number = factory.LazyFunction(faker.phone_number)
    sex = factory.SubFactory(SexFactory)
    programing_level = factory.SubFactory(ProgramingLevelFactory)
    reason_assistance = faker.text()
    operation_system = factory.SubFactory(OperatingSystemFactory)
    event = factory.SubFactory(EventFactory)
    status = factory.SubFactory(ParticipantStatusFactory)


class OrganizerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'event.Organizer'

    user = factory.SubFactory(UserFactory)
    name = faker.name()
    email = faker.email()
    phone_number = factory.LazyFunction(faker.phone_number)
    sex = factory.SubFactory(SexFactory)
    event = factory.SubFactory(EventFactory)
