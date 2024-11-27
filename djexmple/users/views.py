import django.views

import users.forms


class Registration(django.views.View):
    form_class = users.forms.SignUpForm
    template_name = "users/signup.html"

    def get(self, request):
        form = users.forms.SignUpForm()
        context = {
            "form": form,
        }
        return django.shortcuts.render(request, self.template_name, context)

    def post(self, request):
        form = users.forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return django.shortcuts.redirect("users:login")
        context = {"form": form}
        return django.shortcuts.render(request, self.template_name, context)
