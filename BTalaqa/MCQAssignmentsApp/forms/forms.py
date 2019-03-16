from django.forms import Form, ModelForm, BooleanField, TextInput, formset_factory
from MCQAssignmentsApp.models import Question, Answer, Test


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
                                  extra=1,
                                  can_delete=False)


class DeleteQuestion(Form):
    yes_no = BooleanField(label='Are you sure?')

