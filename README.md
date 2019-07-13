# Finding-Most-Similar-Words-NLP
Finding Most Important Words using word2vec Model of Google
![similar_words](https://user-images.githubusercontent.com/35392729/61172926-655a8d00-a5a9-11e9-88d0-4cd682ece25a.png)  

## Finding the mostt similar words to each word of sentence  
This code is implemented with the aim to find the sentence based on keyword entered by the user and then preporocess that sentence. Preprocessing includes operations like removing stop words from the text or removing non characters. Resultant sentence is tokenized and is passed to word2vec. It converts each word into word embedding of dimension 300 as set by me. There are some of the dimensions that one can set based on the documentation of word2vec. In the end, most similar words corresponding to each word of the vocabulary is displayed at the terminal. One can see such in the image added above. If anyone is finding difficult in understanding this, let me write down these in steps.  
<ol>
  <li> User is asked to enter the keyword from the text according to which he/she wants the sentence to get filtered.</li>
  <li> Sentence or sentences according to above filter are checked for stop words, non word characters.</li>
  <li> Such words are converted into the list and is passed to the word2vec model provided by gensim.</li>
  <li> Model is created and each word of the vocabulary is checked for the similar words</li>
  <li> Result is displayed on the terminal.</li>
  </ol>  
  
## How to run the code  

To run the code, first install the dependencies using the below command  

```
pip3 install -r requirements.txt  
```

Now please run below file  

```
python3 similar_words_word2vec.py

```

## Thanks
Happy Coding



