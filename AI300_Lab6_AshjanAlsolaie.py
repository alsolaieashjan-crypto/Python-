# Lab 6 Algorithm Plan
# Program I chose: Sentiment Analyzer (Medium Level)
# Program Description: This program takes a text input from the user 
# and determines if the mood is positive, negative, or neutral 
# based on specific keywords. It also identifies the index of the word
# that triggered the prediction. 

# Algorithm (Plain English):
# Create lists of words that represent 'positive' and 'negative' sentiments. 
# Ask the user to enter a sentence or a description of their day. 
# Clean the input by converting it to lowercase and using slicing to find words. 
# Loop through each word in the user's sentence. 
# For each word, check if it exists in the positive list or the negative list. 
# If a positive word is found, increment the positive counter.
# If a negative word is found, increment the negative counter.
# Compare the counters:
#  - If positive is higher, label "Positive".
#  - If negative is higher, label "Negative".
#  - If they are equal or no keywords are found, label "Neutral". 
# Print the sentiment result and the indicator index. 

# Create lists of sentiment indicators
positive_words = ["good","great","fun","enjoy","happy","excellent","amazing","relaxing","easy","interesting"]
negative_words = ["sad","bad","boring","terrible","horrible","hard", "tired", "difficult"]

# Ask the user for input
user_input = input("Enter a word: ").lower() + " " 

pos_count = 0
neg_count = 0
first_indicator_index = -1 
# If the user enters a sentence that contains both positive and negative words
# if the words are equal it display neutral

# Process the input manually using slicing 
words_found = 0
start_idx = 0
sentiment = "Neutral"
indicator_index = -1 
# Since the index starts from 0 we need to subtract 
# for example the third word is at index 2 

# Loop through the string to slice out words 
for i in range(len(user_input)):
    # Look for a space to find the end of a word
    if user_input[i] == " ":
        # Slicing the word from the start position to the current space
        word = user_input[start_idx:i].strip(".,!?;:")
        
        if word in positive_words:
            pos_count += 1
            # Track the index of the very first indicator found
            if first_indicator_index == -1:
                first_indicator_index = words_found
                
        elif word in negative_words:
            neg_count += 1
            # Track the index of the very first indicator found
            if first_indicator_index == -1:
                first_indicator_index = words_found
        
        start_idx = i + 1
        words_found += 1

# If the user wrote mixed sentiments
if pos_count > neg_count:
    sentiment = "Positive"
    indicator_index = first_indicator_index
elif neg_count > pos_count:
    sentiment = "Negative"
    indicator_index = first_indicator_index
else:
    # if the words are equal it will display neutral
    sentiment = "Neutral"
    indicator_index = first_indicator_index

print(f"Sentiment: {sentiment}")
if indicator_index != -1:
    print(f"Indicator Index: {indicator_index}")