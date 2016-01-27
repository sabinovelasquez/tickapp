from django.http import HttpResponse
from django.shortcuts import render

from .models import Premise

def detail(request, premise_id):
  return HttpResponse("You're looking at Premise %s." % premise_id)


def index(request):
    latest_premise_list = Premise.objects.order_by('-pub_date')[:5]
    context = {'latest_premise_list': latest_premise_list}
    return render(request, 'premises/index.jade', context)