from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from braces.views import AnonymousRequiredMixin, FormValidMessageMixin, LoginRequiredMixin, MessageMixin
from django.views.generic import (View, FormView, TemplateView, RedirectView,
                                  CreateView, ListView, DetailView, UpdateView, DeleteView)
from .models import Account, Pay, Charge
from .forms import PayForm


class BankView(TemplateView):
    template_name = 'bank.html'

    def get_context_data(self, **kwargs):
        context = super(BankView, self).get_context_data(**kwargs)
        context['accounts'] = Account.objects.all()
        context['pays'] = Pay.objects.all()
        return context

""" Views for Pay """

class CreatePay(CreateView):
    form_class = PayForm
    template_name = 'create_pay.html'
    success_url = reverse_lazy('list_pay')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.account = Account.objects.get(pk=self.kwargs['pk'])
        return super(CreatePay, self).form_valid(form)


class ListPay(ListView):
    model = Pay
    template_name = 'list_pay.html'


class DetailPay(DetailView):
    model = Pay
    template_name = 'detail_pay.html'


""" Views for Charge """

class CreateCharge(CreateView):
    form_class = PayForm
    template_name = 'create_charge.html'
    success_url = reverse_lazy('list_charge')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.account = Account.objects.get(pk=self.kwargs['pk'])
        return super(CreateCharge, self).form_valid(form)


class ListCharge(ListView):
    model = Charge
    template_name = 'list_charge.html'


class DetailCharge(DetailView):
    model = Charge
    template_name = 'detail_charge.html'