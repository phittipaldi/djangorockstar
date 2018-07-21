import factory
from datetime import datetime


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

    name = 'Python Punta Cana'
    portal = factory.SubFactory(PortalFactory)
    begin_date = datetime.now().replace(hour=23, minute=59)
    end_date = datetime.now().replace(hour=23, minute=59)
