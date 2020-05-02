from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Question, Choices
from django.dispatch import receiver

@receiver(post_save, sender=Question)
def create_choices(sender, instance, created, **kwargs):
	if created:
		for i in range(1,4):
			Choices.objects.create(choice_text="Choice No : "+str(i), question=instance)


