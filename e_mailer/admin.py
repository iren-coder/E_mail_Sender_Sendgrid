from django.contrib import admin

# Register your models here.

from e_mailer.models import Mail

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    pass