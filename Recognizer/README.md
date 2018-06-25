## Probabilistic Models
## Project: Sign Language Recognition System

### Install

This project requires **Python 3** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [SciPy](https://www.scipy.org/)
- [scikit-learn](http://scikit-learn.org/0.17/install.html)
- [pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [jupyter](http://ipython.org/notebook.html)
- [hmmlearn](http://hmmlearn.readthedocs.io/en/latest/)
- [arpa](https://pypi.python.org/pypi/arpa/0.1.0b1)

##### Provided Raw Data

The data in the `asl_recognizer/data/` directory was derived from 
the [RWTH-BOSTON-104 Database](http://www-i6.informatik.rwth-aachen.de/~dreuw/database-rwth-boston-104.php). 
The hand positions (`hand_condensed.csv`) are pulled directly from 
the database [boston104.handpositions.rybach-forster-dreuw-2009-09-25.full.xml](boston104.handpositions.rybach-forster-dreuw-2009-09-25.full.xml). The three markers are:

*   0  speaker's left hand
*   1  speaker's right hand
*   2  speaker's nose
*   X and Y values of the video frame increase left to right and top to bottom.
 
Take a look at the sample [ASL recognizer video](http://www-i6.informatik.rwth-aachen.de/~dreuw/download/021.avi)
to see how the hand locations are tracked.

The videos are sentences with translations provided in the database.  
For purposes of this project, the sentences have been pre-segmented into words 
based on slow motion examination of the files.  
These segments are provided in the `train_words.csv` and `test_words.csv` files
in the form of start and end frames (inclusive).

The videos in the corpus include recordings from three different ASL speakers.
The mappings for the three speakers to video are included in the `speaker.csv` 
file.

### Solution

Implemented SLM with HMM in Viterbi algorithm. The HMM probabilities are the probabilites of observation in each state (word) solved in GaussianHMM model; SLM probabilities from arpa library are the transition probabilities between the states. Top 10 HMM probabilities are kept in the search to expedite the process. The execution time of Viterbi algorithm for given LM scale parameter is ~ 10 seconds in my environment.

*   a) original HMM with features_polar (BIC as score function) alone has a WER of 55%.
*   b) 2-gram SLM with HMM achieves a WER of 49%.
*   c) 3-gram SLM with HMM achieves a WER of 39%.
