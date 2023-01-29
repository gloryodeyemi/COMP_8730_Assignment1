# # Assignment 1
# 
# ### Glory Odeyemi
# 
# #### 28-Jan-2023

import nltk
import multiprocessing as mp
import time
import itertools
from utils.k_success import top_k_words, success_at_k, average_k
import matplotlib.pyplot as plt
%matplotlib inline

nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import wordnet as wn
print("Total number of words in Wordnet = ", len(list(wn.words())))

birkbeck_data = []
with open('Data/FAWTHROP1DAT.643', 'r') as file_data1:
    for line in file_data1:
        data = line.split()
        birkbeck_data.append(data)
    
with open('Data/SHEFFIELDDAT.643', 'r') as file_data2:
    for line in file_data2:
        data = line.split()
        birkbeck_data.append(data)

birkbeck_data = sorted(birkbeck_data)
print("Total number of words in Birbeck corpus = ", len(birkbeck_data))


# Getting the top k words

# Without parallelization
start_time = time.time()
top_k_result = []
for data_row in birkbeck_data[:10]:
    top_k_result.append(top_k_words(data_row))
    
print("--- Without parallelization: %s seconds ---" % (time.time() - start_time))


# With parallelization
pool = mp.Pool()
start_time = time.time()
top_k_result = []
top_k_result.append(pool.map(top_k_words, birkbeck_data[:10]))
    
print("--- With parallelization: %s seconds ---" % (time.time() - start_time))


# Getting the top k-words for all incorrect token in the birkbeck corpus.
top_k_result = []
start_time = time.time()
top_k_result.append(pool.map(top_k_words, birkbeck_data))

print(top_k_result[0][-5:])


# Getting the success at k
success = success_at_k(top_k_result[0])
print(dict(itertools.islice(reversed(success.items()), 5)))

# Getting the average success at k
avg_success = average_k(success)
print(avg_success)

# bar chart showing the avegare success at k
x = avg_success.keys()
y = avg_success.values()

colors = ['green','blue','purple']
plt.bar(x, y, color=colors)
plt.title('Average success at k', fontsize=14)
plt.xlabel('Top-k', fontsize=14)
plt.ylabel('Average', fontsize=14)
plt.grid(False)

for i in range(len(x)):
    plt.text(i,list(y)[i],list(y)[i], ha='center')

plt.savefig('average.png',dpi=400)
plt.show()

