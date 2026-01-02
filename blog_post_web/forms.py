from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class BWFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": (
                    "w-full px-4 py-2 "
                    "bg-black text-white "
                    "border border-gray-600 rounded-md "
                    "placeholder-gray-400 "
                    "focus:outline-none focus:ring-2 focus:ring-white "
                    "transition"
                    "placeholder:"
                )
            })
            if "placeholder" not in field.widget.attrs:
                field.widget.attrs["placeholder"] = field.label or name.replace("_", " ").title()

class Registration_Form(BWFormMixin, UserCreationForm):
    full_name = forms.CharField(max_length=100, label="Full Name")

    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        full_name = self.cleaned_data.get('full_name')
        if full_name:
            parts = full_name.strip().split(' ', 1)
            user.first_name = parts[0]
            user.last_name = parts[1] if len(parts) > 1 else ''
        if commit:
            user.save()
        return user



class Login_Form(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                "class": "w-full px-3 py-2 rounded-md border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:outline-none text-black"
            })
