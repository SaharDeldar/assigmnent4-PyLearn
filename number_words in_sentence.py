def Number_of_words(sentences):
    words=sentences.split(' ')
    number=len(words)
    print('The number of words in a sentence ', number)

sentences=input('Enter the sentence:')
Number_of_words(sentences)
