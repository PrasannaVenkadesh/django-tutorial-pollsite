from django.shortcuts import render, get_object_or_404
from polls.models import Poll

# Create your views here.
def index(request):
	latest_poll = Poll.objects.order_by('-pub_date')[:5]
	context = {'latest_poll': latest_poll }
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
		poll = get_object_or_404(Poll, pk=poll_id)
		return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
 	pass

def vote(request, poll_id):
	pass
