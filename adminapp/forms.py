from django import forms
from .models import register



class registerForm(forms.ModelForm):
        class Meta:
            model =register
            fields = "__all__"
            labels = {"name": "Full Name", "gender": "Gender", "email": "Email", "contact": "Phone Number"}