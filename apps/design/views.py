from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMessage,BadHeaderError
from django.template.loader	import render_to_string
from .forms import ContactForm

def contact_thanks(request):
	return render(request, 'thanks_for_message.html')

def under_reconstruction(request):
	return render(request, 'reconstruction.html')

def contacts(request):
	return render(request, 'contacts.html')

def index(request):
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			return send_email(request)
	else:
		form = ContactForm()

	return render(request, 'index.html', {'form': form})


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


