# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from apps.event import models


class ParticipantAprovalForm(forms.ModelForm):
    class Meta:
        model = models.ParticipantApproval
        fields = ['participant']
        widgets = {'participant': forms.HiddenInput(attrs={'required': False})}


class ParticipantCancelForm(forms.ModelForm):
    class Meta:
        model = models.ParticipantCancel
        fields = ['participant', 'note']
        widgets = {'participant': forms.HiddenInput(attrs={'required': False})}


class ResendInvitationForm(forms.ModelForm):
    class Meta:
        model = models.Participant
        fields = [
            'email']
