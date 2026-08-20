from django import forms
from .models import ContactUs



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
            "email": forms.EmailInput(attrs={
                "class" : "col-lg-12",
                "placeholder" : "ایمیل شما..."
                
            }),
            "text" : forms.TextInput(attrs={
                "class" : "col-lg-12",
                "placeholder" : "پیام یا درخواست خود را بنویسید..."
            })
        }
        
