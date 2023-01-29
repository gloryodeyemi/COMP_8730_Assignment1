import nltk
import re
import pytrec_eval as pt
from operator import itemgetter
from nltk.corpus import wordnet as wn
from utils.min_edit_distance import med_function

# function to return top-k most similar, least distant list of tokens
def top_k_words(data_row):
    words_in_wn = wn.words(lang='eng')
    cor_word = data_row[0].lower()
    incor_word = data_row[1].lower()
    wn_result = {'correct_word':cor_word, 'incorrect_word':incor_word}
    words_dict = {}
    for word in words_in_wn:
        if re.match("^[a-zA-Z]+$", word):
            edit_distance = med_function(incor_word, word, False)
            words_dict[word] = edit_distance
        
    words_dict = dict(sorted(words_dict.items(), key=lambda item: item[1]))
    for k in [1,5,10]:
        words_dict_res = dict(list(words_dict.items())[:k])
        k_words = []
        for k_word, k_distance in words_dict_res.items():
            k_words.append(k_word)
        wn_result['top_' + str(k)] = k_words
    
    return wn_result


# function to check for the success at k
def check_insert(k_list, correct_word):
    if correct_word in k_list:
        return 1
    else:
        return 0


# function to return the success at k for every incorrectly spelled token
def success_at_k(top_k_result):
    suc_at_k_dict = {}
    result_dict = {}
    for item in top_k_result:
        correct_word, incorrect_word, top_1, top_5, top_10 = itemgetter('correct_word', 'incorrect_word',
                                                                        'top_1', 'top_5', 'top_10')(item)
        result_dict['success_at_1'] = check_insert(top_1, correct_word)
        result_dict['success_at_5'] = check_insert(top_5, correct_word)
        result_dict['success_at_10'] = check_insert(top_10, correct_word)

        suc_at_k_dict[incorrect_word] = result_dict
        result_dict = {}

    return suc_at_k_dict


# function calculate average success at k for k={1, 5, 10} using PyTrec_Eval_Terrier
def average_k(success_dict):
    average_dict = {}
    for k_success in success_dict[list(success_dict.keys())[0]].keys():
        average_dict[k_success] = pt.compute_aggregated_measure(
                                  k_success, [val[k_success] for val in success_dict.values()])
    return average_dict

