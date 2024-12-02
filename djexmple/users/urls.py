from allauth.account.views import ConfirmEmailView
from allauth.account.views import EmailVerificationSentView
from allauth.account.views import EmailView
from allauth.account.views import LoginView
from allauth.account.views import LogoutView
from allauth.account.views import PasswordChangeView
from allauth.account.views import PasswordResetDoneView
from allauth.account.views import PasswordResetFromKeyDoneView
from allauth.account.views import PasswordResetFromKeyView
from allauth.account.views import PasswordResetView
from allauth.account.views import SignupView
from django.urls import path, re_path, reverse_lazy

from users import forms
from users import views


app_name = "users"

urlpatterns = [
    path(
        "account/",
        views.AccountView.as_view(),
        name="profile",
    ),
    path(
        "singup/",
        SignupView.as_view(
            form_class=forms.DFSignupForm,
            template_name="users/signup.html",
        ),
        name="signup",
    ),
    path(
        "login/",
        LoginView.as_view(
            form_class=forms.DFLoginForm,
            template_name="users/login.html",
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path(
        "email/",
        views.EmailChangeView.as_view(),
        name="email_change",
    ),
    path(
        "password/change/",
        PasswordChangeView.as_view(
            form_class=forms.DFChangePasswordForm,
            template_name="users/password_change.html",
            success_url=reverse_lazy("users:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password/change/done/",
        views.PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html",
        ),
        name="password_change_done",
    ),
]
