from django.forms import Form, ModelForm, BooleanField, Textarea, TextInput
from MCQAssignmentsApp.models import Question, Answer, Test
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
        widgets = {
            'text': TextInput,
        }

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        self.fields['text'].widget.attrs['width'] = 300


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
        widgets = {
            'text': TextInput,
        }


class DeleteQuestion(Form):
    yes_no = BooleanField(label='Are you sure?')

