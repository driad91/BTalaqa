from django.shortcuts import render
from django.http import JsonResponse
import spacy
from spacy import displacy
# Create your views here.
import json
from django.contrib.auth.decorators import login_required


def dep_parse_spacy(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    parsed_dict = {}
    for token in doc:
        parsed_dict[token.text] = token.dep_
    return parsed_dict
        #token.lemma_, token.pos_, token.tag_, token.dep_,
        #token.shape_, token.is_alpha, token.is_stop


@login_required
def render_active_passive(request):
    return render(request, 'active-passive-explanation.html', context={})

@login_required
def parse_sentence(request):
    """
    Ajax request to parse sentence using spacy and return POS tags
    """
    sentence = request.GET.get('sentence')
    print(sentence)
    parsed_dict = dep_parse_spacy(text=sentence)
    counter = 0
    nodes = []
    edges = []

    for key in parsed_dict:
        node = {}
        edge = {}
        node['id'] = counter
        node['label'] = key + '|' + parsed_dict[key]
        nodes.append(node)
        if counter != 0:
            edge['from'] = counter-1
            edge['to'] = counter
            edges.append(edge)
        counter += 1
    return JsonResponse({'nodes': nodes,
                         'edges': edges})
