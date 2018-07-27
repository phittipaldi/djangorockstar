import factory
from datetime import datetime
from faker import Factory
from apps.security.tests.factories import UserFactory

faker = Factory.create()


class ListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dashboard.List'
        django_get_or_create = ('name',)

    name = 'ListadoParticipante'


class MenuOptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dashboard.MenuOption'
        django_get_or_create = ('name', 'list',)

    name = 'ListadoParticipante'
    list = ListFactory()
    url = factory.LazyAttribute(lambda _: faker.word())
    target = factory.LazyAttribute(lambda _: faker.word())
    icono = factory.LazyAttribute(lambda _: faker.word())
    order = 1


class MenuOptionStatusNotAllowedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dashboard.MenuOptionStatusNotAllowed'
        django_get_or_create = ('status', 'option')

    option = MenuOptionFactory()
    status = 'Pendiente'
