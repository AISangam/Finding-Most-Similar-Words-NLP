"""
This code is compiled to understand how to process the text using NLTK
In this code, first of all sentence corresponding to user chosen keyword 
is selected and then such sentence is checked for stop words, non-word 
characters. The refined list of words or toekns from such sentence is
passed to google Word2Vec model which will convert each word into 
word embedding with each word dimension as 300 as set by me. These are
predefined dimension and one have to choose between them only. In the 
end all the similar words to a single words is dsiplayed as the 
output
"""

# sentence tokenizer is imported from nltk
from nltk import sent_tokenize
# regex is imported
import re
# word2vec is provided by gensim
from gensim.models import Word2Vec
# stop words are imported from nltk corpus
from nltk.corpus import stopwords

# text is written which is to be analysed and preprocessed using NLP
text = "India (ISO: Bhārat), official name, the Republic of India,[e] \
(ISO: Bhārat Gaṇarājya), is a country in South Asia. It is the seventh- \
largest country by area, the second-most populous country, and the most \
populous democracy in the world. Bounded by the Indian Ocean on the south, \
the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, \
it shares land borders with Pakistan to the west;[f] China, Nepal, and Bhutan \
to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India \
is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands \
share a maritime border with Thailand and Indonesia."

# Senetence tokenization is performed here
sentence_tokenization = sent_tokenize(text)
# english stop words are stored in the variable stop_words
stop_words = stopwords.words("english")
# user is asked to enter the keyword according to which he wants the sentences to be extracted
user_choice_keyword = input("Enter the keyword to look for sentence where it occured: ")
# each sentence is looped
for each_sentence in sentence_tokenization:
    # search for the keyword specified by the user
    keyword_search = re.search(user_choice_keyword, each_sentence)
    # if match is found
    if keyword_search:
        # converting the string into list of strings
        list_with_Stop_words= each_sentence.split()
        # removing stop words
        list_without_stop_words =[each_word for each_word in list_with_Stop_words
                                 if each_word not in stop_words] 
        
        # removing non-words characters
        list_without_comma_semicolon_word = [re.sub(r"\W", "", each_word)  
                                            for each_word in list_without_stop_words]
        # outer list to append each word as a list in the main list
        outer_list =list()
        for each_word in list_without_comma_semicolon_word:
            each_word = [each_word]
            outer_list.append(each_word)                                   
        # see the output of the outer list
        print(outer_list)
        """
        word2vec will be used to produce the word embedding for each of the 
        words from the outer list. I will use the dimension of each word as
        300 and 4 threads to carry out the process and each word has to appear
        minuimum of 1 time  
        """
        model = Word2Vec(outer_list, min_count=1, size=300, workers=4)
        model.save("word2vec.model")
        model.save("model.bin")
        model = Word2Vec.load('model.bin')
        print(model.wv.vectors.shape)
        # vocabulary
        vocabulary_word2vec = list(model.wv.vocab)
        
        # loop to check the similar words for each of the words in the vocab
        for each_word in list_without_comma_semicolon_word:
            similar_word = model.most_similar(each_word)
            print("Similar word corresponding to {} is {}".format(each_word, similar_word))	
            print("\n")
        # if word is not found in the dictionary, then pass such words  
            if each_word not in vocabulary_word2vec:
                pass
        
 