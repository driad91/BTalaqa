from django.shortcuts import render
import spacy
from spacy import displacy
# Create your views here.
from django.contrib.auth.decorators import login_required


def dep_parse_spacy(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)
@login_required
def render_active_passive(request):
    dep_parse_spacy('I went to school today!')
    return render(request, 'active-passive-explanation.html', context={})