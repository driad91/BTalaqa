from django.forms import ModelForm,Textarea, TextInput, formset_factory
from TeachersApp.models import Question,Answer,Test,TestQuestions

class TestForm(ModelForm):

    """
    Test Form
    """
    class Meta:
        model = Test
        fields = ['name']
        widgets = {
            'name':TextInput ,
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
        fields = ['text','is_correct']
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

