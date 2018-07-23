from django.conf.urls import url, include
from . import views as core
from django.contrib.auth import views

urlpatterns = [
    url(r'^login/$', views.login,
        {'template_name': 'security/login.html'},
        name='login'),
    url(r'^logout/$', core.LogoutView.as_view(),
        name='logout'),

    url('^password_reset/$',
        views.PasswordResetView.as_view(
            html_email_template_name='security/mail/password_reset_email.html',
            subject_template_name='security/mail/password_reset_subject.txt',
            template_name='security/password_reset_form.html'),
        name='password_reset'),

    url('^password_reset/done/$',
        views.PasswordResetDoneView.as_view(
            template_name='security/password_reset_done.html'),
        name='password_reset_done'),

    url('^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmView.as_view(
            template_name='security/password_reset_confirm.html'),
        name='password_reset_confirm'),

    url('^reset/done/$',
        views.PasswordResetCompleteView.as_view(
            template_name='security/password_reset_complete.html'),
        name='password_reset_complete'),
    url('^', include('django.contrib.auth.urls')),
]
