from django import forms


class ContactForm(forms.Form):
    Imię = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Treść = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
