from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest,HttpResponseNotFound
from .models import *
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage

def index(request):
    obj = Post.objects.all()
    context = {
        "object" : obj
    }
    return render(request, 'index.html',context)

def pdf_view(request):
    fs = FileSystemStorage()
    filename = '200_MCQS_for_Computer_Science_PPSC_Preparation.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="200 MCQS for Computer Science PPSC Preparation.pdf"'
            response['Content-Disposition'] = 'inline; filename="200_MCQS_for_Computer_Science_PPSC_Preparation.pdf"'
            return response
    else:
        return HttpResponseNotFound('The request pdf was not found in our server')

    # if request.method == "GET":
        # form = ManualForm(request.GET)

def product_manual(request, my_id):
    obj = manual_backend.objects.get(id=my_id)
    context = {
        "object" : obj
    }
    return render(request, 'index.html')

def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [ x.slug for x in category_queryset ]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category,slug=slug,parent=parent)
        else:
            instance = get_object_or_404(Post, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "postDetail.html", {'instance':instance,'breadcrumbs':breadcrumbs})

    return render(request,"categories.html",{'post_set':parent.post_set.all(),'sub_categories':parent.children.all()})

# from django.http import FileResponse, Http404

# class LoadPdfViewSet(views.APIView):
#     def get(self, request):
#         # some code here here
#         response = FileResponse(open(path_to_pdf, 'rb').read())
#         response.headers = {   
#             'Content-Type': 'application/pdf',
#             'Content-Disposition': 'attachment;filename="Spring_2022_ISL202_1_SOL.pdf"',
#         }
#         response.as_attachment = True
#         return response
