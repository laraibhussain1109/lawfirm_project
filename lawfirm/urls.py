from django.urls import path
from . import views

urlpatterns = [
    path('', views.query_list, name='query_list'),
    path('query/<int:query_id>/', views.query_detail, name='query_detail'),
    path('query/<int:query_id>/upload-document/', views.upload_document, name='upload_document'),
    path('query/<int:query_id>/upload-invoice/', views.upload_invoice, name='upload_invoice'),
]
