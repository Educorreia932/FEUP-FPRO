def count(word, phrase):
    word = word.lower()
    phrase = phrase.lower()  

    phrase_split = phrase.split()
    
    counter = 0
    
    for phrase_word in phrase_split:
        if phrase_word == word:
            counter += 1  
    
    return counter
  