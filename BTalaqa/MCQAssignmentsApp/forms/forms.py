from django.forms import ModelForm,Textarea, TextInput, inlineformset_factory
from MCQAssignmentsApp.models import Question,Answer,ModelAnswers,Test,TestQuestions

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



question_form_set = inlineformset_factory(Question, Answer, ModelAnswers, fields='__all__')