from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('index/',views.blogindex,name="blog_index"),
	]