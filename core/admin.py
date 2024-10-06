from django.contrib import admin
from core.models import ContactUs, Newsletter

class ContactAdminSide(admin.ModelAdmin):
    list_display = ('fname','lname', 'email', 'subject', 'message')

admin.site.register(ContactUs,ContactAdminSide)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['sub_email',]

admin.site.register(Newsletter, NewsletterAdmin)