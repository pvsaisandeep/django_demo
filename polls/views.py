from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choices
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .serializers import QuestionSerializer 

@api_view(['GET'])
def index(request):
	if request.method == 'GET':
		all_questions = Question.objects.all().order_by('pub_date')
		serializer_result = QuestionSerializer(all_questions, many=True)
		return Response(serializer_result.data)
		#context = {'latest_question_list': all_questions}
	# return render(request, 'polls/index.html', context)


def details(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	context = {'question': question}
	return render(request, 'polls/details.html', context)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		choice = question.question_choices.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
	else:
		choice.votes_number += 1
		choice.save()
		return HttpResponseRedirect(reverse('polls:quesiton_results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# def createquestion(request):




