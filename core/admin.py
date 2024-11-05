from .models import EmailAccount, EmailMessage
from django.contrib import admin


@admin.register(EmailAccount)
class EmailAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'provider', 'created_at', 'updated_at')
    search_fields = ('email',)


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sent_date', 'received_date', 'is_read', 'account')
    search_fields = ('subject', 'message_text')
    list_filter = ('is_read', 'account')
