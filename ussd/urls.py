from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r"^ussd/$", views.ussd, name="ussd-gateway"),
)
