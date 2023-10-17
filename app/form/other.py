from django import forms

from app.models import Contact


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()
