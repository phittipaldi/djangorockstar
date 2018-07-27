import factory
from faker import Factory

faker = Factory.create()


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'auth.Group'

    # name = factory.Sequence(lambda n: "Group #%s" % n)
    name = 'Organizer'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'auth.User'  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('username',)

    username = 'djangorockstar'
    password = factory.PostGenerationMethodCall('set_password', '12345678')
    email = faker.email()

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.groups.add(group)
