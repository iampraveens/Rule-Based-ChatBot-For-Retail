import random
import pickle
import json
import numpy as np 

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow import keras

load_model = keras.models.load_model

lemmatizer = WordNetLemmatizer()
intents_data = json.loads(open('intents.json').read())

model = load_model('model.h5')
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

def predict(input_text):
    input_words = nltk.word_tokenize(input_text)
    input_words = [lemmatizer.lemmatize(w.lower()) for w in input_words]
    input_bag_of_words = [0] * len(words)

    for input_word in input_words:
        for i, word in enumerate(words):
            if input_word == word:
                input_bag_of_words[i] = 1

    input_bag_of_words = np.array([input_bag_of_words])

    predictions = model.predict(input_bag_of_words, verbose=0)[0]
    predicted_class = classes[np.argmax(predictions)]
    return predicted_class


def process_input(input_text):
    predicted_class = predict(input_text)
    
    for intent in intents_data["intents"]:
                if intent["tag"] == predicted_class:
                    return random.choice(intent["responses"])
    return "I didn't understand your request."
                
# while True:
#     message = input("You: ") 
#     response = process_input(message)
#     print("Bot:", response)
