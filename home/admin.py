from django.contrib import admin
from .models import Post, Homepage, Aboutpage, Newsletter
from .models import Contact
# Register your models here.

admin.site.register(Post)
admin.site.register(Homepage)
admin.site.register(Aboutpage)
admin.site.register(Newsletter)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','content']
admin.site.register(Contact, ContactAdmin)