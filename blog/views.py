from email.policy import HTTP
from multiprocessing import context
from re import template
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

from django.template.loader import get_template

rooms = [
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Design Web Page'},
]

def home(request):
    # return HttpResponse('Home')
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request):
    something_here = "Room"
    return HttpResponse(something_here)

def about_page(request):
    return HttpResponse('<h1>About Page</h1>')

def contact_page(request):
    return HttpResponse('<h1>Contact Page</h1>')

# Example: Render any type of data
def example_page(request):
    context = {'title': 'A text file to test rendering an type of data'}
    template_name = "text_file.txt"
    template_obj = get_template(template_name)
    rendered_string = template_obj.render(context)
    return HttpResponse(rendered_string)


# Create your views here.
# def blog_post_detail_page(request):
#     obj = BlogPost.objects.get(id=1) # query -> database -> data -> django renders it
#     context = {"object": obj}
#     return render(request, "blog_post_detail.html", context)


# dynamic urls based
# def blog_post_detail_page(request, post_id):
#     # handle erros
#     try:
#         obj = BlogPost.objects.get(id=post_id) # query -> database -> data -> django renders it
#     except BlogPost.DoesNotExist:
#         raise Http404
#     except ValueError:
#         raise Http404
#     context = {"object": obj}
#     return render(request, "blog_post_detail.html", context)


# get_object_or_404
# def blog_post_detail_page(request, post_id):
#     # obj = BlogPost.objects.get(id=post_id) # query -> database -> data -> django renders it
#     obj = get_object_or_404(BlogPost, id=post_id) # query -> database -> data -> django renders it
#     context = {"object": obj}
#     return render(request, "blog_post_detail.html", context)


# After using slug
# def blog_post_detail_page(request, slug):
    # we do need id here as we are using slug
    # query_set = BlogPost.objects.filter(slug=slug) 
    # if query_set.count() == 0:
    #     raise Http404
    # obj = query_set.first()
    # obj = get_object_or_404(BlogPost, slug=slug)
    # context = {"object": obj}
    # return render(request, "blog_post_detail.html", context)


def blog_post_list_view(request):
    # list out objects
    # could be search

    # queryset = BlogPost.objects.filter(title__icontains="Hello")
    queryset = BlogPost.objects.all()
    template_name = 'blog_post_list.html'
    context = {"object_list": queryset}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_create_view(request):
    # create objects
    # ? use a form
    template_name = 'blog_post_create.html'
    context = {"form": None}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {"object": None, 'form': None}
    return render(request, template_name, context)

def blog_post_delete_view(request):
    template_name = 'blog_post_delete.html'
    context = {"object": None}
    return render(request, template_name, context)