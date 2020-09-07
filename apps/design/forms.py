from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label='Имя', required=True, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
	email = forms.EmailField(label='E-mail', required=False, widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
	message = forms.CharField(label='Сообщение', required=True, widget=forms.Textarea(attrs={'placeholder': 'Сообщение'}))
