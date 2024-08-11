# -*- coding: utf-8 -*-
"""NLP ASSIGNMENT 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ocouv-oKuLc73VwF8fqRXVbYtMURYhuk
"""

import pandas as pd

df_fake = pd.read_csv('/content/drive/MyDrive/NLP assignment 2/Fake.csv')
df_true = pd.read_csv('/content/drive/MyDrive/NLP assignment 2/True.csv')

df_fake['label'] = 'fake'
df_true['label'] = 'true'

df_combined = pd.concat([df_fake, df_true], ignore_index=True)

print(df_combined.shape)
print(df_combined.head())
print(df_combined.tail())
print(df_combined['label'].value_counts())

import matplotlib.pyplot as plt

df_combined['label'].value_counts().plot(kind='bar')
plt.title('Distribution of Labels')
plt.xlabel('Label')
plt.ylabel('Count')
plt.show()

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """

    Args:
      text:

    Returns:

    """
    tokens = word_tokenize(text.lower())
    tokens = [stemmer.stem(word) for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(tokens)

df_combined['text_clean'] = df_combined['text'].apply(preprocess_text)