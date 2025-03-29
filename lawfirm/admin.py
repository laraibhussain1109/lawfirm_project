from django.contrib import admin
from .models import Query, Document, Invoice

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'query', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('title',)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'query', 'amount', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('invoice_number',)
