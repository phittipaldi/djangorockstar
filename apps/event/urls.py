from django.urls import path

from . import views

urlpatterns = [
    path('index/<uuid:uuid>/', views.IndexEvent.as_view(), name='event'),
    path('index/', views.IndexEvent.as_view(), name='event'),
]
