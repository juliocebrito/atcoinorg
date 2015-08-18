from django.conf.urls import patterns, url
from views import (HomeView, CreateEntry, ListEntry, DetailEntry, UpdateEntry, DeleteEntry, CampaignEntry,
                   CreateComment, UpdateComment, DeleteComment)

urlpatterns = patterns('',

    url(r'^home/$', HomeView.as_view(), name='home'),

    #urls for Entry
    url(r'^createentry/$', CreateEntry.as_view(), name='createentry'),
    url(r'^listentry/$', ListEntry.as_view(), name='listentry'),
    url(r'^detailentry/(?P<slug>[-\w]+)/$', DetailEntry.as_view(), name='detailentry'),
    url(r'^updateentry/(?P<slug>[-\w]+)/$', UpdateEntry.as_view(), name='updateentry'),
    url(r'^deleteentry/(?P<slug>[-\w]+)/$', DeleteEntry.as_view(), name='deleteentry'),
    url(r'^campaignentry/(?P<slug>[-\w]+)/$', CampaignEntry.as_view(), name='campaignentry'),
    #urls for Comment
    url(r'^createcomment/(?P<slug>[-\w]+)/$', CreateComment.as_view(), name='createcomment'),
    url(r'^updatecomment/(?P<pk>\d+)/$', UpdateComment.as_view(), name='updatecomment'),
    url(r'^deletecomment/(?P<pk>\d+)/$', DeleteComment.as_view(), name='deletecomment'),
)
