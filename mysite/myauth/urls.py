from django.urls import path

from .views import (
    UserLoginView,
    UserProfileView,
    user_logout,
    UserChangePasswordView,
    UserChangePasswordDoneView,
    UserPasswordResetView,
    UserPasswordResetDoneView,
    UserPasswordResetConfirmView,
    UserPasswordResetCompleteView,
    UserRegistrationView
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('logout/', user_logout, name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('change-password/', UserChangePasswordView.as_view(), name='change_password'),
    path('change-password-done/', UserChangePasswordDoneView.as_view(), name='change_password_done'),
    path('reset-password/', UserPasswordResetView.as_view(), name='reset_password'),
    path('reset-password-done/', UserPasswordResetDoneView.as_view(), name='reset_password_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         UserPasswordResetCompleteView.as_view(),
         name='reset_password_complete'),

]