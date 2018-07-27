# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('participants/', views.ListPendingParticipant.as_view(),
         name='participants-pending'),
    path('participants/<uuid:uuid>/success/',
         views.ListPendingParticipant.as_view(),
         name='participants-success'),
    path('participant/<uuid:uuid>/approval/',
         views.AprovalParticipant.as_view(),
         name='participant-approval'),
    path('participant/<uuid:uuid>/cancel/',
         views.AprovalParticipant.as_view(),
         name='participant-cancel'),
]
