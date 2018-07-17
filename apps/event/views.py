# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from . import models
from . import forms
from django.urls.base import reverse


class EventDetail(DetailView):
    model = models.Event
    template_name = "index_event.html"
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'


class Events(ListView):
    models = models.Event
    template_name = "events.html"

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        if self.object_list.count() > 1:
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            if self.object_list.count() == 1:
                event = self.object_list[0]
                return redirect('event-detail', uuid=event.uuid)

    def get_queryset(self):
        queryset = self.models.objects.all_active_events()
        return queryset


class ParticipantCreateView(CreateView):
    form_class = forms.ParticipantForm
    template_name = 'forms/participant_form.html'
    model = models.Participant

    def get_context_data(self, **kwargs):
        context = super(ParticipantCreateView, self).get_context_data(**kwargs)
        event = models.Event.objects.get(
            uuid=self.kwargs.get('uuid'))
        context['event'] = event
        return context

    def get_initial(self):
        event = models.Event.objects.get(
            uuid=self.kwargs.get('uuid'))
        return {'event': event.pk}

    def get_success_url(self):
        return reverse('event:participant-success',
                       kwargs={'uuid': self.object.uuid})


class ParticipantSuccessView(DetailView):
    template_name = 'forms/participant_success.html'
    model = models.Participant
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super(
            ParticipantSuccessView, self).get_context_data(**kwargs)
        context['event'] = self.get_object().event
        return context
