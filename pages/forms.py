from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=40, widget=forms.TextInput(attrs={'placeholder': ' Full Name.'}))
    email = forms.CharField(label='Email:', max_length=40, widget=forms.TextInput(attrs={'placeholder': ' Email Address.'}))
    phone = forms.CharField(label='Phone:', max_length=40, widget=forms.TextInput(attrs={'placeholder': ' Phone Number.'}))
    subject = forms.CharField(label='Subject:', max_length=100, widget=forms.TextInput(attrs={'placeholder': ' Subject.'}))
    message = forms.CharField(label='Message:', widget=forms.TextInput(attrs={'placeholder': ' Message.'}))
