from django.forms import Form, ModelForm, BooleanField, Textarea, TextInput
from MCQAssignmentsApp.models import Question, Answer, Test, TestUserAssignment
from django.forms import ModelForm, Textarea, TextInput, formset_factory, Form
from MCQAssignmentsApp.models import Question, Answer, Test, StudentTestAnswers
from django.contrib.auth.models import User


class TestForm(ModelForm):
    """
    Test Form
    """

    class Meta:
        model = Test
        fields = ['name', 'tag', 'tag_color']
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

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


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
    Question Form
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

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DeleteQuestion(Form):
    yes_no = BooleanField(label='Are you sure?')

    def __init__(self, *args, **kwargs):
        super(DeleteQuestion, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AssignmentsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AssignmentsForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields['user'].queryset = User.objects.filter(groups__name__in=['Students'])
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = TestUserAssignment
        fields = ['user', 'test']
