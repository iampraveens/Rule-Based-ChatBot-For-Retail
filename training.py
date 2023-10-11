import random
import pickle
import json
import numpy as np 

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow import keras

Sequential = keras.models.Sequential
Dense = keras.layers.Dense
Activation = keras.layers.Activation
Dropout = keras.layers.Dropout
Adam = keras.optimizers.Adam
InputLayer = keras.layers.InputLayer

lemmatizer = WordNetLemmatizer()

intents_data = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']
training_data = []

for intent in intents_data["intents"]:
    if intent["tag"] not in classes:
        classes.append(intent["tag"])
    for pattern in intent["patterns"]:
        pattern_words = nltk.word_tokenize(pattern)
        words += pattern_words
        documents.append((pattern_words, intent["tag"]))

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
words = sorted(set(words))

empty_output = [0] * len(classes)

for document in documents:
            bag_of_words = []
            pattern_words = document[0]
            pattern_words = [lemmatizer.lemmatize(w.lower()) for w in pattern_words]
            for word in words:
                bag_of_words.append(1 if word in pattern_words else 0)
                
            output_row = empty_output.copy()
            output_row[classes.index(document[1])] = 1
            training_data.append([bag_of_words, output_row])
            
random.shuffle(training_data)
training_data = np.array(training_data, dtype="object")

X = np.array([data[0] for data in training_data])
y = np.array([data[1] for data in training_data])

model = Sequential()
model.add(InputLayer(input_shape=(None, X.shape[1])))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(y.shape[1], activation='softmax'))

optimizer = Adam(learning_rate=0.01)
model.compile(loss="categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])
history = model.fit(X, y, epochs=200, batch_size=5, verbose=1)

with open('words.pkl', 'wb') as words_file:
    pickle.dump(words, words_file)

with open('classes.pkl', 'wb') as classes_file:
    pickle.dump(classes, classes_file)
    
model.save('model.h5', history)
