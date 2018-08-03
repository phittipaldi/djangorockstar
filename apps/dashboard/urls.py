# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('participants/', views.ListPendingParticipant.as_view(),
         name='participants-pending'),
    path('participants/_/<uuid:uuid>/success/',
         views.ListPendingParticipant.as_view(),
         name='participants-success'),
    path('participant/_/<uuid:uuid>/approval/',
         views.AprovalParticipant.as_view(),
         name='participant-approval'),
    path('participant/_/<uuid:uuid>/cancel/',
         views.CancelParticipant.as_view(),
         name='participant-cancel'),
    path('participant/_/<uuid:uuid>/resend-invitation/',
         views.ResendInvitationParticipant.as_view(),
         name='resend-invitation'),
]
