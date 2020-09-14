from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView #, MultipleObjectMixin
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMessage,BadHeaderError
from django.template.loader	import render_to_string
from .forms import ContactForm
from .models import Project, Category, Image

class project_list(ListView):
	model = Project
	template_name = 'design/portfolio.html'
	context_object_name = 'projects'

	section_class = 'design__selected'
	paginate_by = 10

	def get_queryset(self):
		slug = self.kwargs['category']
		search_query = self.request.GET.get('q')
		if search_query:
			posts = self.model.objects.filter(except__icontains = search_query)
		else:
			if slug == None:
				posts = self.model.objects.all()
			else:
				posts = self.model.objects.filter(category__slug=slug)

		return posts

	def get_context_data(self, **kwargs):
		slug = self.kwargs['category']
		context = super().get_context_data(**kwargs)
		context['selected_section'] = self.section_class
		context['classes'] = ['portfolio', 'is-nav']
		context['category'] = Category.objects.filter(slug=slug).first()

		return context


# def styling(request, category=''):
# 	section_class = 'styling__selected';
# 	return render(request, 'styling.html', {'selected_section': section_class})

class project_detail(DetailView):
	model = Image
	template_name = 'design/gallery.html'
	context_object_name = 'gallery'

	def get_object(self):
		return self.model.objects.filter(project=get_object_or_404(Project, slug=self.kwargs['slug']))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['classes'] = ['gallery', 'is-nav']
		context['project'] = Project.objects.filter(slug=self.kwargs['slug'])[0]

		return context


def design(request):
	return index(request,'design__selected');

def contacts(request, section=''):

	context = {
		'selected_section': section,
		'classes': ['contacts'],
	}

	if section != '':
		context['classes'].append('is-nav')

	return render(request, 'contacts.html', context)

def about_us(request, section=''):
	context = {
		'selected_section': section,
		'classes': ['about-us'],
	}
	if section != '':
		context['classes'].append('is-nav')

	return render(request, 'about-us.html', context)

def index(request,section_class=''):
	classesList = ['home','is-nav']
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			return send_email(request)
	else:
		form = ContactForm()

	context = {
		'form': form,
		'classes': classesList,
		'selected_section': section_class,
	}
	return render(request, 'index.html', context)


def message_thanks(request):
	return render(request, 'thanks_for_message.html')


def send_email(request):

	template = render_to_string('message_for_recepient.html', {
		'name':request.POST['name'],
		'email':request.POST['email'],
		'message':request.POST['message'],
	})

	email = EmailMessage(
		'Новое сообщение с сайта!',
		template,
		settings.EMAIL_HOST_USER,
		settings.EMAIL_RICIPIENTS,

	)
	email.content_subtype = "html"
	email.html_message = True
	email.fail_silently=False
	try:
		email.send()
	except BadHeaderError: #Защита от уязвимости
		return HttpResponse('Неверный заголовок письма')

	#return HttpResponse("Сообщение было успешно отправлено!. Я обязательно с Вами скоро свяжусь")
	return HttpResponseRedirect('/thanks/')


