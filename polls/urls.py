from django.urls import path
from . import views

app_name = "polls"  ## to get clear path of the app
urlpatterns = [
	path('<int:question_id>/vote/', views.vote ,name="ques_votes"),
	path('<int:question_id>/results/', views.results ,name="quesiton_results"),
	path('<int:question_id>/', views.details,name="question_details"),
	path('', views.index, name= "index"),
	]