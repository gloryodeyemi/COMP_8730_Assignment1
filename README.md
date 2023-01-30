# Spell Correction using Minimum Edit Distance (MED)
This experiment uses the MED **(Lavenshtein distance)** algorithm to find the correct spelling of misspelled words in the **Birkbeck** corpus from the **WordNet** dictionary. Where k={1, 5, 10}, the average success at k, is calculated.

**Keywords:** Spell correction, Lavenshtein distance, Corpus, Dictionary, Natural Language Processing.

## The Data
Two files, [SHEFFIELDDAT.643](https://github.com/gloryodeyemi/COMP_8730_Assignment1/blob/main/Data/SHEFFIELDDAT.643) and [FAWTHROP1DAT.643](https://github.com/gloryodeyemi/COMP_8730_Assignment1/blob/main/Data/FAWTHROP1DAT.643), out of the Birkbeck spelling error corpus by Roger Mitton was used for this experiment. They contain 1,193 words misspelled words in total and the correct equivalent of these words.

The WordNet dictionary contains 147,306 words.

## Requirements
You can find the modules and libraries used in this project in the [requirement.txt](https://github.com/gloryodeyemi/COMP_8730_Assignment1/blob/main/requirements.txt) file. You can also run the code below.
```
pip install -r requirements.txt
```

## Structure
* **[Data](https://github.com/gloryodeyemi/COMP_8730_Assignment1/tree/main/Data):** contains the Birbeck corpus files used for this project.

* **[images](https://github.com/gloryodeyemi/COMP_8730_Assignment1/tree/main/images):** contains the bar graph showing the average success at k.

* **[utils](https://github.com/gloryodeyemi/COMP_8730_Assignment1/tree/main/utils):** contains the essential functions for this project.

* **[Assignment_#1.ipynb](https://github.com/gloryodeyemi/COMP_8730_Assignment1/blob/main/Assignment_%231.ipynb)** and **[Assignment_#1.py](https://github.com/gloryodeyemi/COMP_8730_Assignment1/blob/main/Assignment_%231.py)** are python notebook and script that uses the functions in the utils folder to generate the results.

## Contact
Glory Odeyemi is currently undergoing her Masters program in Computer Science, Artificial Intelligence specialization at the [University of Windsor](https://www.uwindsor.ca/), Windsor, ON, Canada. You can connect with her on [LinkedIn](https://www.linkedin.com/in/glory-odeyemi-a3a680169/).

## References
1. [WordNet](https://en.wikipedia.org/wiki/WordNet)
2. [Birkbeck spelling error corpus](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/0643)
3. [Parallelization](https://python.plainenglish.io/parallelization-in-python-e5ac80b32b22)
4. [PyTrec-Eval-Terrier](https://pypi.org/project/pytrec-eval-terrier/)
