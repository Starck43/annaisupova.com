from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.utils.text import slugify
from django.utils.html import format_html
import os

from uuslug import uuslug
#from datetime import date
#from time import time
from portfolio import models