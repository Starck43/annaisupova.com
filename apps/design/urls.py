from django.urls import path
from .views import send_email

app_name = 'design'

urlpatterns = [
	#path('', views.IndexView.as_view(), name='index'),
	path('message/', send_email, name="send-email"),
]