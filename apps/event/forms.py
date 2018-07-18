# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from . import models


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = models.Participant
        fields = [
            'name', 'email', 'phone_number', 'city', 'birthdate',
            'programing_knowledge', 'current_ocupation', 'reason_assistance',
            'event', 'operation_system', 'programing_level', 'sex']
        widgets = {'event': forms.HiddenInput(attrs={'required': False})}
