from django.contrib.auth import logout
from django.contrib.auth.views import (LoginView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,)
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, FormView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .forms import UserRegistrationForm

class UserLoginView(LoginView):
    template_name = 'myauth/login.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile',
            kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'myauth/profile.html'
    model = User
    fields = 'first_name', 'last_name', 'username', 'email', 'bio', 'age'

    def get_success_url(self):
        return  f'/accounts/profile/{self.request.user.pk}/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserRegistrationView(FormView):
    template_name = 'myauth/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def user_logout(request):
    logout(request)
    return redirect(reverse('index'))


class UserChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'myauth/change_password.html'
    success_url = reverse_lazy('change_password_done')

class UserChangePasswordDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'myauth/change_password_done.html'

class UserPasswordResetView(PasswordResetView):
    template_name = 'myauth/reset_password.html'
    success_url = reverse_lazy('reset_password_done')

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'myauth/reset_password_done.html'
#
class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'myauth/reset_password_confirm.html'
    success_url = reverse_lazy('reset_password_complete')

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'myauth/reset_password_complete.html'