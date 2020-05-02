from rest_framework import serializers
from .models import Question, Choices
from django.contrib.auth.models import User

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ['question_text', 'pub_date', 'description', 'author', 'blog_post']
