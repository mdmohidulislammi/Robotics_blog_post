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

class User_Creation(BWFormMixin, UserCreationForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email','is_active',  'is_staff', 'is_superuser', 'groups',)
    def clean_username(self): 
        username = self.cleaned_data['username'] 
        qs = User.objects.filter(username=username).exclude(pk=self.instance.pk) 
        if qs.exists(): 
            raise forms.ValidationError("This username is already taken.") 
        return username