import nltk

nltk.download("punkt_tab")
from nltk.tokenize import word_tokenize, sent_tokenize

sentence = "Her cat's name is Luna. Her dog's name is Max."
tokens = word_tokenize(sentence)
print(tokens)
