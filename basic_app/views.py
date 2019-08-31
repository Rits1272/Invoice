from django.shortcuts import render
from basic_app.models import Invoice_Data
from basic_app.forms import PostForm
from django.shortcuts import redirect
from easy_pdf.views import PDFTemplateView
from basic_app.utils import render_to_pdf
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

# Create your views here.

def data_list(request):
    data = Invoice_Data.objects.all()
    return render(request, 'basic_app/html_invoice.html', {'data':data})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('base')
    else:
        form = PostForm()
    return render(request, 'basic_app/add_invoice.html', {'form':form})

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('basic_app/base.html')
        data = {'data':Invoice_Data.objects.all()}
        html = template.render(data)
        pdf = render_to_pdf('basic_app/base.html', data)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice.pdf"
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment;filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
