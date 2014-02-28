from django import forms

class NewsletterSignupForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email_address = forms.EmailField()
