from django import forms
from phones.models import Entry


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = 'surname', 'family_name', 'phone_number'
