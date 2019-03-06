from django.forms import ModelForm, TextInput, formset_factory
from AssignmentsApp.models import Assignments
from django.contrib.auth.models import User

class AssignmentsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AssignmentsForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields['user_id'].queryset = User.objects.filter(groups__name__in=['Students'])
    """
    Test Form
    """
    class Meta:
        model = Assignments
        fields = '__all__'

