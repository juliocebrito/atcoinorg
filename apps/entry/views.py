from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from braces.views import AnonymousRequiredMixin, FormValidMessageMixin, LoginRequiredMixin, MessageMixin
from django.views.generic import (View, FormView, TemplateView, RedirectView,
                                  CreateView, ListView, DetailView, UpdateView, DeleteView)
from .models import Entry, Comment
from .forms import EntryForm, CommentForm

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['entries'] = Entry.objects.all()
        context['comments'] = Comment.objects.all()
        return context


class CreateEntry(FormValidMessageMixin,
                  CreateView):
    form_class = EntryForm
    form_valid_message = 'created succesful.'
    template_name = 'createentry.html'
    success_url = reverse_lazy('listentry')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateEntry, self).form_valid(form)


class ListEntry(ListView):
    model = Entry
    login_url = reverse_lazy('index')
    template_name = 'listentry.html'


class DetailEntry(DetailView):
    model = Entry
    template_name = 'detailentry.html'


class UpdateEntry(FormValidMessageMixin,
                  UpdateView):
    model = Entry
    form_class = EntryForm
    form_valid_message = 'updated succesful.'
    template_name = 'updateentry.html'
    success_url = reverse_lazy('listentry')


class DeleteEntry(FormValidMessageMixin,
                  DeleteView):
    model = Entry
    form_valid_message = 'deleted.'
    template_name = 'deleteentry.html'
    success_url = reverse_lazy('listentry')


class CampaignEntry(DetailView):
    model = Entry
    template_name = 'campaignentry.html'


""" Views for Comment """


class CreateComment(CreateView):
    form_class = CommentForm
    model = Entry
    template_name = 'createcomment.html'
    success_url = reverse_lazy('listentry')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.entry = Entry.objects.get(slug=self.kwargs['slug'])
        return super(CreateComment, self).form_valid(form)


class UpdateComment(FormValidMessageMixin,
                    UpdateView):
    model = Comment
    form_class = CommentForm
    form_valid_message = 'updated succesful.'
    template_name = 'updatecomment.html'
    success_url = reverse_lazy('listentry')


class DeleteComment(FormValidMessageMixin,
                    DeleteView):
    model = Comment
    form_valid_message = 'deleted.'
    template_name = 'deletecomment.html'
    success_url = reverse_lazy('listentry')