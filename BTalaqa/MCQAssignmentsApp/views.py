from django.shortcuts import render, redirect
from MCQAssignmentsApp.forms.forms import TestForm, answer_form_set,\
    QuestionForm, AnswerForm
from MCQAssignmentsApp.models import Test, Question, Answer, StudentTestAnswers
from AssignmentsApp.models import Assignments
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import JsonResponse

from MCQAssignmentsApp.helpers import test_helper
import json

@login_required
@permission_required('MCQAssignmentsApp.edit_test')
def create_test(request):
    """
    a view to create tests.

    :param request:
    :return:
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            test_object = form.save()
            messages.info(request, "Test created")

            return redirect('MCQAssignmentsApp:create_question_answers', pk=test_object.id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    return render(request, 'teachers/test-creation.html', {'form': form})


@login_required
@permission_required('MCQAssignmentsApp.edit_question')
def create_questions_answers(request, pk):
    """
    The view for teachers to create their questions and answers to them.

    :param request:
    :param pk: primary key of the test
    :return:
    """

    test = None
    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        answer_forms = answer_form_set(request.POST)

        if question_form.is_valid():
            valid = True
            question = question_form.save()

            for answer_form in answer_forms:
                if answer_form.is_valid():
                    name = answer_form.cleaned_data.get('name')
                    if name:
                        print(name)
                    answer_form = answer_form.save(commit=False)
                    answer_form.question = question
                    answer_form.save()
                    test_current = Test.objects.get(pk=pk)
                    question.test.add(test_current)
                else:
                    valid = False
            if valid:
                messages.info(request, "Question {} created".format(question.id))
                # go to the next answer
                return redirect('MCQAssignmentsApp:create_question_answers',
                                pk=pk)
            else:
                messages.warning(request, "One of the forms is not valid")

    else:
        try:
            test = Test.objects.get(pk=pk)
        except ObjectDoesNotExist:
            messages.info(request, "There is no test with this id")

    return render(request, 'teachers/questions-answers-creation.html',
                  {'question_form': QuestionForm,
                   'answer_formset': answer_form_set,
                   'test': test})


@login_required
@permission_required('MCQAssignmentsApp.read_test')
def students_assignments(request):
    """
    returns view of all tests assigned to the logged in student and renders the
    template
    :param request: http request
    :return: template
    """

    user_tests = Assignments.objects.filter(user_id__username=request.user)\
        .values('test_id','test_id__name')
    return render(request, 'students/students-assigned-tests.html',
                  context={'user_tests': user_tests})
@login_required
@permission_required('MCQAssignmentsApp.read_test')
def render_test(request, id):
    """
    renders any chosen test by the user in the form of a test
    :param request: http request
    :param id: id of the test to be rendered
    :return:
    """
    relevant_questions = Question.objects.filter(test=id)
    relevant_answers =Answer.objects.filter(question__in=relevant_questions.values_list('id', flat=True))
    return render(request, 'students/selected-test.html', context={'questions': relevant_questions.values(),
                                                                   'answers': relevant_answers.values(),
                                                                   'test_id': id})
@login_required
@permission_required('MCQAssignmentsApp.read_test')
def submit_test(request):
    """
    Handles different things to be done when student submits test, i.e. saving
    of the students answers, removing test as an assignment to this student
    and checks if the answers for this test were already in the database,
    and if so deletes them and updates them with the new values
    :param request: Ajax request
    :return: Msg, containing the score of the student
    """
    data = json.loads(request.POST.get('values'))
    student_answers_dict = data['student_answers']
    student = request.user
    test_id = data['test_id']
    test = Test.objects.get(pk=test_id)
    correct_answers = Answer.objects.filter(is_correct=True,
                                            question__test=test).values('id', 'question_id')
    qs_assignment = Assignments.objects.filter(test_id=test, user_id=student)
    if qs_assignment.exists():
        qs_assignment.delete()
    qs = StudentTestAnswers.objects.filter(test=test, student=student)
    if qs.exists():  # if student has previous answers for this test
        qs.delete()  # delete
    for k, v in student_answers_dict.items():
        question = Question.objects.get(pk=k)  # retrieving question item from id
        answer = Answer.objects.get(pk=v)  # retrieving answer obj from id
        test_answer = StudentTestAnswers.objects.create(student=student,
                                                        question=question,
                                                        answer=answer,
                                                        test=test)
        test_answer.save()
    percentage, corrections_dict = test_helper.test_correction\
        (student_answers=student_answers_dict, model_answers=correct_answers)
    return JsonResponse({'percentage': percentage*100,
                         'corrections_dict': corrections_dict})



