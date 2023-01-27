import nltk
import re
from nltk.corpus import wordnet as wn
from min_edit_distance import med_function

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
        wn_result['top ' + str(k)] = k_words
    
    return wn_result

