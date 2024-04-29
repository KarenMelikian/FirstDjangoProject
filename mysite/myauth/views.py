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
    """
    View for user login.

    This view handles user authentication and redirects to the user's profile upon successful login.

    Attributes:
        template_name (str): The template to render for the login form.
    """
    template_name = 'myauth/login.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, UpdateView):
    """
    View for user profile.

    This view allows users to view and update their profile information.

    Attributes:
        template_name (str): The template to render for the user profile page.
        model (Model): The User model.
        fields (tuple): The fields to display in the user profile form.
    """
    template_name = 'myauth/profile.html'
    model = User
    fields = 'first_name', 'last_name', 'username', 'email', 'bio', 'age', 'image'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserRegistrationView(FormView):
    """
    View for user registration.

    This view allows users to register a new account.

    Attributes:
        template_name (str): The template to render for the registration form.
        form_class (Form): The form class for user registration.
        success_url (str): The URL to redirect to upon successful registration.
    """
    template_name = 'myauth/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def user_logout(request):
    """
    View for user logout.

    This view logs out the current user and redirects to the home page.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponseRedirect: Redirects to the home page.
    """
    logout(request)
    return redirect(reverse('index'))


class UserChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    """
    View for changing user password.

    This view allows users to change their password.

    Attributes:
        template_name (str): The template to render for the change password form.
        success_url (str): The URL to redirect to upon successful password change.
    """
    template_name = 'myauth/change_password.html'
    success_url = reverse_lazy('change_password_done')

class UserChangePasswordDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    """
    View for successful password change.

    This view displays a success message after the user changes their password.

    Attributes:
        template_name (str): The template to render for the success message.
    """
    template_name = 'myauth/change_password_done.html'

class UserPasswordResetView(PasswordResetView):
    """
    View for password reset.

    This view allows users to request a password reset.

    Attributes:
        template_name (str): The template to render for the password reset form.
        success_url (str): The URL to redirect to upon successful password reset request.
    """
    template_name = 'myauth/reset_password.html'
    success_url = reverse_lazy('reset_password_done')

class UserPasswordResetDoneView(PasswordResetDoneView):
    """
    View for successful password reset request.

    This view displays a success message after the user requests a password reset.

    Attributes:
        template_name (str): The template to render for the success message.
    """
    template_name = 'myauth/reset_password_done.html'

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    """
    View for password reset confirmation.

    This view allows users to confirm their password reset.

    Attributes:
        template_name (str): The template to render for the password reset confirmation form.
        success_url (str): The URL to redirect to upon successful password reset confirmation.
    """
    template_name = 'myauth/reset_password_confirm.html'
    success_url = reverse_lazy('reset_password_complete')

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    """
    View for successful password reset.

    This view displays a success message after the user resets their password.

    Attributes:
        template_name (str): The template to render for the success message.
    """
    template_name = 'myauth/reset_password_complete.html'
