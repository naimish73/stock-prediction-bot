from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

html_class='shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':html_class})
        self.fields['email'].widget.attrs.update({'class':html_class})
        self.fields['password1'].widget.attrs.update({'class':html_class})
        self.fields['password2'].widget.attrs.update({'class':html_class})

