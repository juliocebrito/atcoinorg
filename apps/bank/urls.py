from django.conf.urls import patterns, url
from views import BankView, CreatePay, ListPay, DetailPay, CreateCharge, ListCharge, DetailCharge


urlpatterns = patterns('',

    url(r'^bank/$', BankView.as_view(), name='bank'),

    #urls for Pay
    url(r'^create_pay/$', CreatePay.as_view(), name='create_pay'),
    url(r'^list_pay/$', ListPay.as_view(), name='list_pay'),
    url(r'^detail_pay/(?P<pk>\d+)/$', DetailPay.as_view(), name='detail_pay'),

    #urls for Charge
    url(r'^create_charge/$', CreateCharge.as_view(), name='create_charge'),
    url(r'^list_charge/$', ListCharge.as_view(), name='list_charge'),
    url(r'^detail_charge/(?P<pk>\d+)/$', DetailCharge.as_view(), name='detail_charge'),
)
