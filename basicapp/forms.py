from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("Name needs to start with z!")

class FormName(forms.Form):
    name = forms.CharField(validators = [check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="enter again email")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget = forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)] )


    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise fomrs.ValidationError("Gotta bot!!!")

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails matches")
