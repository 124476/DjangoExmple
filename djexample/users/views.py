from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import FormView
import django.views

from users.forms import UserForm, DFEmailForm
from users.models import User


class AccountView(LoginRequiredMixin, FormView):
    template_name = "users/profile.html"
    form_class = UserForm

    def get_initial(self):
        return {
            "username": self.request.user.username,
            "email": self.request.user.email,
            "avatar": self.request.user.avatar,
        }

    def post(self, request, *args, **kwargs):
        post = request.POST.copy()
        post["email"] = request.user.email
        user_form = UserForm(post, request.FILES, instance=request.user)
        new_username = user_form.cleaned_data.get("username")

        if new_username != request.user.username:
            if user_form.is_valid():
                if User.objects.filter(username=new_username).exists():
                    user_form.add_error(
                        "username",
                        _("username_is_already_taken"),
                    )
        elif user_form.is_valid():
            user_form.save()
            return redirect("users:profile")

        return render(request, "users/profile.html", {"form": user_form})


class EmailChangeView(LoginRequiredMixin, django.views.View):
    template_name = "users/email_change.html"
    form_class = DFEmailForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={'email': request.user.email})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            new_email = form.cleaned_data['email']
            if request.user.email != new_email:
                request.user.email = new_email
                request.user.save()
                return redirect('users:profile')
        return render(request, self.template_name, {'form': form})


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    pass
