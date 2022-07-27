from django.contrib import admin
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.home),
    re_path(r'^room/$', views.room),
    # path('room/', room),
    path('example/', views.example_page),
    path('about/', views.about_page),
    path('contact/', views.contact_page),

    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
