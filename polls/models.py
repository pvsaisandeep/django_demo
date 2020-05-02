from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import BlogPost

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('published date',default=timezone.now)
	description = models.TextField(blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_polls")
	blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, blank=True, null=True, related_name="blog_questions")

	class Meta:
		get_latest_by = 'pub_date'
		ordering = ['-pub_date']

	def __str__(self):
		return str(self.id)

class Choices(models.Model):
	choice_text = models.CharField(max_length=100)
	votes_number = models.IntegerField(default=0)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_choices')

	def __str__(self):
		return self.choice_text