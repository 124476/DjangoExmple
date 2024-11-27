import django.contrib.auth


class SignUpForm(django.contrib.auth.forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta(django.contrib.auth.forms.UserCreationForm.Meta):
        model = django.contrib.auth.models.User
        fields = [
            django.contrib.auth.models.User.email.field.name,
            django.contrib.auth.models.User.username.field.name,
            "password1",
            "password2",
        ]
