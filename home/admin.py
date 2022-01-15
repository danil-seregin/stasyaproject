from django.contrib import admin

# Register your models here.
from .models import logo
from .models import otzyv
from .models import uslugi
from .models import news
from .models import questions

admin.site.register(logo)
admin.site.register(otzyv)
admin.site.register(uslugi)
admin.site.register(news)
admin.site.register(questions)
