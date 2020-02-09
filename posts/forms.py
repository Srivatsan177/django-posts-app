from django import forms

class CustomUserForm(forms.Form):
    Username=forms.CharField(label="username",widget=forms.TextInput(attrs={'class':'form-control'}))
    Password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',"type":"password"}))
    confirm_password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',"type":"password"}))


class CustomLoginForm(forms.Form):
    Username=forms.CharField(label="username",widget=forms.TextInput(attrs={'class':'form-control'}))
    Password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',"type":"password"}))

class AddPostForm(forms.Form):
    title = forms.CharField(label="title",widget=forms.TextInput(attrs={'class':'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

class UpdatePostForm(forms.Form):
    title = forms.CharField(label="title",widget=forms.TextInput(attrs={'class':'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
