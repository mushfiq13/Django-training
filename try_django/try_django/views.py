
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    # return HttpResponse('home')
    # return render(request, 'home.html')
    context = {'obj_list':[
        {'id': 1, 'name': 'object 1'},
        { 'id': 2, 'name': 'object 2'}
    ]}
    return render(request, 'home.html', context)

# Using this structure of code, we can render any different type of file
def about_page(request):
    context = { 'title': 'About Us - Here we are rendering a text file to experiment.' }
    template_name = 'text_file.txt'
    template_obj = get_template(template_name)
    rendered_string = template_obj.render(context)
    return HttpResponse(rendered_string)

def contact_page(request):
    context = '<h1>Contact Us</h1>'
    return HttpResponse(context)
