"""определяет схемы url for blogs"""

from django.urls import path, include

from . import views

app_name = 'blogs'

urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # page to add new blog
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page for edit blogs
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    # page for list of blogs
    path('blogs/', views.blogs, name='blogs'),
]
