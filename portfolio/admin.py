from django.contrib.admin import *
from sorl.thumbnail.admin import AdminImageMixin

class ModelAdmin(AdminImageMixin, ModelAdmin):
	pass

class TabularInline(AdminImageMixin, TabularInline):
	pass

class StackedInline(AdminImageMixin, StackedInline):
	pass