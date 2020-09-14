from django import forms
from .models import Category, Project, Image, current_year


class ContactForm(forms.Form):
	name = forms.CharField(label='Имя', required=True, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
	email = forms.EmailField(label='E-mail', required=False, widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
	message = forms.CharField(label='Сообщение', required=True, widget=forms.Textarea(attrs={'placeholder': 'Сообщение'}))

def year_choices():
	return [(r,r) for r in range(1984, datetime.date.today().year+1)]

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project

		fields = '__all__'
		#exclude = ['image']

		widgets = {
			'slug': forms.TextInput(attrs={'class': 'form-control'}), #forms.HiddenInput(),
			'category': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'excerpt': forms.Textarea(attrs={'class': 'form-control','rows': 10}),
			'cover': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'status': forms.Select(attrs={'class': 'form-control'}),
			'year': forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year),
		}

	#files = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)
	files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
