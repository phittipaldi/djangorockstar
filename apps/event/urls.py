from django.urls import path

from . import views

urlpatterns = [
    path('', views.Events.as_view(), name='event-list'),
    path('index/<uuid:uuid>/', views.EventDetail.as_view(),
         name='event-detail'),
    path('<uuid:uuid>/participant/', views.ParticipantCreateView.as_view(),
         name='participant'),
    path('participant/<uuid:uuid>/success/',
         views.ParticipantSuccessView.as_view(),
         name='participant-success'),
]
