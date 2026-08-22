from django import forms
from .models import ContactUs
from django.core.validators import ValidationError
import re


class ContactUsForm(forms.ModelForm):
    
    class Meta :
        model = ContactUs
        fields = "__all__"
        widgets={
            "name":forms.TextInput(attrs={
                "class" : "col-lg-12",
                "placeholder" : "نام شما...",
                "autocomplete" : "on"
            }),
            "phone_number":forms.TextInput(attrs={
                "class" : "col-lg-12",
                "placeholder" : "شماره تلفن شما..."
            }),
            "email": forms.EmailInput(attrs={
                "class" : "col-lg-12",
                "placeholder" : "ایمیل شما..."
            }),
            "text" : forms.TextInput(attrs={
                "class" : "col-lg-12",
                "placeholder" : "پیام یا درخواست خود را بنویسید..."
            })
        }
    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        if not re.match(r'^09\d{9}$', phone):
            raise ValidationError("شماره تلفن باید با ۰۹ شروع شود و ۱۱ رقم باشد.", code="invalid_number")
        return phone