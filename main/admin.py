from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.AboutMe)
admin.site.register(models.Contact)
admin.site.register(models.Portfolio)
admin.site.register(models.Skills)
admin.site.register(models.Technologies)
admin.site.register(models.Services)
admin.site.register(models.Articles)
admin.site.register(models.Tags)
admin.site.register(models.Testimonials)
admin.site.register(models.Seo)
