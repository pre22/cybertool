from django import forms

class ToolsForm(forms.Form):
    sender_input = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your mail account here:'}))
    receiver_input = forms.CharField(max_length=200, required=True)
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the subject here:'}))
    body = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter your body text here'}))
    password_user = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password here'}))