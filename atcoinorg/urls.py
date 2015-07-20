from django.conf.urls import include, url
from django.contrib import admin
from apps.users import urls as users_urls
from apps.bank import urls as bank_urls
from apps.entry import urls as entry_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(users_urls)),
    url(r'^', include(bank_urls)),
    url(r'^', include(entry_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
