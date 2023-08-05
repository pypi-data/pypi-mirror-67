import numpy as np
import os
import shutil
import json

from .call_html import call_html
from .get_beam_dependency import get_beam_dependency


def visualize_beam_search_decode(source_sentences, target_sentences, predicts,
                                 parents, log_probs, beam_width):
    '''
    source_sentences: A python list consisting translated sentences
    target_sentences: A python list consisting translation results
    predicts: An numpy array of shape [num_sentences,num_steps,beam_width]. Words predicted by the beam search decoder at every step
    parents: An numpy array of shape [num_sentences,num_steps,beam_width]. Indexes of beams which the predictions at next step come from
    log_probs: An numpy array of shape [num_sentences,num_steps,beam_width]. Log probabilities of giving every predicted words
    beam_width: A python int. The size of the beams
    '''
    if os.path.exists('beamvistemp') == True:
        shutil.rmtree('beamvistemp')
    if os.path.exists('beamvistemp') == False:
        get_beam_dependency()
    get_json(source_sentences, target_sentences, predicts, parents, log_probs,
             beam_width)
    os.chdir('beamvistemp')
    call_html()


def make_children_lookup(parent):
    res = np.zeros_like(np.array(parent))
    for i in range(len(parent) - 1):
        for j in parent[i + 1]:
            res[i][j] = 1
    return res.tolist()


def make_accum_probs(probs, parent):
    probs = np.array(probs)
    parent = np.array(parent)
    for i in range(1, probs.shape[0]):
        for j in range(0, probs.shape[1]):
            probs[i][j] += probs[i - 1][parent[i][j]]
    return probs.tolist()


def get_json(source_sentences, target_sentences, predicts, parents, log_probs,
             beam_width):
    predicts = np.array(predicts)
    parents = np.array(parents)
    log_probs = np.array(log_probs)

    total = len(source_sentences)
    res = []
    for i in range(total):
        tmp = {}
        tmp["id"] = i
        tmp["beam_width"] = beam_width
        tmp["source"] = source_sentences[i]
        tmp["target"] = target_sentences[i]
        tmp["parent"] = parents[i, :, :].tolist()
        tmp["has_children_lookup"] = make_children_lookup(tmp["parent"])
        tmp['predict'] = predicts[i, :, :].tolist()
        tmp["probs"] = log_probs[i, :, :].tolist()
        tmp['accum_probs'] = make_accum_probs(tmp["probs"], tmp["parent"])
        res.append(tmp)
    with open("beamvistemp/history.json", 'w') as out:
        json.dump(res, out)
