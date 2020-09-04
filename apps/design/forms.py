from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label='Имя')
	email = forms.EmailField(label='E-mail', required=False)
	message = forms.CharField(label='Сообщение', widget=forms.Textarea)
