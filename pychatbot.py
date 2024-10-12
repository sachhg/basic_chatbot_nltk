import nltk
import re
import random
from nltk.corpus import wordnet

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')


# Function to preprocess the user input
def preprocess_input(user_input):
    # Convert to lowercase
    user_input = user_input.lower()
    # Remove punctuation and special characters
    user_input = re.sub(r'[^\w\s]', '', user_input)
    # Tokenize the sentence into words
    tokens = nltk.word_tokenize(user_input)
    return tokens



# Find synonyms for a word using WordNet (for more flexible matching)
def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)

# Check if the user's input contains any keywords or synonyms of keywords
def keyword_match(user_input_tokens, keywords):
    for word in user_input_tokens:
        for key in keywords:
            if word == key or word in get_synonyms(key):
                return True
    return False



# Predefined set of responses
responses = {
    'greeting': ['Hello!', 'Hi there!', 'Greetings!', 'Hey!'],
    'goodbye': ['Goodbye!', 'See you later!', 'Take care!'],
    'about': ['I am a simple chatbot created using Python and NLP.', 'I can help with basic conversations!'],
    'default': ["I'm sorry, I didn't understand that.", 'Could you say that again?', "I'm not sure I can help with that."]
}

# Keywords for matching
keywords = {
    'greeting': ['hello', 'hi', 'hey', 'greetings'],
    'goodbye': ['bye', 'goodbye', 'see you', 'later'],
    'about': ['who', 'what', 'you', 'yourself']
}

# Chat function to generate responses based on user input
def get_response(user_input):
    tokens = preprocess_input(user_input)
    
    # Greeting
    if keyword_match(tokens, keywords['greeting']):
        return random.choice(responses['greeting'])
    
    # Goodbye
    elif keyword_match(tokens, keywords['goodbye']):
        return random.choice(responses['goodbye'])
    
    # About the bot
    elif keyword_match(tokens, keywords['about']):
        return random.choice(responses['about'])
    
    # Default response if nothing matches
    else:
        return random.choice(responses['default'])



def chatbot():
    print("Chatbot: Hi! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: " + random.choice(responses['goodbye']))
            break
        else:
            response = get_response(user_input)
            print("Chatbot: " + response)

# Start chatting
chatbot()


