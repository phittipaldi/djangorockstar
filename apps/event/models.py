# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from . import models_utils
import uuid
from apps.event import managers


class Slider(models.Model):
    picture = models.ImageField(
        upload_to="slider", null=True, blank=True)
    title = models.TextField()
    subtitle = models.TextField()
    btn_text = models.CharField(max_length=64)

    def __unicode__(self):
        return ''.format(self.title)


class Portal(models.Model):
    name = models.CharField(max_length=64)
    slider = models.ForeignKey(
        Slider, on_delete=models.CASCADE, blank=True, null=True)
    about_us = models.TextField(blank=True, null=True)
    title_aplication_session = models.CharField(
        max_length=64, blank=True, null=True)
    text_aplication_session = models.TextField(blank=True, null=True)
    subtext_aplication_session = models.TextField(blank=True, null=True)
    title_coach_session = models.CharField(
        max_length=64, blank=True, null=True)
    subtitle_coach_session = models.CharField(
        max_length=120, blank=True, null=True)
    text_coach_session = models.TextField(blank=True, null=True)
    title_organizer_session = models.CharField(
        max_length=64, blank=True, null=True)
    subtitle_organizer_session = models.CharField(
        max_length=120, blank=True, null=True)
    title_sponsor_session = models.CharField(
        max_length=64, blank=True, null=True)
    subtitle_sponsor_session = models.CharField(max_length=120,
                                                null=True, blank=True)
    participant_sucess = models.TextField(blank=True, null=True)
    participant_warning = models.TextField(blank=True, null=True)
    coach_success = models.TextField(blank=True, null=True)
    btn_inscription = models.CharField(max_length=30, blank=True, null=True)
    text_form_inscription_participant = models.TextField(null=True, blank=True)
    text_form_inscription_sponsor = models.TextField(null=True, blank=True)

    text_footer = models.CharField(max_length=120, null=True, blank=True)

    picture_1_application = models.ImageField(
        upload_to="portal", null=True, blank=True)
    picture_2_application = models.ImageField(
        upload_to="portal", null=True, blank=True)
    picture_bg_coach = models.ImageField(
        upload_to="portal", null=True, blank=True)

    logo = models.ImageField(
        upload_to="portal", null=True, blank=True)

    def __unicode__(self):
        return '{}'.format(self.name)


class Event(models.Model):
    portal = models.ForeignKey(
        Portal, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=64)
    about = models.TextField(blank=True, null=True)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    place = models.CharField(max_length=40, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    max_quote_participants = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4,
                            editable=False)
    logo = models.ImageField(
        upload_to="event", null=True, blank=True)
    objects = managers.EventManager()

    def __str__(self):
        return '{}'.format(self.name)

    def display_date(self):
        text = self.begin_date.strftime('%b %d, %Y, %I:%M%p - ')
        text = text + self.end_date.strftime('%I:%M%p')
        return text

    @property
    def get_organizers_emails(self):
        result = ''
        organizers = Organizer.objects.filter(
            event__pk=self.pk)
        for organizer in organizers:
            result += str(organizer.email) + ', '
        return result[:-2]


class ParticipantStatus(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return '{}'.format(self.name)


class Person(models.Model):
    event = models.ForeignKey(
        Event,
        related_name='persons',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=16)
    city = models.CharField(max_length=32)
    birthdate = models.CharField(max_length=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    picture = models.ImageField(upload_to="persons", null=True)
    is_verified = models.BooleanField(default=False)
    is_assistance_confirmated = models.BooleanField(default=False)
    sex = models.ForeignKey(
        models_utils.Sex,
        on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=False,
                            default=uuid.uuid4,
                            editable=False)

    def __str__(self):
        return '{}'.format(self.name)


class Organizer(Person):
    is_the_principal = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)


class Participant(Person):
    programing_level = models.ForeignKey(
        models_utils.ProgramingLevel,
        on_delete=models.CASCADE)
    programing_knowledge = models.TextField(null=True, blank=True)
    current_ocupation = models.TextField()
    reason_assistance = models.TextField()
    operation_system = models.ForeignKey(
        models_utils.OperatingSystem,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return '{}'.format(self.name)


class Coach(Person):

    YES_OR_NO_CHOICES = (
        ('', '-------------'),
        ('Si', 'Si'),
        ('No', 'No'),
    )

    github_user = models.CharField(max_length=120, blank=True, null=True)
    operating_systems = models.ManyToManyField(models_utils.OperatingSystem)
    agree_work_with_windows = models.CharField(
        max_length=2,
        choices=YES_OR_NO_CHOICES,
        default="KG"
    )
    languages_speak = models.ManyToManyField(models_utils.Languages)
    time_install_before_workshop = models.CharField(
        max_length=2,
        choices=YES_OR_NO_CHOICES,
        default="KG"
    )
    time_meet_before_workshop = models.CharField(
        max_length=2,
        choices=YES_OR_NO_CHOICES,
        default="KG"
    )
    experience_teaching = models.TextField(blank=True, null=True)
    want_be_add_website = models.CharField(
        max_length=2,
        choices=YES_OR_NO_CHOICES,
        default="KG"
    )


class FAQ(models.Model):

    event = models.ForeignKey(Event, related_name='faqs',
                              on_delete=models.CASCADE)
    question = models.CharField(max_length=120)
    answer = models.TextField()

    def __unicode__(self):
        return '{}'.format(self.question)
