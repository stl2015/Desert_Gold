import warnings
from asl_data import SinglesData
import operator


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # implement the recognizer
    Xlengths = test_set.get_all_Xlengths()
    
    for idx in Xlengths:
        
        X, lengths = Xlengths[idx]
        prob = {}

        for word in models:
            model = models[word]
            try:
                logL = model.score(X, lengths)
                prob[word] = logL
            except:
                prob[word] = float('-inf')  # can not score
        
        probabilities.append(prob)
        guesses.append(max(prob.items(), key=operator.itemgetter(1))[0])        
    
    # return probabilities, guesses
    return probabilities, guesses

