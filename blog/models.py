from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
	title = models.CharField(max_length=50)
	post_description = models.TextField(blank=True, null=True)
	date_posted = models.DateTimeField()
	author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,related_name="author_blogs")
	tagged_user = models.ManyToManyField(User)

	def __str__(self):
		return self.title

