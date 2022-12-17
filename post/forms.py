from django import forms
from post.models import Post


class NewPostform(forms.ModelForm):
    # content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True) 
    #picture is required initially by sachin
    # widget=forms.FileInput(attrs={'id':'insert-image','style':'display: none;','accept':'image/jpeg,image/gif,image/png'})
    picture = forms.ImageField()
    caption = forms.CharField(widget=forms.Textarea(attrs={'id': 'post-text', 'placeholder': 'Caption'}), required=True)
    tags = forms.CharField(widget=forms.TextInput(attrs={'id': 'post-tags', 'placeholder': 'Tags | Seperate with comma'}), required=True)

    class Meta:
        model = Post
        fields = ['picture', 'caption', 'tags']
