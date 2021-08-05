from django.contrib import admin
from .models import Place,Restaurant,Waiter,Reporter,Article,Publication,many

# Register your models here.
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(many)