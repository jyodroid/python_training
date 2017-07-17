from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')

    # Dictionary with envirnment variables on template
    context = {
        'latest_question_list': latest_question_list
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # Using a template
    # return HttpResponse(template.render(context, request))

    # Using shortcut render()
    return render(request, 'polls/index.html', context)

def detail(request, question_id):

    # Use shortcut get_object_or_404()
    question = get_object_or_404(Question, pk = question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    # response = "You're looking at the results of the question %s."
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': questin, 'error_message': "you didn't selesct a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponse("you're voting on question %s" % question_id)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # Reverse function helps avoid having to hardcode URL in the view function
