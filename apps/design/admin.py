from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Category, Project, Image
from portfolio import models

from sorl.thumbnail.admin import AdminImageMixin
from multiupload.admin import MultiUploadAdmin


# auto generator slug from any field
class CategoryAdmin(admin.ModelAdmin):
	model = Category
	prepopulated_fields = {"slug": ('name',)} # adding name to slug field


class ImageInlineAdmin(admin.TabularInline):
	model = Image
	fields = ['title', 'description', 'file', 'file_thumb',]
	list_display = ['title', 'description', 'file_thumb',]
	readonly_fields = ['file_thumb',]

class GalleryMultiuploadMixing(object):

	def process_uploaded_file(self, uploaded, project, request):
		if project:
			image = project.images.create(file=uploaded)
		else:
			image = Image.objects.create(file=uploaded, project=None)
		return {
			'url': image.file.url,
			'thumbnail_url': image.file.url,
			'id': image.id,
			'name': image.filename
		}


class ImageAdmin(AdminImageMixin, GalleryMultiuploadMixing, MultiUploadAdmin, admin.ModelAdmin):
	model = Image
	fields = ['title', 'description', 'file_thumb', 'file', 'name']
	list_display = ['title', 'description', 'file_thumb', 'name']
	readonly_fields = ['file_thumb']

	multiupload_form = False
	multiupload_list = True
	multiupload_limitconcurrentuploads = 50


class ProjectAdmin(GalleryMultiuploadMixing, MultiUploadAdmin, admin.ModelAdmin):
	fields = ['category', 'title', 'slug', 'excerpt', 'thumb_img', 'cover', 'year', 'status',]
	list_display = ['thumb_img', 'title', 'category_list', 'slug', 'year', 'status',]
	list_filter = ['year', 'category', 'status']
	sortable_by = ['title','status']
	#list_editable = ['slug',]
	list_display_links = ['thumb_img','title',]
	readonly_fields = ['thumb_img',]
	search_fields = ['title', 'excerpt',]
	#inlines = ['TagsInline',]
	prepopulated_fields = {"slug": ("title",)} # adding name to slug field

	inlines = [ImageInlineAdmin,]
	multiupload_form = True
	multiupload_list = False

	def category_list(self, obj):
		return ', '.join(obj.category.values_list('name', flat=True))

	def delete_file(self, pk, request):
		obj = get_object_or_404(Image, pk=pk)
		return obj.delete()

	#  Переопределение форм
	def get_form(self, request, obj=None, **kwargs):
		form = super().get_form(request, obj, **kwargs)
		form.base_fields["cover"].label = ""
		return form

admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)

