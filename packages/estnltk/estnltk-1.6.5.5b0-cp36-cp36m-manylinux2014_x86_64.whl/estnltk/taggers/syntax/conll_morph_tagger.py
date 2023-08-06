from estnltk.taggers import Tagger
from estnltk.layer.layer import Layer
from estnltk.converters.CG3_exporter import export_CG3
from estnltk.taggers.syntax.vislcg3_syntax import VISLCG3Pipeline, convert_cg3_to_conll
from estnltk.core import abs_path
import os
import re


class ConllMorphTagger(Tagger):
    """From morph_extended towards conll_syntax"""

    conf_param = []

    def __init__(self, output_layer: str = 'conll_morph', morph_extended_layer: str = 'morph_extended'):
        self.input_layers = [morph_extended_layer]
        self.output_layer = output_layer
        self.output_attributes = ['id', 'form', 'lemma', 'upostag', 'xpostag', 'feats', 'head', 'deprel', 'deps', 'misc']

    def _make_layer(self, text, layers, status):
        morph_extended_layer = layers[self.input_layers[0]]

        layer = Layer(name=self.output_layer, text_object=text, attributes=self.output_attributes,
                      parent=morph_extended_layer.name, ambiguous=True)

        for i, span in enumerate(morph_extended_layer):
            for annotation in span.annotations:
                values = get_values(i, text)
                xpostag = create_xpostag(values[3], values[5])
                feats = fix_feats(xpostag, values[2], values[5])
                layer.add_annotation(span,
                                     id=values[0],
                                     form=values[1],
                                     lemma=values[2],
                                     upostag=values[3],
                                     xpostag=xpostag,
                                     feats=feats,
                                     head='_',
                                     deprel='_',
                                     deps='_',
                                     misc='_'
                )
                if values[3] == annotation.partofspeech:
                    break
        return layer


def get_values(id, text):
    text.analyse('syntax_preprocessing')
    res1 = export_CG3(text)
    vislcgRulesDir = abs_path('taggers/syntax/files')
    pipeline2 = VISLCG3Pipeline(rules_dir=vislcgRulesDir)
    results2 = pipeline2.process_lines(res1)
    for j, word in enumerate(list(filter(None, convert_cg3_to_conll(results2.split('\n'))))):
        if word != '':
            if id+1 == j+1:
                values = word.split('\t')
                return (values)


def create_xpostag(upostag, feats):
    xpostag = upostag
    if upostag == 'S' and 'prop' in feats:
        return 'H'
    if upostag == 'J':
        if 'crd' in feats:
            return 'Jc'
        if 'sub' in feats:
            return 'Js'
    if upostag == 'K':
        if 'pre' in feats:
            return 'Ke'
        if 'post' in feats:
            return 'Kt'
    if upostag == 'G':
        return 'A'
    if upostag == 'N':
        if 'card' in feats:
            return 'N'
        if 'ord' in feats:
            return 'A'
    if upostag == 'P':
        if 'pers' in feats:
            return 'Ppers'
    if upostag == 'V':
        if 'aux' in feats:
            return 'Vaux'
        if 'inf' in feats:
            return 'Vinf'
        if 'sup' in feats:
            return 'Vsup'
        if 'mod' in feats:
            return 'Vmod'
    return xpostag


def fix_feats(xpostag, lemma, feats):
    if xpostag == 'D':
        feats = '_'
    if xpostag == 'A':
        feats = re.sub('pos', '', feats)
    if lemma == '"':
        feats = 'Quo'

    feats = re.sub('partic\|past', 'ppast', feats)
    feats = re.sub('\|ps$', '', re.sub('[^fm]ps[^\d]', '|', feats))
    feats = re.sub('inter_rel', 'intrel', feats)
    feats = re.sub('^pre$', '', feats)

    unnecessary_info = ['main', 'af', 'aux', 'mod', 'cap', 'com', 'sub', 'crd', 'pers', 'post', 'prop', 'CLBC', 'CLB',
                        'CLC', 'CLO']
    for elem in unnecessary_info:
        feats = re.sub(elem, '', feats)

    feats = re.sub('^\|', '', re.sub('\|+$', '', feats))
    if feats == '':
        return '_'

    else:
        return feats
