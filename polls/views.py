from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('Hello World!, You are at the Poll Index')

def detail(request, poll_id):
	return HttpResponse('You are looking at poll %s.' % poll_id)

def results(request, poll_id):
	return HttpResponse('You are looking at poll results of poll %s.' % poll_id)

def vote(request, poll_id):
	return HttpResponse('You are voting on poll %s' % poll_id)
