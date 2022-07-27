from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

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


# list out objects
# could be search
def blog_post_list_view(request):
    # queryset = BlogPost.objects.filter(title__icontains="Want")
    queryset = BlogPost.objects.all()
    template_name = 'blog_post_list.html'
    context = {"object_list": queryset}
    return render(request, template_name, context)

# 1 object -> detail view
def blog_post_detail_view(request, slug):
    print(request, slug)
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

# create objects
# ? use a form
def blog_post_create_view(request):
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