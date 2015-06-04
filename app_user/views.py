from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from braces.views import AnonymousRequiredMixin, FormValidMessageMixin, LoginRequiredMixin, MessageMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import (View, FormView, TemplateView, RedirectView,
                                  CreateView, ListView, DetailView, UpdateView, DeleteView)
from .models import Profile
from .forms import SignupForm, LoginForm, ProfileForm
from django.conf import settings
import facebook


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/listentry/')
        else:
            cookie = facebook.get_user_from_cookie(self.request.COOKIES,
                                                   settings.FACEBOOK_APP_ID,
                                                   settings.FACEBOOK_APP_SECRET)
            if not cookie:
                return super(IndexView, self).get(request, *args, **kwargs)
            else:
                try:
                    user = User.objects.get(username=cookie['uid'])
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(self.request, user)
                    return redirect('/listentry/')
                except User.DoesNotExist:
                    graph = facebook.GraphAPI(cookie["access_token"])
                    data = graph.get_object("me")
                    user = User.objects.create_user(
                        username=data["id"],
                        first_name=data["first_name"],
                        last_name=data["last_name"],
                        email=data["email"]
                    )
                    profile = Profile.objects.get(user_id=user.pk)
                    profile.first_name = data["first_name"]
                    profile.last_name = data["last_name"]
                    profile.email = data["email"]
                    profile.save()
                    if user is not None and user.is_active:
                        user.backend = 'django.contrib.auth.backends.ModelBackend'
                        login(self.request, user)
                    return redirect('/listentry/')



class SigninView(FormValidMessageMixin,
                 CreateView):
    form_class = SignupForm
    form_valid_message = 'Thanks for signing up, go ahead and login.'
    model = User
    template_name = 'signin.html'
    success_url = reverse_lazy('index')


class LoginView(FormValidMessageMixin,
                FormView):
    form_class = LoginForm
    form_valid_message = 'You are logged in, create an entry.'
    template_name = 'login.html'
    success_url = reverse_lazy('listentry')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class SignupFacebookView(RedirectView):
    pass


class LoginFacebookView(TemplateView):
    template_name = 'loginfacebook.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(LoginFacebookView, self).get(request, *args, **kwargs)
        else:
            cookie = facebook.get_user_from_cookie(self.request.COOKIES,
                                                   settings.FACEBOOK_APP_ID,
                                                   settings.FACEBOOK_APP_SECRET)
            if not cookie:
                return super(LoginFacebookView, self).get(request, *args, **kwargs)
            else:
                try:
                    user = User.objects.get(username=cookie['uid'])
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login(self.request, user)
                    return super(LoginFacebookView, self).get(request, *args, **kwargs)
                except User.DoesNotExist:
                    graph = facebook.GraphAPI(cookie["access_token"])
                    data = graph.get_object("me")
                    user = User.objects.create_user(
                        username=data["id"],
                        first_name=data["first_name"],
                        last_name=data["last_name"]
                    )
                    profile = Profile.objects.get(user_id=user.pk)
                    profile.name = data["name"]
                    profile.first_name = data["first_name"]
                    profile.last_name = data["last_name"]
                    profile.email = data["email"]
                    profile.save()
                    if user is not None and user.is_active:
                        user.backend = 'django.contrib.auth.backends.ModelBackend'
                        login(self.request, user)
                    return super(LoginFacebookView, self).get(request, *args, **kwargs)


class LogoutView(MessageMixin,
                 RedirectView):
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        self.messages.success("You've been logged out. Come back soon!")
        return super(LogoutView, self).get(request, *args, **kwargs)


""" Views for Profile """


class DetailProfile(DetailView):
    model = Profile
    template_name = 'detailprofile.html'


class UpdateProfile(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'updateprofile.html'

    def get_success_url(self):
        return reverse('detailprofile', kwargs={'slug':self.kwargs['slug']})