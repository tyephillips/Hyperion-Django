from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    """
    Render the homepage for the polls app.
    """
    return render(request, 'polls/home.html')


def index(request):
    """
    Display the latest 5 questions in the poll app.

    Retrieves the latest 5 questions ordered by their publication 
    date and passes them to the " polls/poll.html" template.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)


def detail(request, question_id):
    """
    Display the details of a specific question.

    Retrieves a question by its primary key (question_id) and
    renders it using "polls/poll.html" template. If the question is
    not found displays a 404 error.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required
def vote(request, question_id):
    """
    Handle voting for a specific question.

    Retrieves the selected choice for a question based on the posted
    data. If no choice is selected, re-renders the "polls/detail.html"
    template with an error message. If a valid choice is selected, 
    increments its vote count, saves the result, and redirects to the 
    results page for the question.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
            )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Redirects to the results page for the question.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
            )


def results(request, question_id):
    """
    Display results of a specific question.

    Retrieves a question using its primary key (question_id) and
    renders it using the "polls/results.html" template.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

