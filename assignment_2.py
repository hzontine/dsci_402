#Hannah Zontine
#Assignment 2

def word_breaks(original_word, word_list):
    firstPhrase = findPhrase([], original_word,word_list) 
    phrases = []
    nextPhrases = [firstPhrase[:]]
    oldPhrases = []
    while True:
        phrases = nextPhrases
        nextPhrases = []
        if len(phrases) == 0:
            break;
        for phrase in phrases:
            if phrase not in oldPhrases:
                oldPhrases.append(phrase)
            combined_words = []
            for word in phrase:
                combined_words.append(word)
                phraseAgain = findPhrase(combined_words, original_word, word_list)
                if phraseAgain != False and phraseAgain not in nextPhrases and phraseAgain not in oldPhrases:
                    nextPhrases.append(phraseAgain) 
    print(oldPhrases)
        
def findPhrase(start, original_word, word_list):
    current_phrase = start[:]
    if len(start) > 0:
        current_word = start[-1]
    else:
        current_word = ""
    combined_word_length = 0
    for word in current_phrase:
        combined_word_length += len(word)
    previous_word_length = 0
    word_length = 0
    valid_phrase = True
    while True:
        previous_word_length = word_length
        if combined_word_length == len(original_word):
            return False
        for letter in original_word[combined_word_length:]:
            current_word  += letter
            if current_word in word_list: 
                current_phrase.append(current_word)
                current_word = ""              
        if len(current_word) > len(original_word):
            return tuple(current_phrase)
        word_length = 0
        for word in current_phrase:
            word_length += len(word)
        if word_length != len(original_word):
            valid_phrase = False
        else:
            valid_phrase = True
        if valid_phrase:
            return tuple(current_phrase)
        if len(original_word) <= word_length or len(original_word) <= word_length + len(current_word): 
            if len(current_phrase) == 0:
                return False
            else:
                current_word = current_phrase[-1]
                combined_word_length = 0
                for word in current_phrase:
                    combined_word_length += len(word)
                
                if combined_word_length == len(original_word):
                    return tuple(current_phrase)
                current_phrase.pop()