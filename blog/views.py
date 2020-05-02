from django.shortcuts import render
from blog.models import BlogPost

def blogindex(request):
	context = {'blogposts': BlogPost.objects.all()}
	return render(request, 'blog/blogindex.html', context)