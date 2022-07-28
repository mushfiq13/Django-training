from django.urls import path
from .views import (
    blog_post_delete_view,
    blog_post_list_view,
    blog_post_detail_view,
    blog_post_update_view
)

# slug value should the exact value that we given during create or update
urlpatterns = [
    path('', blog_post_list_view),
    path('detail/<str:slug>/', blog_post_detail_view),
    path('update/<str:slug>/', blog_post_update_view),
    path('delete/<str:slug>/', blog_post_delete_view)
]