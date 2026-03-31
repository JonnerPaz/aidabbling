import nltk
import re

nltk.download("stopwords")
from nltk.corpus import stopwords

en_stopwords = stopwords.words("english")

sentence = "it was too far to go to the shop and he did not want her to walk"
sentence_no_stopwords = " ".join(
    [word for word in sentence.split() if word not in en_stopwords]
)

# by removing "did" and "not", we exclude them from the stopword list
en_stopwords.remove("did")
en_stopwords.remove("not")

# now go will appear in the sentence if it already is there
en_stopwords.append("go")

sentence_no_stopwords_custom = " ".join(
    [word for word in sentence.split() if word not in en_stopwords]
)

my_folder = r"C:\desktop\notes"

result_search = re.search("pattern", r"string to contain the pattern")
if not result_search:
    print("pattern not found")

no_punct_reviews = r"[^\w\s]"  # remove punctuation
