from django.http import HttpResponse
from django.shortcuts import render
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
