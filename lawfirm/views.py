from django.shortcuts import render, get_object_or_404, redirect
from .models import Query
from .forms import DocumentForm, InvoiceForm

def query_list(request):
    queries = Query.objects.all().order_by('-created_at')
    return render(request, 'lawfirm/query_list.html', {'queries': queries})

def query_detail(request, query_id):
    query = get_object_or_404(Query, id=query_id)
    return render(request, 'lawfirm/query_detail.html', {'query': query})

def upload_document(request, query_id):
    query = get_object_or_404(Query, id=query_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.query = query
            document.save()
            return redirect('query_detail', query_id=query.id)
    else:
        form = DocumentForm()
    return render(request, 'lawfirm/upload_document.html', {'form': form, 'query': query})

def upload_invoice(request, query_id):
    query = get_object_or_404(Query, id=query_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.query = query
            invoice.save()
            return redirect('query_detail', query_id=query.id)
    else:
        form = InvoiceForm()
    return render(request, 'lawfirm/upload_invoice.html', {'form': form, 'query': query})
