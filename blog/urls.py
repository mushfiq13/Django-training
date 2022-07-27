from django.urls import path, re_path
from . import views
from .views import (
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_create_view,
)

urlpatterns = [
    path('', blog_post_list_view),
    
    # path('detail/', blog_post_detail_page),
    # dynamic urls based
    # path('detail/<int:post_id>/', blog_post_detail_page),
    # re_path(r'^detail/(?P<post_id>\d+)/$', blog_post_detail_page),
    
    # If we slug then we should follow this format:
    path('<str:slug>/', blog_post_detail_view),
    # re_path(r'^(?P<slug>\w+)/$', blog_post_detail_page),
     path('create/', views.blog_post_create_view),
]