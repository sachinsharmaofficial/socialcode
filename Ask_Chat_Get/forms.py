from django.contrib.auth.models import User
from Ask_Chat_Get.models import Ask
from django import forms

class ASK_Form(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Write Your Question'}), required=True)
    
    class Meta:
        model = Ask
        fields = ['body', ]