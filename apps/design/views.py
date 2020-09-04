from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import EmailMessage
from django.template.loader	import render_to_string


def index(request):

	return render(request, 'index.html')

def send_email(request):

	if request.method == 'POST':

		template = render_to_string('success.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
		})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['saloon.as@gmail.com']
		)

		email.fail_silently=False
		email.send()

		return HttpResponse('Сообщение отправлено!')
