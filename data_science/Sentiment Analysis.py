#!/usr/bin/env python
# coding: utf-8

# In[1]:


# get_ipython().system('pip install nltk')

import re
import nltk
from sklearn.datasets import load_files
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords


movie_data = load_files('./data/sentiment_dataset')
X, y = movie_data.data, movie_data.target


print(f'length of X: {len(X)}')
print(f'length of y: {len(y)}')


# remove special characters

documents = []

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english", ignore_stopwords=True)


for i in range(0, len(X)):
    document = str(X[i])
    
    # Remove all the special characters
    document = re.sub(r'\W', ' ', document)
    
    # Converting to Lowercase
    document = document.lower()
    
    # remove single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    
    # Lemmatization
    document = document.split()
    document = [stemmer.stem(word) for word in document]
    document = ' '.join(document)
    
    documents.append(document)


# training and testing set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(documents, y, test_size=0.2)


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def evaluate_classifier(classifier, X_test, y_test):
    y_pred = classifier.predict(X_test)

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))


print('not' in stopwords.words('english'))


from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.pipeline import Pipeline


#inner_classifier = RandomForestClassifier(n_estimators=400)
inner_classifier = SGDClassifier(
    loss='hinge', 
    penalty='l2',
    alpha=1e-3, 
    random_state=42,
    max_iter=10,
    tol=None
)

classifier = Pipeline([
    ('vect', CountVectorizer(
        max_features=5000,
        min_df=5,
        max_df=0.8, 
        stop_words=stopwords.words('english'),
        analyzer='word',
        strip_accents='unicode',
        ngram_range=(1, 3)
    )),
    ('tfidf', TfidfTransformer()),
    ('classifier', inner_classifier)
])


classifier = classifier.fit(X_train, y_train)


evaluate_classifier(classifier, X_test, y_test)


# perform a grid search over various parameters
from sklearn.model_selection import GridSearchCV

parameters = {
    'vect__ngram_range': [(1, 2), (1, 3), (1, 4)],
    'vect__max_features': [1500, 2000, 3000, 5000, 6000]
}

gs_classifier = GridSearchCV(classifier, parameters, cv=5, iid=False, n_jobs=-1)


# perform grid searh on a subset of the data
gs_classifier = gs_classifier.fit(X_train[:400], y_train[:400])


# print out the best values for each parameter
for param_name in sorted(parameters.keys()):
    print("%s: %r" % (param_name, gs_classifier.best_params_[param_name]))







