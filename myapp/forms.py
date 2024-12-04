from django import forms
from .models import *
class customertform(forms.ModelForm):
    
    class Meta:
        model = customer
        fields = "__all__"
        
        
class contactform(forms.ModelForm):
    
    class Meta:
        model = contact
        fields = "__all__"
        


def claen_email(self):
    email= self.cleaned_data.get('email')
    if contact.objects.filter(email=email).exists():
        raise forms.validationError("email is already in use")
    return email
def clean_message(self):
    message=self.cleaned_data.get('message')
    if not message.isdigit() or len(message) != 10:
        raise forms.validationerror("the message must contain exactly 10 digits")
    return message