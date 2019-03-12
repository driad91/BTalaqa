from django.forms import ModelForm, Textarea, TextInput, formset_factory, Form
from MCQAssignmentsApp.models import Question, Answer, Test, StudentTestAnswers


class TestForm(ModelForm):
    """
    Test Form
    """

    class Meta:
        model = Test
        fields = ['name']
        widgets = {
            'name': TextInput,
        }
        max_length = Test._meta.get_field('name').max_length
        labels = {
            'name': 'Test Name',
        }
        help_texts = {
            'name': 'Please enter the test name here'
        }


class AnswerForm(ModelForm):
    """
    Answer Form
    """
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']
        labels = {
            'text': 'Answer text',
            'is_correct': 'Correct Answer?'
        }


class QuestionForm(ModelForm):
    """
    Answer Form
    """
    class Meta:
        model = Question
        fields = ['text', 'exclusive_answer']
        labels = {
            'text': 'Question text',
        }


answer_form_set = formset_factory(form=AnswerForm,
                                  extra=4,
                                  can_delete=True)


class StudentAnswerForm(Form):

    """
    Student Answer Form, basically form  created to render the assigned tests
    to students as they are created by the teachers as a form and save them in
    the StudentTestAnswers Model
    """

    def __init__(self, *args, **kwargs):
        super(StudentAnswerForm, self).__init__(*args, **kwargs)
        self.test_id = kwargs.pop('test_id')
    relevant_questions = Question.objects.filter(test=Form.test_id).values()
    if relevant_questions:
        relevant_answers = Answer.object.filters(question__in=list(relevant_questions.values('id')))
        





