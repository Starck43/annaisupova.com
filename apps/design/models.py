from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.utils.text import slugify
from django.utils.html import format_html
from django.core.files.storage import FileSystemStorage
from sorl.thumbnail import ImageField, get_thumbnail
import os

from uuslug import uuslug
import datetime
#from portfolio import models
# from .logic import MediaFileStorage
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
	return datetime.date.today().year

def max_value_current_year(value):
	return MaxValueValidator(current_year())(value)

def UploadFilename(instance, filename):
	basename, ext = os.path.splitext(filename)
	return os.path.join('portfolio/', basename + ext.lower())

class MediaFileStorage(FileSystemStorage):
	def save(self, name, content, max_length=None):
		# prevent saving file on disk
		return name

class Category(models.Model):
	name = models.CharField('Раздел', max_length=50)
	slug = models.SlugField('Ярлык', max_length=50, unique=True)
	# Metadata
	class Meta:
		ordering = ['name'] # '-' for DESC ordering
		verbose_name = 'Раздел'
		verbose_name_plural = 'Разделы'

	def get_absolute_url(self):
		pass
		# return reverse('portfolio-cat-url', args=[self.slug.lower()])
		# return self.slug.lower()

	def __str__(self):
		return self.name


class Project(models.Model):
	category = models.ManyToManyField(Category, blank=True)
	slug = models.SlugField('Ярлык', max_length=150, unique=True)
	title = models.CharField('Название проекта', max_length=150)
	excerpt = models.TextField('Описание статьи', db_index=True, null=True, blank=True)
	year = models.IntegerField('Год реализации', validators=[MinValueValidator(2008), max_value_current_year], blank=True)
	cover = models.ImageField('Обложка', upload_to='portfolio/', storage=MediaFileStorage())
	# Metadata
	class Meta:
		ordering = ['title'] # '-' for DESC ordering
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'

	STATUS_LIST = (
		('0', 'Реализован'),
		('1', 'В стадии реализации'),
	)

	status = models.CharField(
		'Статус',
		max_length=1,
		choices=STATUS_LIST,
		blank=False,
		default='0',
		help_text='',
	)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = uuslug(self.title, instance=self)
		if self.slug.lower() == 'new':
			self.slug = f'{self.slug}-1'
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title
		#return f'{self.title} ({self.category.name})'

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this project."""
		#return reverse('project-detail-url', args=[self.category, self.slug])
		return self.slug.lower()

	def thumb_img(self):
		if self.cover:
			return format_html('<img src="/media/{0}"/>', get_thumbnail(self.cover, '50x50', quality=80))
		else:
			return format_html('<img src="/media/no-image.png" width="50"/>')

	thumb_img.short_description = 'Миниатюра'


	@property
	def imageURL(self):
		try:
			url = self.cover.url
		except:
			url = ''
		print('URL:', url)
		return url

	@property
	def filename(self):
		return self.cover.name.rsplit('/', 1)[-1]


class Image(models.Model):
	project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='images', null=True, blank=True)
	title = models.CharField('Название', max_length=150, null=True, blank=True)
	description = models.CharField('Описание', max_length=255, null=True, blank=True)
	file = models.ImageField('Фото', upload_to='portfolio/', default="/no-image.png", storage=MediaFileStorage(), unique=False)
	name = models.CharField('Имя файла', max_length=50, null=True)
	# Metadata
	class Meta:
		verbose_name = 'Изображение'
		verbose_name_plural = 'Изображения'


	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.name:
			self.name = self.file.name.rsplit('/', 1)[-1]

		if not self.title:
			# take only file name
			self.title = os.path.splitext(self.file.name)[0]
		super().save(*args, **kwargs)

	def file_thumb(self):
		if self.file:
			return format_html('<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>', self.file.url)
		else:
			return format_html('<img src="/media/no-image.png" width="100"/>')

	file_thumb.short_description = 'Миниатюра'

	@property
	def filename(self):
		return self.file.name.rsplit('/', 1)[-1]

