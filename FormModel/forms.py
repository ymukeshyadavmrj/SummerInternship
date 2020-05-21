from django import forms
from FormModel.models import User

class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
