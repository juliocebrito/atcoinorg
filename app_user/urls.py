from django.conf.urls import patterns, url
from views import (IndexView, SigninView, LoginView, LoginFacebookView, LogoutView,
                   DetailProfile, UpdateProfile)

urlpatterns = patterns('',

    url(r'^$', IndexView.as_view(), name='index'),

    #urls for Authenticate
    url(r'^signin/$', SigninView.as_view(), name='signin'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^loginfacebook/$', LoginFacebookView.as_view(), name='loginfacebook'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    #urls for Profile
    url(r'^detailprofile/(?P<slug>[-\w]+)/$', DetailProfile.as_view(), name='detailprofile'),
    url(r'^updateprofile/(?P<slug>[-\w]+)/$', UpdateProfile.as_view(), name='updateprofile')
)