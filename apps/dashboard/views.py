# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views.generic import TemplateView, ListView, CreateView, FormView
from apps.event import models
from apps.security.mixin.views import (GroupsRequiredMixin)
from . import forms
from django.http.response import HttpResponseForbidden


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
        event = models.Organizer.objects.get(
            user=self.request.user).event
        context['event'] = event
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
        event = models.Organizer.objects.get(
            user=self.request.user).event
        context['event'] = event
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


class CancelParticipant(LoginRequiredMixin,
                        GroupsRequiredMixin,
                        CreateView):

    form_class = forms.ParticipantCancelForm
    template_name = 'dashboard/participant-cancel.html'
    model = models.ParticipantCancel
    user_check_failure_path = '/accounts/permission_denied/'
    required_groups = ('Organizer',)

    def get_context_data(self, **kwargs):
        context = super(CancelParticipant, self).get_context_data(**kwargs)
        participant = models.Participant.objects.get(
            uuid=self.kwargs.get('uuid'))
        context['participant'] = participant
        context['event'] = participant.event
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        participant = models.Participant.objects.get(
            uuid=self.kwargs.get('uuid'))
        participant.set_status_desestimado()
        participant.send_cancel_participant(participant.email)
        return super(CancelParticipant, self).form_valid(form)

    def get_initial(self):
        participant = models.Participant.objects.get(
            uuid=self.kwargs.get('uuid'))
        return {'participant': participant.pk}

    def get_success_url(self):
        return reverse('dashboard:participants-pending')


class ResendInvitationParticipant(LoginRequiredMixin, FormView):
    template_name = 'dashboard/modals/content_resend_invitation.html'
    form_class = forms.ResendInvitationForm
    model = models.Participant

    def __init__(self, *args, **kwargs):
        super(ResendInvitationParticipant, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(
            ResendInvitationParticipant, self).get_context_data(**kwargs)
        participant = models.Participant.objects.get(
            uuid=self.kwargs.get('uuid'))
        context['participant'] = participant
        context['event'] = participant.event
        return context

    def post(self, request, *args, **kwargs):
        participant = models.Participant.objects.get(
            uuid=self.kwargs.get('uuid'))
        participant.send_invitation(request.POST['email'])
        return super(ResendInvitationParticipant, self).get(
            request, args, **kwargs)

    def get(self, request, *args, **kwargs):
        response = super(ResendInvitationParticipant, self).get(
            request, *args, **kwargs)
        if self.request.is_ajax():
            return response
        return HttpResponseForbidden()

    def get_initial(self):
        participant = models.Participant.objects.get(
            uuid=self.kwargs.get('uuid'))
        return {'email': participant.email}

    def get_success_url(self):
        return reverse('budget:accounts_sync_file',
                       kwargs={'account_pk': self.get_object().account.id})
