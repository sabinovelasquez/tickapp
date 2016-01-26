from django.http import HttpResponse


def detail(request, question_id):
  return HttpResponse("You're looking at Premise %s." % premise_id)
  
def results(request, question_id):
  response = "You're looking at the results of Premise %s."
  return HttpResponse(response % premise_id)