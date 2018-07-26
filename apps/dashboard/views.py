# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views.generic import TemplateView, ListView, CreateView
from apps.event import models
from apps.security.mixin.views import (GroupsRequiredMixin)
from . import forms
# from apps.event.views_service import ParticipantService


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"


class ListPendingParticipant(LoginRequiredMixin,
                             GroupsRequiredMixin,
                             ListView):
    template_name = 'dashboard/pending-participants.html'
    model = models.Participant
    user_check_failure_path = '/accounts/permission_denied/'
    required_groups = ('Organizer',)

    def get_context_data(self, **kwargs):
        context = super(
            ListPendingParticipant, self).get_context_data(**kwargs)
        if self.kwargs.get('uuid'):
            participant = models.Participant.objects.get(
                uuid=self.kwargs.get('uuid'))
            context['participant'] = participant
        return context

    def get_queryset(self):
        event = models.Organizer.objects.get(
            user=self.request.user).event
        queryset = self.model.objects.filter(
            event__pk=event.pk).order_by('status__order').reverse()
        return queryset


class AprovalParticipant(LoginRequiredMixin,
                         GroupsRequiredMixin,
                         CreateView):

    form_class = forms.ParticipantAprovalForm
    template_name = 'dashboard/participant-approval.html'
    model = models.ParticipantApproval
    user_check_failure_path = '/accounts/permission_denied/'
    required_groups = ('Organizer',)

    def get_context_data(self, **kwargs):
        context = super(AprovalParticipant, self).get_context_data(**kwargs)
        participant = models.Participant.objects.get(
            uuid=self.kwargs.get('uuid'))
        context['participant'] = participant
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        participant = models.Participant.objects.get(
            uuid=self.kwargs.get('uuid'))
        participant.set_status_aprobado()
        participant.send_invitation(participant.email)

        return super(AprovalParticipant, self).form_valid(form)

    def get_initial(self):
        participant = models.Participant.objects.get(
            uuid=self.kwargs.get('uuid'))
        return {'participant': participant.pk}

    def get_success_url(self):
        return reverse('dashboard:participants-success',
                       kwargs={'uuid': self.kwargs.get('uuid')})
